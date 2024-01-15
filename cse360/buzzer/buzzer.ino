const int BUZZER = 3;
const int LED_ONE = 4;
const int LED_TWO = 5;

const int S = 1000;
const int M = S * 60;
const int delay_time = M * 25;
int count = 0;

void setup() {
  pinMode(LED_ONE, OUTPUT);
  pinMode(LED_TWO, OUTPUT);
  pinMode(BUZZER, OUTPUT);
}

void play(int f, int d) {
  tone(BUZZER, f, d);
}
void light_up() {
  digitalWrite(LED_ONE, HIGH);
  digitalWrite(LED_TWO, HIGH);
}
void light_down() {
  delay(S * 5);
  digitalWrite(LED_ONE, LOW);
  digitalWrite(LED_TWO, LOW);
}

void loop() {

  if (count == 0) {
    light_up();
    play(500, 400);
    light_down();
  } else {
    light_up();
    for (int i = 0; i < count; i++) {
      play(500, 400);
    }
    light_down();
  }
  count += 1;
  delay(delay_time);
}
