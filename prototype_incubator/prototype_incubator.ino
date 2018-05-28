#include <PID_v1.h>               // library for the PID
#include "Adafruit_SHT31.h"       // library for the tempurature sensor
#include <Adafruit_Sensor.h>      // unified sensor library
#include <Adafruit_TSL2561_U.h>   // library for the light sensor
#include <SPI.h>                  // library for the pins the SD card is using
#include <SD.h>                   // library for the SD card
#include <Wire.h>
#include "RTClib.h"               // library for the RTC

/* Set the appropriate digital I/O pin connections. These are the pin */

const int chipSelect = 10; // set the pin for the SD card

const int lights = 4;   // PWM pin for the lights
const int peltier = 5;  // PWM pin for the peltier
const int fan = 3;      // PWM pin for the fan

/* define the sensors */

RTC_PCF8523 rtc;                                                                        // name the clock
Adafruit_TSL2561_Unified tsl = Adafruit_TSL2561_Unified(TSL2561_ADDR_FLOAT, 12345);     // name the lux sensor
Adafruit_SHT31 sht31 = Adafruit_SHT31();                                                // name the temp sensor

// char daysOfTheWeek[7][12] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
/* The array os string used to store the data as it comes from the sensors */

/* PID variables and constants */
double Setpoint, Input, Output;

//Define the aggressive and conservative Tuning Parameters
const double aggKp=4, aggKi=0.2, aggKd=1;
const double consKp=1, consKi=0.05, consKd=0.25;

//Specify the links and initial tuning parameters
PID myPID(&Input, &Output, &Setpoint, consKp, consKi, consKd, DIRECT);

/* Setpoints */

const int luxSet = 50;
const int tempSet = 18;

/**************************************************************************/
/*
    Configures the gain and integration time for the TSL2561
*/
/**************************************************************************/
void configureLux(void)
{ 
  /* You can also manually set the gain or enable auto-gain support */
  // tsl.setGain(TSL2561_GAIN_1X);      /* No gain ... use in bright light to avoid sensor saturation */
  // tsl.setGain(TSL2561_GAIN_16X);     /* 16x gain ... use in low light to boost sensitivity */
  tsl.enableAutoRange(true);            /* Auto-gain ... switches automatically between 1x and 16x */
  
  /* Changing the integration time gives you better sensor resolution (402ms = 16-bit data) */
  // tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);      /* fast but low resolution */
  tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_101MS);  /* medium resolution and speed   */
  // tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_402MS);  /* 16-bit data but slowest conversions */
}

void configureSD() {
  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    while (1);
  }
}

String timeString() {
  DateTime now = rtc.now();
  char buffer[18];
  snprintf(buffer, 18, "%04d%02d%02d_%02d:%02d:%02d", now.year(), now.month(), now.day(), now.hour(), now.minute(), now.second());
  return buffer;
}
/**************************************************************************/
/*
    Setup code
*/
/**************************************************************************/

void setup() {

  /* set up the output pins */

  pinMode(lights, OUTPUT);
  pinMode(peltier, OUTPUT);
  pinMode(fan, OUTPUT);

  /* set up serial */
  Serial.begin(9600);

  while (!Serial)
    delay(10);     // will pause Zero, Leonardo, etc until serial console opens

  /* set up temp sensor */
  if (! sht31.begin(0x44)) {   // Set to 0x45 for alternate i2c addr
    Serial.println("Couldn't find SHT31");
    while (1) delay(1);
  }

  /* Initialise the lux sensor */
  //use tsl.begin() to default to Wire, 
  //tsl.begin(&Wire2) directs api to use Wire2, etc.
  if(!tsl.begin())
  {
    /* There was a problem detecting the TSL2561 ... check your connections */
    Serial.print("Ooops, no TSL2561 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
  
  /* Setup the lux sensor gain and integration time */
  configureLux();
        
  /* Setup the SD card */
  configureSD();

  /*Display the time for sanity*/
  DateTime now = rtc.now();
  Serial.print("The clock is set to: "); Serial.print(now.hour()); Serial.print(':'); Serial.print(now.minute()); Serial.print(':'); Serial.print(now.second());
  Serial.print(" on "); Serial.print(now.year(), DEC); Serial.print('/'); Serial.print(now.month(), DEC); Serial.print('/'); Serial.println(now.day(), DEC);
  Serial.println("-------------------------------");
  Serial.println();
  
  /*initialize the variables the PID is linked to*/
  Input = tempSet;
  Setpoint = tempSet;

  /*turn the PID on*/
  myPID.SetMode(AUTOMATIC);
}
  
/**************************************************************************/
/*
    Main loop code
*/
/**************************************************************************/

void loop() {

  /* log - assign the data to an array and print to serial */

  String sensorData[4]; // for some reason if this isn't 4 then the last array spot (lux, sensorData[3]) is wonky

  sensorData[0] = timeString();
  Serial.println(sensorData[0]);

  float t = sht31.readTemperature();
  sensorData[1] = t;
  Input = t;
  Serial.print("Temp *C = "); Serial.println(sensorData[1]);

  sensorData[2] = sht31.readHumidity();
  Serial.print("Hum. % = "); Serial.println(sensorData[2]);

  sensors_event_t event;
  tsl.getEvent(&event);
  sensorData[3] = event.light;
  Serial.print("lux = "); Serial.println(sensorData[3]);
  
  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
  String daylog = sensorData[0].substring(2,7);
  daylog += ".log";
  File dataFile = SD.open(daylog, FILE_WRITE);

  // if the file is available, write to it:
  if (dataFile) {
    for (int i=0; i<=3; i++) {
      dataFile.print(sensorData[i]); dataFile.print(", ");
    }
    dataFile.println(Output);
    dataFile.close();
  }
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening datalog");
    Serial.println(daylog);
  }
  
  /*Control fan speed*/
  analogWrite(fan, 50);

  /*Control LED*/
  digitalWrite(lights, HIGH); 
 
  /*PID for temputature*/
  double gap = abs(Setpoint-Input); //distance away from setpoint
  if(gap<0.5)
  {  //we're close to setpoint, use conservative tuning parameters
    myPID.SetTunings(consKp, consKi, consKd);
  }
  else
  {
     //we're far from setpoint, use aggressive tuning parameters
     myPID.SetTunings(aggKp, aggKi, aggKd);
  }

  myPID.Compute();
  analogWrite(peltier,Output);
  /* for debugging PID */
  Serial.print("gap = "); Serial.println(gap);
  Serial.print("PWM input = "); Serial.println(Input);
  Serial.print("PWM output = "); Serial.println(Output);
  Serial.println();
    
  delay(2000);
}
