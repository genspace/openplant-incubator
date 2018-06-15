const int lights = 4;   // pin for the lights

void setup() {
  // put your setup code here, to run once:
  pinMode(lights, OUTPUT);
  pinMode(5, OUTPUT);
  Serial.begin(9600);
  
  while (!Serial)
    delay(10);     // will pause Zero, Leonardo, etc until serial console opens

  Serial.println("LED testing begins now");

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(5, LOW);
  Serial.println("lights ON");
  digitalWrite(lights, HIGH); //for testing purposes
  delay(5000);
  digitalWrite(lights, LOW);
  Serial.println("lights off");
  delay(5000);
}
