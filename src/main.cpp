#include <Arduino.h>

#define LED_PIN 2

unsigned long lastStateToggleTime = 0;
unsigned long lastSerialSendTime = 0;

// Make this variable non-const so we can change it dynamically
unsigned long toggleInterval = 1000; 
const unsigned long serialInterval = 100;

bool ledState = false;

void setup() {
    Serial.begin(115200);
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);
    Serial.println("--- ESP32 Command Listener Initialized ---");
    Serial.println("👉 Send '+' to blink faster, '-' to blink slower.");
}

void loop() {
    unsigned long currentMillis = millis();

    // 1. Check for incoming commands from the Raspberry Pi
    if (Serial.available() > 0) {
        char incomingChar = Serial.read();
        
        if (incomingChar == '+') {
            // Decrease the interval to blink faster (minimum limit 100ms)
            if (toggleInterval > 100) {
                toggleInterval -= 100;
            }
            Serial.print("⚡ SPEED INCREASED. New Interval: ");
            Serial.print(toggleInterval);
            Serial.println(" ms");
        } 
        else if (incomingChar == '-') {
            // Increase the interval to blink slower (maximum limit 3000ms)
            if (toggleInterval < 3000) {
                toggleInterval += 100;
            }
            Serial.print("🐢 SPEED DECREASED. New Interval: ");
            Serial.print(toggleInterval);
            Serial.println(" ms");
        }
    }

    // 2. Handle LED Toggle state
    if (currentMillis - lastStateToggleTime >= toggleInterval) {
        lastStateToggleTime = currentMillis;
        ledState = !ledState;
        digitalWrite(LED_PIN, ledState ? HIGH : LOW);
    }

    // 3. Handle Serial Broadcast state every 100ms
    if (currentMillis - lastSerialSendTime >= serialInterval) {
        lastSerialSendTime = currentMillis;
        Serial.print("LED_STATE: ");
        Serial.print(ledState ? "ON" : "OFF");
        Serial.print(" (Interval: ");
        Serial.print(toggleInterval);
        Serial.println("ms)");
    }
}