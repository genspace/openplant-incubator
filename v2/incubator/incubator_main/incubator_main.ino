/***************************************************
  This is the main file to control the incubator. Rewritten from Danny's prototype_incubator.ino

  Designed specifically to work with the SHT31-D sensor from Adafruit
  ----> https://www.adafruit.com/products/2857

  Wired the SHT31-D to the Arduino following the first diagram here:
  http://cactus.io/hookups/sensors/temperature-humidity/sht31/hookup-arduino-to-sensirion-sht31-temp-humidity-sensor

  Connect the LED strip to the MOSFET transistor following the diagram in the Cloud-based Lab Monitor google doc:
  Power Supply - to breadboard minus rail
  Power Supply + to LED strip red wire
  LED strip black wire to gate middle pin
 ****************************************************/

#include "Adafruit_SHT31.h"

// User input constants
const int desiredTemp = 22.0;

const int fan = 3;  // we just run the fans constantly with no input or output, as Danny did
const int lights = 4;
const int peltier = 5;

int ledState = LOW;
int peltierState = LOW;

Adafruit_SHT31 sht31 = Adafruit_SHT31(); // name the temp sensor

void setup() {

  /*
    Set the pins which are attached to other devices to output to
    prevent a floating pin which can casues issues

  */
  pinMode(fan, OUTPUT);
  pinMode(lights, OUTPUT);
  pinMode(peltier, OUTPUT);

  Serial.begin(9600);
  
  /* set up temp sensor */
  if (! sht31.begin(0x44)) {   // Set to 0x45 for alternate i2c addr
    Serial.println("Couldn't find SHT31");
    while (1) delay(1);
  }
  
  Serial.println("setup successful");
}

unsigned long getCurrentTime() {
  // TODO replace this with getting the time from the real time clock
  return millis();
}

void printCurrentData(unsigned long currentTime, float currentTemp, float currentHum) {
  Serial.print("Current Time = "); 
  Serial.println(currentTime);
  
  Serial.print("Temp *C = "); 
  Serial.println(currentTemp);

  Serial.print("Hum. % = "); 
  Serial.println(currentHum);
}

void recordCurrentData(unsigned long currentTime, float currentTemp, float currentHum) {
  // TODO connect to raspberry pi and save the data somewhere in the cloud
}

const int TEMP_TOL = 1.5;
void adjustPeltier(float currentTemp) {
  // TODO replace with a smarter algorithm, use PID like Danny
  if (currentTemp > desiredTemp + TEMP_TOL && peltierState == LOW) {
    peltierState = HIGH;
    Serial.println("Current temperature " + String(currentTemp) + " is higher than desired temperature " + String(desiredTemp) + ", turning Peltier cooler on");
    digitalWrite(peltier, peltierState);
  }
  else if (currentTemp < desiredTemp && peltierState == HIGH) {
    peltierState = LOW;
    Serial.println("Current temperature " + String(currentTemp) + " is lower than desired temperature " + String(desiredTemp) + ", turning Peltier cooler off");
    digitalWrite(peltier, peltierState);
  }
}

const int EIGHT_HOURS = 1000*60*60*8;
const int SIXTEEN_HOURS = 1000*60*60*16;
unsigned long lightToggleTime = -EIGHT_HOURS;
void adjustLight() {
  // TODO change this to use the real time clock
  if (ledState == LOW && (millis()-lightToggleTime) > EIGHT_HOURS) {
    ledState = HIGH;
    digitalWrite(lights, ledState);
    Serial.println("LED has been off for > 8 hours, turning LED on");
  } else if (ledState == HIGH && (millis()-lightToggleTime) > SIXTEEN_HOURS) {
    ledState = LOW;
    digitalWrite(lights, ledState);
    Serial.println("LED has been on for > 16 hours, turning LED off");
  }
}

void loop() {
  unsigned long currentTime = getCurrentTime();
  float currentTemp = sht31.readTemperature();
  float currentHum = sht31.readHumidity();
  printCurrentData(currentTime, currentTemp, currentHum);
  recordCurrentData(currentTime, currentTemp, currentHum);

  adjustPeltier(currentTemp);
  adjustLight();

  delay(2000);
}
