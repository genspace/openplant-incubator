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

const int lights = 4;   // pin for the lights
const int peltier = 5;  // PWM pin for the peltier
const int fan = 3;      // PWM pin for the fan

//const int innerSensefan = 8;  // Sensor for the inner fan speed
//const int outerSensefan = 7;  // Sensor for the outer fan speed

/* define the sensors */

RTC_PCF8523 rtc;                                                                        // name the clock
Adafruit_TSL2561_Unified tsl = Adafruit_TSL2561_Unified(TSL2561_ADDR_FLOAT, 12345);     // name the lux sensor
Adafruit_SHT31 sht31 = Adafruit_SHT31();                                                // name the temp sensor

// char daysOfTheWeek[7][12] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
/* The array os string used to store the data as it comes from the sensors */

/* PID variables and constants */
double Setpoint, Input, Output=255;

//Define the Tuning Parameters foir when the light is on and when it is off
const double lightKp=150, lightKi=20, lightKd=1;
//const double darkKp=50, darkKi=10, darkKd=15;

//Specify the links and initial tuning parameters
PID myPID(&Input, &Output, &Setpoint, lightKp, lightKi, lightKd, REVERSE);

/* Setpoints */

//const int luxSet = 50;
const int tempSet = 21;

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

/* not accurate
double fanSpeed(int fan) {
  unsigned long rise = pulseIn(fan, HIGH);
  unsigned long fall = pulseIn(fan, LOW);
  unsigned long total = rise + fall;
  double rpm = 1000000/2*total*60;
  return rpm;
}
*/

/**************************************************************************/
/*
    Setup code
*/
/**************************************************************************/

void setup() {

  /* set up the output pins */

  pinMode(lights, OUTPUT);
  pinMode(peltier, OUTPUT);

  /* set up the input pins */

  //pinMode(innerSensefan, INPUT_PULLUP);
  //pinMode(outerSensefan, INPUT_PULLUP);

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

  /* adjust timer 2 to give pin 3 and 11 25kHz output*/
  TCCR2A = 0x23;
  TCCR2B = 0x09;  // select timer2 clock
  OCR2A = 79;  // aiming for 25kHz
  pinMode(fan, OUTPUT);
  OCR2B = 62;  // set the PWM duty cycle

  
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
  
  /*Control LED*/
  int noon2night = sensorData[0].substring(9,11).toInt();
  if (noon2night >= 4 && noon2night <=12) {
    digitalWrite(lights, LOW); //for testing purposes set high
  }
  else {
    digitalWrite(lights, HIGH);
  }
 
  /*PID for temputature*/
  double gap = Input-Setpoint; //distance away from setpoint
  if(gap>1) { //we're far from setpoint, 
     Output = 255;
    }
  else {
     //we're close to setpoint, use PID
     //myPID.SetTunings(lightKp, lightKi, lightKd);
     //myPID.SetControllerDirection(REVERSE);
     myPID.Compute();
    }

  analogWrite(peltier,Output);
  /* for debugging PID */
g  Serial.print("gap = "); Serial.println(gap);
  Serial.print("PWM output = "); Serial.println(Output);
  // analogWrite(peltier, 255);

  /*Control fan speed*/
  //analogWrite(fan, 100);
  OCR2B = map(Output, 0, 255, 30, 79);
  Serial.print("Fan output (%) = "); Serial.println(double OCR2B / 79 * 100);
  Serial.println();

  /*print the calcualed RPM
  Serial.print("Inner fan (RPM) = "); Serial.println(fanSpeed(innerSensefan));
  Serial.print("Outer fan (RPM) = "); Serial.println(fanSpeed(outerSensefan));
  Serial.println();
  */
  
  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
  String daylog = sensorData[0].substring(2,8);
  daylog += ".log";
  File dataFile = SD.open(daylog, FILE_WRITE);

  // if the file is available, write to it:
  if (dataFile) {
    for (int i=0; i<=3; i++) {
      dataFile.print(sensorData[i]); dataFile.print(", ");
    }
    dataFile.print(Input); dataFile.print(", ");
    dataFile.print(OCR2B); dataFile.print(", ");
    dataFile.println(Output);
    dataFile.close();
  }
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening datalog");
    Serial.println(daylog);
  }
  
  delay(2000);
}
