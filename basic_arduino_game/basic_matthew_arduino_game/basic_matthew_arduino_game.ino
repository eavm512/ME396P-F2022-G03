int BUTTON_PIN = 2;
int SWITCH_PIN = 3;
int DELAY_TIME = 250;

void setup() {
  // put your setup code here, to run once:
  pinMode(BUTTON_PIN, INPUT);
  pinMode(SWITCH_PIN, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(SWITCH_PIN) == HIGH){
    if (digitalRead(BUTTON_PIN) == HIGH){
      Serial.print('FIRE!');
      Serial.println();
      delay(DELAY_TIME);
    }
    else{
      Serial.print(analogRead(A0));
      Serial.println();
      delay(DELAY_TIME);
    }
  }
}
