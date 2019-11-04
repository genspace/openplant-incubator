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
#include "RTClib.h"           // library for the RTC

const float peltier_on_threshold = 25.0;
const float peltier_off_threshold = 24.0;

const int fan = 3;  // we just run the fans constantly with no input or output, as Danny did
const int lights = 4;
const int peltier = 5;

int peltierState = LOW;

Adafruit_SHT31 sht31 = Adafruit_SHT31();  // name the temp sensor
RTC_PCF8523 rtc;                          // name the clock

void setup() {
  /*
    Set the pins which are attached to other devices to output to
    prevent a floating pin which can cause issues

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

DateTime getCurrentTime() {
  return rtc.now();
}

void printCurrentData(DateTime currentTime, float currentTemp, float currentHum) {
  Serial.print("The clock is set to: "); 
  Serial.print(currentTime.hour()); 
  Serial.print(':'); 
  Serial.print(currentTime.minute()); 
  Serial.print(':'); 
  Serial.print(currentTime.second());
  Serial.print(" on "); 
  Serial.print(currentTime.year(), DEC); 
  Serial.print('/'); 
  Serial.print(currentTime.month(), DEC); 
  Serial.print('/'); 
  Serial.println(currentTime.day(), DEC);
  
  Serial.print("Temp *C = "); 
  Serial.println(currentTemp);

  Serial.print("Hum. % = "); 
  Serial.println(currentHum);
}

void recordCurrentData(DateTime currentTime, float currentTemp, float currentHum) {
  // TODO connect to raspberry pi and save the data somewhere in the cloud
}

void adjustPeltier(float currentTemp) {
  // TODO(low priority) replace with a smarter algorithm, use PID like Danny
  if (currentTemp > peltier_on_threshold) {
    peltierState = HIGH;
    Serial.println("Current temperature " + String(currentTemp) + " is higher than " + String(peltier_on_threshold) + ", turning Peltier cooler on");
    digitalWrite(peltier, peltierState);
  }
  else if (currentTemp < peltier_off_threshold) {
    peltierState = LOW;
    Serial.println("Current temperature " + String(currentTemp) + " is lower than " + String(peltier_off_threshold) + ", turning Peltier cooler off");
    digitalWrite(peltier, peltierState);
  }
  if (peltierState == HIGH) {
    Serial.println("Peltier is on");
  } else if (peltierState == LOW) {
    Serial.println("Peltier is off");
  }
}

void adjustLight(DateTime currentTime) {
  int hour = currentTime.hour();
  if (hour >= 4 && hour < 12) {
    digitalWrite(lights, LOW);
    Serial.println("Time is between 4am-12pm - lights are off");
  }
  else {
    digitalWrite(lights, HIGH);
    Serial.println("Time is between 12pm-4am - lights are on");
  }
}

void loop() {
  DateTime currentTime = getCurrentTime();
  float currentTemp = sht31.readTemperature();
  float currentHum = sht31.readHumidity();
  printCurrentData(currentTime, currentTemp, currentHum);
  recordCurrentData(currentTime, currentTemp, currentHum);

  adjustPeltier(currentTemp);
  adjustLight(currentTime);

  delay(5000);
}
