int echo_pin = 11;
int trig_pin = 10;
int ping_travel_time;


// 
const int button_pin = 12;  // the number of the pushbutton pin
const int led_pin = 13;     // the number of the LED pin


void setup() {
  //  WTF is this?
  Serial.begin(9600);
  
  pinMode(led_pin, OUTPUT);

  pinMode(trig_pin,OUTPUT);
  pinMode(echo_pin,INPUT);
}

void loop() {
  // Trigger the sensor to measure distance
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);

  // Measure the time taken for the ultrasonic pulse to return
  ping_travel_time = pulseIn(echo_pin, HIGH);

  // Calculate distance in centimeters (speed of sound is 343 m/s)
  float distance_cm = (ping_travel_time * 0.0343) / 2;

  Serial.print("Distance: ");
  Serial.print(distance_cm);
  Serial.println(" cm");

  // If an object is detected within a certain range, turn on the LED
  if (distance_cm > 0 && distance_cm < 50) {
    digitalWrite(led_pin, HIGH); // Turn on the LED
  } else {
    digitalWrite(led_pin, LOW);  // Turn off the LED
  }

  delay(500); // Delay for a short interval before taking the next reading
}

