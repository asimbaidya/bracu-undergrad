// HC-SR505 Mini Infrared PIR Motion Sensor
int pir_pin = 9;  // Pin connected to the PIR sensor

// LED pin
const int led_pin = 13;

void setup() {
  pinMode(led_pin, OUTPUT);
  pinMode(pir_pin, INPUT);
  
  Serial.begin(9600);
}

void loop() {
  // Read the state of the PIR sensor
  int pirState = digitalRead(pir_pin);

  // If motion is detected, turn on the LED
  if (pirState == HIGH) {
    digitalWrite(led_pin, HIGH); // Turn on the LED
    Serial.println("Motion detected!");
  } else {
    digitalWrite(led_pin, LOW);  // Turn off the LED
    Serial.println("No motion detected.");
  }

  delay(100); // Adjust this delay as needed
}
