const int currentPin = A0; // Current Sensor

// Constants for resistor values in voltage divider (in ohms)
const float R1 = 30000.0;
const float R2 = 7500.0;

// Constant for reference voltage
const float refVoltage = 5.0;

void setup() {
  Serial.begin(9600);
  Serial.flush(); // clear screen on reuploading
  Serial.println("------CURRENT SENSOR DATA-------");
}

void loop() {
  // Current measurement
  float currentSum = 0;
  for (int i = 0; i < 25; i++) {
    float analogVoltage = (analogRead(currentPin) * refVoltage) / 1024.0;
    float current = (analogVoltage - (refVoltage / 2.0)) / 0.100;
    currentSum += current;
    delay(100);
  }
  float currentAvg = currentSum / 25.0;
  Serial.print("Average current: ");
  Serial.print(currentAvg + 0.0932, 2);

  delay(5000);
}
