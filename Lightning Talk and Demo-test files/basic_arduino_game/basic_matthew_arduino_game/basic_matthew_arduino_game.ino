int BUTTON_PIN = 2;
int SWITCH_PIN = 3;
int DELAY_TIME = 200;
int angle = 10;
bool prior_switch = digitalRead(SWITCH_PIN);

void setup() {
  // put your setup code here, to run once:
  pinMode(BUTTON_PIN, INPUT);
  pinMode(SWITCH_PIN, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(SWITCH_PIN) != prior_switch ){
    Serial.print("Toggle mode");
    Serial.println();
    prior_switch = digitalRead(SWITCH_PIN);
    }
    
  if (digitalRead(BUTTON_PIN) == HIGH){
    Serial.print("FIRE!");
    Serial.println();
    delay(DELAY_TIME);
  }
  else{
    angle = analogRead(A0);
    Serial.print(map(angle, 0, 1023, 0, 359));
    Serial.println();
    delay(DELAY_TIME);
  }
}
