const int ldrPin = A0;  // LDR connected to analog pin A0

void setup() {
  Serial.begin(9600);   // Initialize serial communication
}

void loop() {
  int ldrValue = analogRead(ldrPin);  // Read analog value from LDR
  if(ldrValue > 50){
    digitalWrite(12,HIGH);
    delay(100);
  }else{
    digitalWrite(12,LOW);
  }
  Serial.print("LDR Value: ");
  Serial.println(ldrValue);           // Print LDR value to the serial monitor
  
  delay(100);  // Delay for 1 second
}