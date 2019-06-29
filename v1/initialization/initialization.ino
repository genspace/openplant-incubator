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
const int peltier = 3;  // PWM pin for the peltier
const int fan = 9;      // PWM pin for the fan

/* define the sensors */

RTC_PCF8523 rtc;                                                                        // name the clock
Adafruit_TSL2561_Unified tsl = Adafruit_TSL2561_Unified(TSL2561_ADDR_FLOAT, 12345);     // name the lux sensor
Adafruit_SHT31 sht31 = Adafruit_SHT31();                                                // name the temp sensor

char daysOfTheWeek[7][12] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

/**************************************************************************/
/*
    Displays some basic information on this sensor from the unified
    sensor API sensor_t type (see Adafruit_Sensor for more information)
*/
/**************************************************************************/
void displaySensorDetails(void)
{
  sensor_t sensor;
  tsl.getSensor(&sensor);
  Serial.println("------------------------------------");
  Serial.print  ("Sensor:       "); Serial.println(sensor.name);
  Serial.print  ("Driver Ver:   "); Serial.println(sensor.version);
  Serial.print  ("Unique ID:    "); Serial.println(sensor.sensor_id);
  Serial.print  ("Max Value:    "); Serial.print(sensor.max_value); Serial.println(" lux");
  Serial.print  ("Min Value:    "); Serial.print(sensor.min_value); Serial.println(" lux");
  Serial.print  ("Resolution:   "); Serial.print(sensor.resolution); Serial.println(" lux");
  Serial.println("------------------------------------");
  Serial.println("");
  delay(500);
}

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
  Serial.println("------------------------------------");
  Serial.print  ("Gain:         "); Serial.println("Auto");
  Serial.print  ("Timing:       "); Serial.println("101 ms");
  Serial.println("------------------------------------");

}

void configureSD() {
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
}

void setup() {
  // put your setup code here, to run once:

  /* set up the sensor and logger */
  Serial.begin(9600);

  while (!Serial)
    delay(10);     // will pause Zero, Leonardo, etc until serial console opens

  /* Initialize temp sensor */
  Serial.println("SHT31 test"); Serial.println("");
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

  /* Display some basic information on this sensor */
  displaySensorDetails();

  /* Setup the sensor gain and integration time */
  configureSensor();

  /*set up the SD card*/
  configureSD();
  
  // Initialize a new chip by turning off write protection and clearing the
  if (! rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1);
  }

  if (! rtc.initialized()) {
    Serial.println("RTC is NOT running!");
    // following line sets the RTC to the date & time this sketch was compiled
    // rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
    // This line sets the RTC with an explicit date & time, for example to set
    // January 21, 2014 at 3am you would call:
    rtc.adjust(DateTime(2018, 5, 28, 16, 11, 50));
  }
}

// Loop and print the time every second.
void loop() {
  DateTime now = rtc.now();
    
  Serial.print(now.year(), DEC); Serial.print('/'); Serial.print(now.month(), DEC); Serial.print('/'); Serial.print(now.day(), DEC);
  Serial.print(" ("); Serial.print(daysOfTheWeek[now.dayOfTheWeek()]); Serial.print(") ");
  Serial.print(now.hour()); Serial.print(':'); Serial.print(now.minute()); Serial.print(':'); Serial.println(now.second());
    
  Serial.print("Temp *C = "); Serial.println(sht31.readTemperature());
  Serial.print("Hum. % = "); Serial.println(sht31.readHumidity());
  
  sensors_event_t event;
  tsl.getEvent(&event);
  Serial.print("lux = "); Serial.println(event.light);
  Serial.println();
  delay(2000);
}


