const int voltagePin = A1; // Voltage Sensor

// Constants for resistor values in voltage divider (in ohms)
const float R1 = 30000.0;
const float R2 = 7500.0;

// Constant for reference voltage
const float refVoltage = 5.0;

void setup() {
  Serial.begin(9600);
  Serial.flush(); // clear screen on reuploading
  Serial.println("------VOLTAGE SENSOR DATA-------");
}

void loop() {
  // Voltage measurement
  int adcValue = analogRead(voltagePin);
  float adcVoltage = (adcValue * refVoltage) / 1024.0; 
  float inVoltage = adcVoltage / (R2 / (R1 + R2));
  inVoltage += 0.27;
  Serial.print("Voltage: ");
  Serial.print(inVoltage, 2);

  delay(5000);
}