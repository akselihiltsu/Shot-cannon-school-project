#include <Servo.h>
int y1;
int y2;
int y3;
int p1;
int p2;
int p3;
int ypos = 90;
int ppos = 45;
int Ypos = 90;
int Ppos = 45;
int garbage;
int i = 0;
  Servo Yaw;
  Servo Pitch;
 

void setup() {
  Serial.begin(9600);
  pinMode(8,OUTPUT);
  pinMode(13,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(2,OUTPUT);
  Yaw.attach(3);
  Pitch.attach(5);
  Yaw.write(ypos);
  Pitch.write(ppos);
}

void loop() {
  
  if (Serial.available() >5) {
    digitalWrite(4, HIGH);
    p1 = Serial.read() - '0';
    p2 = Serial.read() - '0';
    p3 = Serial.read() - '0';
    y1 = Serial.read() - '0';
    y2 = Serial.read() - '0';
    y3 = Serial.read() - '0';
    i ++;
    ypos = (100*y1) + (10*y2) + y3;
    ppos = (100*p1)+ (10*p2) + p3;
    //Ypos = (60/630)*ypos+65;
    //Ppos = (-45/470)*ppos +75;
  }
    if (i == 347) {
      digitalWrite(13,HIGH);
    }
    if (i == 350) {
      digitalWrite(8,HIGH);
      delay(100);
      digitalWrite(0,LOW);
    }
    Yaw.write(ypos);
    Pitch.write(ppos);
}
  
