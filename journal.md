# This is my journal
1. What did we do
2. What did I learn
3. What questions do I have

18 Feb 2020
1. Today we learned how to code for Arduino. We assembled virtual wires, resistors, LED lights, 9v Battery, Breadboard and a Arduino. We hooked up the wires, resistors, lights, breadboard and battery to see how the circuit would work first. And then, we took out the battery and replaced it with a Arduino which we coded it to do what we wanted it to do. In particular we programmed it in what order to turn on and off the LED lights. I personally programmed my Arduino to turn the light bulbs on from left to right, and turn them off from right to left.

```.py
void setup()
{
  pinMode(13, OUTPUT); //TL
  pinMode(12, OUTPUT); //TM
  pinMode(11, OUTPUT); //TR
  pinMode(10, OUTPUT); //BL
  pinMode(9, OUTPUT); //BM
  pinMode(8, OUTPUT); //BR
}

void loop()
{
  digitalWrite(13, HIGH);
  delay(500); // Wait for 1000 millisecond(s)
  
  digitalWrite(12, HIGH);
  delay(500); // Wait for 1000 millisecond(s)

  digitalWrite(11, HIGH);
  delay(500); // Wait for 1000 millisecond(s)

  digitalWrite(10, HIGH);
  delay(500); // Wait for 1000 millisecond(s)

  digitalWrite(9, HIGH);
  delay(500); // Wait for 1000 millisecond(s)
  
  digitalWrite(8, HIGH);
  delay(500); // Wait for 1000 millisecond(s)

  
  digitalWrite(8, LOW);
  delay(500); // Wait for 1000 millisecond(s)
  
  digitalWrite(9, LOW);
  delay(500); // Wait for 1000 millisecond(s)
  
  digitalWrite(10, LOW);
  delay(500); // Wait for 1000 millisecond(s)
  
  digitalWrite(11, LOW);
  delay(500); // Wait for 1000 millisecond(s)
 
  digitalWrite(12, LOW);
  delay(500); // Wait for 1000 millisecond(s)
  
  digitalWrite(13, LOW);
  delay(500); // Wait for 1000 millisecond(s)

}
```

2. Today we learned how to use the commands and coding format that we have already learned on a virtual Arduino. Instead of coding, appearances which we usually do, we learned how to code a realistic virtual Arduino board so that next time we can work with a real Arduino board and programme it to turn the lights on and off when we want it to.

3. How different is a Arduino virtual board to a physical real life board?
