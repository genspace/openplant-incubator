/***************************************************
  This is an test program to verify the wiring is correct. 
  If the humidity above 60% the lights and Peltier turn on. 
  You can trigger this by putting a finger on the humidty sensor.

  Designed specifically to work with the SHT31-D sensor from Adafruit
  ----> https://www.adafruit.com/products/2857

  These sensors use I2C to communicate, 2 pins are required to
  interface

  Wired the SHT31-D to the Arduino following the first diagram here:
  http://cactus.io/hookups/sensors/temperature-humidity/sht31/hookup-arduino-to-sensirion-sht31-temp-humidity-sensor

  Connect the LED strip to the gate following the diagram in the Cloud-based Lab Monitor google doc:
  Power Supply - to breadboard minus rail
  Power Supply + to LED strip red wire
  LED strip black wire to gate middle pin

  The small LED does not light up because when the humidity sensor is connected, the Arduino 
  does not have enough power to power it.
 ****************************************************/

#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_SHT31.h"

const int lights = 4;
const int peltier = 5;
const int ledPin = LED_BUILTIN;// the number of the LED pin, this is pin 13 for the LED
const int humidityThreshold = 60.0;

int ledState = LOW;
int ledStripState = LOW;
int peltierState = LOW;

/*
  This next section defines a a subclass of the tempurature sensing
  hardware as Tempsensor which will hold the information from the last
  time the sensor was polled

*/

class Tempsensor: public Adafruit_SHT31 {
  private:
    byte readInterval;            // the time in seconds between readings
    unsigned long lastUpdate;     // to store the millis

  public:
    float temp;                   // to store the tempurature data
    float humidity;               // to store the humidity data

    /*
      Constructor, also should call the base class constructor

    */

    Tempsensor(byte seconds) {
      readInterval = seconds;
      temp = 0;
      humidity = 0;
      lastUpdate = millis();
    }

    void Update() {
      unsigned long currentMillis = millis();

      if ((currentMillis - lastUpdate) >= (readInterval * 1000)) {
        lastUpdate = millis();
        temp = readTemperature();
        humidity = readHumidity();
      }
      if (humidity > humidityThreshold) {
        if (ledState == LOW) {
          ledState = HIGH;
          Serial.println("Humidity is >= " + String(humidityThreshold) + ", turning small LED on");
          digitalWrite(ledPin, ledState);
        }
        if (ledStripState == LOW) {
          ledStripState = HIGH;
          Serial.println("Humidity is >= " + String(humidityThreshold) + ", turning LED strip on");
          digitalWrite(lights, ledStripState);
        }
        if (peltierState == LOW) {
          peltierState = HIGH;
          Serial.println("Humidity is >= " + String(humidityThreshold) + ", turning Peltier on");
          digitalWrite(peltier, peltierState);
        }
      }
      else {
        if (ledState == HIGH) {
          ledState = LOW;
          Serial.println("Humidity is < " + String(humidityThreshold) + ", turning small LED off");
          digitalWrite(ledPin, ledState);
        }
        if (ledStripState == HIGH) {
          ledStripState = LOW;
          Serial.println("Humidity is < " + String(humidityThreshold) + ", turning LED strip off");
          digitalWrite(lights, ledStripState);
        }
        if (peltierState == HIGH) {
          peltierState = LOW;
          Serial.println("Humidity is < " + String(humidityThreshold) + ", turning Peltier off");
          digitalWrite(peltier, peltierState);
        }
      }
    }

    void testprint() {
      unsigned long currentMillis = millis();

      if ((currentMillis - lastUpdate) >= (readInterval * 1000)) {
        Serial.print("Current millis() = "); Serial.println(currentMillis);
        Serial.print("Millis of last poll = "); Serial.println(lastUpdate);
        Serial.print("Temp *C = "); Serial.println(temp);
        Serial.print("Hum. % = "); Serial.println(humidity);
        Serial.println();
      }
    }

    void TestLight() {
      unsigned long currentMillis = millis();

      if ((currentMillis - lastUpdate) >= (readInterval * 1000)) {
        lastUpdate = millis();
        if (ledState == LOW) {
          ledState = HIGH;
          Serial.println("turning LED on");
        } else {
          ledState = LOW;
          Serial.println("turning LED off");
        }
    
        // set the LED with the ledState of the variable:
        digitalWrite(ledPin, ledState);
      }
    }
};

Tempsensor testsensor = Tempsensor(2); // initialize the sensor

void setup() {

  /*
    Set the pins which are attached to other devices to output to
    prevent a floating pin which can casues issues

  */
  pinMode(3, OUTPUT);
  pinMode(lights, OUTPUT);
  pinMode(peltier, OUTPUT);

  Serial.begin(9600);

  if (! testsensor.begin()) {   // Set to 0x45 for alternate i2c addr
    Serial.println("Couldn't find SHT31");
    while (1);
  }
  Serial.println("setup successful");
}


void loop() {

  testsensor.testprint();
  testsensor.Update();
//  testsensor.TestLight();
}
