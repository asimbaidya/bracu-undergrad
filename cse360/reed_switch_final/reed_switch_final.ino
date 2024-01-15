const int REED_PIN = 2;	// Pin connected to reed switch
const int LED_PIN = 13;	// LED pin

void setup() {
	Serial.begin(9600);
	pinMode(REED_PIN, INPUT_PULLUP);	// Enable internal pull-up for the reed switch
	pinMode(LED_PIN, OUTPUT);
}

void loop() {
	int proximity = digitalRead(REED_PIN); // Read the state of the switch
	
	// If the pin reads low, the switch is closed.
	if (proximity == LOW) {
		Serial.println("Switch closed");
		digitalWrite(LED_PIN, HIGH);	// Turn the LED on
	}
	else {
		Serial.println("Switch opened");
		digitalWrite(LED_PIN, LOW);		// Turn the LED off
	}
}