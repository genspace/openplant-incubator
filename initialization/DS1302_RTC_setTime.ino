#include <Time.h>
#include <DS1302.h>

DS1302 rtc(9,8,7);

void setup() {
  Serial.begin(9600);

  while (!Serial)
    delay(10);     // will pause Zero, Leonardo, etc until serial console opens

  rtc.halt(false);
  rtc.writeProtect(false);
    
  rtc.setDOW(TUESDAY);         
  rtc.setTime(2, 36, 10);
  rtc.setDate(8, 5, 2018);    
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(rtc.getTimeStr());
  
  String chardate = rtc.getDateStr(FORMAT_LONG, FORMAT_LITTLEENDIAN, '-');
  char output[10];
  chardate.toCharArray(output, 10);
  Serial.println(chardate);
    
  delay(5000);
}
