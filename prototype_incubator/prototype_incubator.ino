#include <PID_v1.h>
#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_SHT31.h"       // library for the tempurature sensor
#include <Adafruit_Sensor.h>      // unified sensor library
#include <Adafruit_TSL2561_U.h>   // library for the light sensor
#include <SPI.h>
#include <SD.h>
#include <Time.h>
#include <DS1302.h>


const int chipSelect = 10; // set the pin for the SD card

const int lights = 5;   // PWM pin for the lights
const int peltier = 3;  // PWM pin for the peltier
const int fan = 6;      // PWM pin for the fan

Adafruit_TSL2561_Unified tsl = Adafruit_TSL2561_Unified(TSL2561_ADDR_FLOAT, 12345);     // name the lux sensor
Adafruit_SHT31 sht31 = Adafruit_SHT31();                                                // name the temp sensor

DS1302 rtc(9,8,7);  // set the pins for the clock

//Define Variables we'll be connecting to
double Setpoint, Input, Output;

//Define the aggressive and conservative Tuning Parameters
double aggKp=4, aggKi=0.2, aggKd=1;
double consKp=1, consKi=0.05, consKd=0.25;

//Specify the links and initial tuning parameters
PID myPID(&Input, &Output, &Setpoint, consKp, consKi, consKd, DIRECT);

int adjustlux = 50;

/**************************************************************************/
/*
    Configures the gain and integration time for the TSL2561
*/
/**************************************************************************/
void configureSensor(void)
{
  /* You can also manually set the gain or enable auto-gain support */
  // tsl.setGain(TSL2561_GAIN_1X);      /* No gain ... use in bright light to avoid sensor saturation */
  // tsl.setGain(TSL2561_GAIN_16X);     /* 16x gain ... use in low light to boost sensitivity */
  tsl.enableAutoRange(true);            /* Auto-gain ... switches automatically between 1x and 16x */
  
  /* Changing the integration time gives you better sensor resolution (402ms = 16-bit data) */
  // tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);      /* fast but low resolution */
  tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_101MS);  /* medium resolution and speed   */
  // tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_402MS);  /* 16-bit data but slowest conversions */

  /* Update these values depending on what you've set above! */  
  Serial.println("----------------------------------");
  Serial.print  ("Gain:         "); Serial.println("Auto");
  Serial.print  ("Timing:       "); Serial.println("13 ms");
  Serial.println("----------------------------------");
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

  /* set up the sensor and logger */
  Serial.begin(9600);

  while (!Serial)
    delay(10);     // will pause Zero, Leonardo, etc until serial console opens

  Serial.println("SHT31 test"); Serial.println("");
  if (! sht31.begin(0x44)) {   // Set to 0x45 for alternate i2c addr
    Serial.println("Couldn't find SHT31");
    while (1) delay(1);
  }
  
  /* Setup the sensor gain and integration time */
  sensor_t sensor;
  tsl.getSensor(&sensor);
  delay(500);
  configureSensor();

  Serial.println("Light Sensor Test"); Serial.println("");
  
  /* Initialise the lux sensor */
  //use tsl.begin() to default to Wire, 
  //tsl.begin(&Wire2) directs api to use Wire2, etc.
  if(!tsl.begin())
  {
    /* There was a problem detecting the TSL2561 ... check your connections */
    Serial.print("Ooops, no TSL2561 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
    
  /* We're ready to go! */
  Serial.println("----------------------------------");
    
  Serial.print("Initializing SD card...");

  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    while (1);
  }
  Serial.println("card initialized.");
  Serial.println("");
  Serial.println("----------------------------------");

  rtc.halt(false);
  rtc.writeProtect(true);

  String chardate = rtc.getDateStr();;
  Serial.print("The clock is set to: "); Serial.print(rtc.getTimeStr()); Serial.print(" on "); Serial.println(chardate);
  Serial.println("");
  Serial.println("----------------------------------");

   //initialize the variables we're linked to
  Input = analogRead(0);
  Setpoint = 27;

  //turn the PID on
  myPID.SetMode(AUTOMATIC);
}
  
/**************************************************************************/
/*
    Main loop code
*/
/**************************************************************************/

void loop() {

  /* log */

  String sensorData[4]; // for some reason if this isn't 4 then the daylog string overlflows into the sensorData array
  
  /* set points */
  int set_lux = 50;
  
  //beign the code for the tempurature sensor
  
  float t = sht31.readTemperature();
  float h = sht31.readHumidity();
  sensors_event_t event;
  tsl.getEvent(&event);

  sensorData[0] = rtc.getTimeStr();
  Serial.println(sensorData[0]);

  sensorData[1] = t;
  Input = t;
  Serial.print("Temp *C = "); Serial.println(sensorData[1]);
  Serial.print("PWM output = "); Serial.println(Output);
  
  sensorData[2] = h;
  Serial.print("Hum. % = "); Serial.println(sensorData[2]);

  sensorData[3] = event.light;
  Serial.print("lux = "); Serial.println(sensorData[3]);
  
  Serial.println();
  
  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
  String daylog = rtc.getDateStr(FORMAT_SHORT, FORMAT_LITTLEENDIAN, '-'); //the option BIG_LITTLEENDIAN messes up the data so the date format is stuck as mm-dd-yy
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
    Serial.println("error opening datalog.txt");
  }
  //fan speed
  analogWrite(fan, 10);

  //lights
  
  if (set_lux>sensorData[3].toInt()) {
    adjustlux += 10;
    analogWrite(lights, adjustlux);
  }
  else if (set_lux<sensorData[3].toInt()) {
    adjustlux -= 10;
    analogWrite(lights, adjustlux);
  }
  else {
    //nothing
  }

  //PID for temputature
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
  
  delay(2000);
}
