#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// set display
LiquidCrystal_I2C lcd(0x27,16,2); 


const int REED_PIN = 2;	// Pin connected to reed switch
const int LED_PIN = 13;	// LED pin
const int BUZZER_PIN = 3;
int led = 13;                                    // LED connected to pin 13
int sound = 3;                                // piezo buzzer connected to pin 3


void foo(int f,int d){
  tone(sound, f, 250);              // play a tone with 1000 Hz for 250 ms
  delay(d);                                  // wait for 2 seconds
}


void setup() {
  
	Serial.begin(9600);

  lcd.init();
  lcd.backlight();

	pinMode(REED_PIN, INPUT_PULLUP);	// Enable internal pull-up for the reed switch
	pinMode(LED_PIN, OUTPUT);

  pinMode(sound, OUTPUT);         // sets the buzzer alarm as output
}

void loop() {
	int proximity = digitalRead(REED_PIN); // Read the state of the switch
	
	// If the pin reads low, the switch is closed.
	if (proximity == LOW) {
    lcd.clear();
    lcd.setCursor(1,0);
    lcd.print("Switch closed");
    // delay(100);

		Serial.println("Switch closed");
		digitalWrite(LED_PIN, HIGH);	// Turn the LED on
    
    digitalWrite(BUZZER_PIN,LOW);


    foo(10,400);
	}
	else {
    lcd.clear();
    lcd.setCursor(1,1);
    lcd.print("Switch opened");
    // delay(100);

		Serial.println("Switch opened");
		digitalWrite(LED_PIN, LOW);		// Turn the LED off

    digitalWrite(BUZZER_PIN,HIGH);

    foo(1000,400);
    delay(1000);
	}
}
