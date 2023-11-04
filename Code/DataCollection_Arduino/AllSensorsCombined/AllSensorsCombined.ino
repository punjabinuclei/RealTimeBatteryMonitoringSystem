const int currentPin = A0; // Current Sensor
const int voltagePin = A1; // Voltage Sensor
const int tempPin = A2; // Temperature Sensor
 
// Constants for resistor values in voltage divider (in ohms)
const float R1 = 30000.0;
const float R2 = 7500.0; 
 
// Constant for reference voltage
const float refVoltage = 5.0;

void setup() {
  Serial.begin(9600);
  Serial.flush(); // clear screen on reuploading
  Serial.println("------BATTERY SENSOR DATA-------");
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
  
  // Voltage measurement
  int adcValue = analogRead(voltagePin);
  float adcVoltage = (adcValue * refVoltage) / 1024.0; 
  float inVoltage = adcVoltage / (R2 / (R1 + R2));
  inVoltage += 0.27;
  float SOC = (inVoltage - 8.0) / 3.1 * 100.0;

  // Temperature measurement
  int adcData = analogRead(tempPin);
  float voltage = adcData * (refVoltage / 1024.0);
  float temperature = voltage * 100.0;



  Serial.print("Average current: ");
  Serial.print(currentAvg + 0.0932, 2);
  Serial.print(" Voltage: ");
  Serial.print(inVoltage, 2);
  Serial.print(" State of Charge: ");
  Serial.print(SOC, 2);
  Serial.print(" Temperature: ");
  Serial.print(temperature, 2);
  Serial.println("*C");



  delay(5000);
}
