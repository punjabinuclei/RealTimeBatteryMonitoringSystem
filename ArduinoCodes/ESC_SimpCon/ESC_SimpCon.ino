#include<servo.h>
Servo esc;
void setup() {
  esc.attach(A0);
  esc.writeMicroseconds(1000);
  pinMode(A0,INPUT);
  serial.begin(9600);
}

void loop() {
 int val;
 val= digitalRead(11);
 if(digitalRead(11) == HIGH)
 {
  esc.writeMicroseconds(2000);
 }
 else
 {
  esc.writeMicroseconds(1000);
 }
}
