
const int button_pin = 12;  // the number of the pushbutton pin
const int led_pin = 13;     // the number of the LED pin

// Variables will change:
int led_state = 0;

int button_old = 1;
int button_new;
int delay_time = 100;



void setup() {
  //  WTF is this?
  Serial.begin(9600);

  pinMode(button_pin, INPUT);
  pinMode(led_pin, OUTPUT);
}

void loop() {
  button_new = digitalRead(button_pin);
  
  if (button_new == 0) {
    Serial.println("Pressed");
    if (led_state == 0) {
      Serial.println("ON");
      digitalWrite(led_pin, HIGH);
      led_state = 1;
    } else {
      Serial.println("OFF");
      digitalWrite(led_pin, LOW);
      led_state = 0;
    }
  }
  Serial.println(button_new);
  delay(delay_time);
}
