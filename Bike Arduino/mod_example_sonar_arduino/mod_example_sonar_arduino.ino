// ---------------------------------------------------------------- //
// Arduino Ultrasoninc Sensor HC-SR04
// Re-writed by Arbi Abdul Jabbaar
// Using Arduino IDE 1.8.7
// Using HC-SR04 Module
// Tested on 17 September 2019
// ---------------------------------------------------------------- //

#define echoPin 3 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 2 //attach pin D3 Arduino to pin Trig of HC-SR04
#define LED1Pin 53
#define LED2Pin 51

//GND to GND
//5V to 5V

// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement
int CUTOFF_ONE = 30;
int CUTOFF_TWO = 10;

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  pinMode(LED1Pin, OUTPUT);
  pinMode(LED2Pin, OUTPUT);
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed

}
void loop() {
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor

  if(distance < CUTOFF_ONE){
    digitalWrite(LED1Pin, HIGH);
  }
  else {
    digitalWrite(LED1Pin, LOW);
  }

  if(distance < CUTOFF_TWO){
    digitalWrite(LED2Pin, HIGH);
  }
  else{
    digitalWrite(LED2Pin, LOW);
  }

  
  //Print the distance 
  Serial.println(distance);
}
