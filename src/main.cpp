#include <Arduino.h>

// Pin 2 is the built-in blue LED on almost all ESP32 NodeMCU boards
#define LED_PIN 2 

void setup() {
    // Open serial communications at 115200 baud rate
    Serial.begin(115200);
    pinMode(LED_PIN, OUTPUT);
    Serial.println("--- ESP32 Blink Test Initialized ---");
}

void loop() {
    digitalWrite(LED_PIN, HIGH);   // Turn the LED on
    Serial.println("LED: ON");
    delay(100);                   // Wait half a second
    
    digitalWrite(LED_PIN, LOW);    // Turn the LED off
    Serial.println("LED: OFF");
    delay(100);                   // Wait half a second
}