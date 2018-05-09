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
  tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);      /* fast but low resolution */
  // tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_101MS);  /* medium resolution and speed   */
  // tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_402MS);  /* 16-bit data but slowest conversions */

  /* Update these values depending on what you've set above! */  
  Serial.println("------------------------------------");
  Serial.print  ("Gain:         "); Serial.println("Auto");
  Serial.print  ("Timing:       "); Serial.println("13 ms");
  Serial.println("------------------------------------");
}

void setup() {
  // put your setup code here, to run once:
    /* Display some basic information on this sensor */
  displaySensorDetails();
  
  /* Setup the sensor gain and integration time */
  configureSensor();


}

void loop() {
  // put your main code here, to run repeatedly:

}
