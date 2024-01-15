#include <SoftwareSerial.h>


// HC-06 configuration
int rx = 7;
int tx = 6;
SoftwareSerial mySerial(rx, tx); // RX, TX

// initial
void setup() {

  Serial.begin(9600);
  while (!Serial) {
  }
  Serial.println("Bluetooth Module Ready");
  mySerial.begin(9600);
}

void loop() {
  if (mySerial.available()) {
    // Read data until newline character ('\n') is encountered
    char buffer[64];  
    int bytesRead = mySerial.readBytesUntil('\n', buffer, sizeof(buffer) - 1); 
    buffer[bytesRead] = '\0';  // Null-terminate the received data

    // Print the received buffer
    Serial.print("Received: ");
    Serial.println(buffer);  // Print the buffer

    // Send the received buffer back to the app
    mySerial.print("You sent: ");
    mySerial.println(buffer);

    mySerial.println(5);
    mySerial.println("5");
  }
}
