/* Set the appropriate digital I/O pin connections. These are the pin */

const int lights = 4;   // pin for the lights
const int peltier = 5;  // PWM pin for the peltier
const int fan = 3;      // PWM pin for the fan


/**************************************************************************/
/*
    Setup code
*/
/**************************************************************************/

void setup() {

  /* set up the output pins */

  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);

  /* set up serial */
  Serial.begin(9600);

  while (!Serial)
    delay(10);     // will pause Zero, Leonardo, etc until serial console opens

  /* adjust timer 2 to give pin 3 and 11 25kHz output*/
  TCCR2A = 0x23;
  TCCR2B = 0x09;  // select timer2 clock
  OCR2A = 79;  // aiming for 25kHz
  pinMode(3, OUTPUT);
  OCR2B = 62;  // set the PWM duty cycle
}
  
/**************************************************************************/
/*
    Main loop code
*/
/**************************************************************************/

void loop() {

  //analogWrite(peltier,Output);

  /*Control fan speed*/
  //analogWrite(fan, 100);
  OCR2B = 0;
  analogWrite(peltier, 0);
  Serial.println("Fan off, peltier off");
  delay(30000);
  digitalWrite(peltier, HIGH);
  Serial.println("Fan off, peltier on");
  delay(30000);
  OCR2B = 79;
  analogWrite(peltier,0);
  Serial.println("Fan on, peltier off");
  delay(30000);
  digitalWrite(peltier,HIGH);
  Serial.println("Fan on, peltier on");
  delay(30000);
}
