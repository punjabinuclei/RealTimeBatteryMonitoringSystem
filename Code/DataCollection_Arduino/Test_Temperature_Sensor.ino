const int tempPin = A2; // Temperature Sensor

// Constant for reference voltage
const float refVoltage = 5.0;

void setup() {
  Serial.begin(9600);
  Serial.flush(); // clear screen on reuploading
  Serial.println("------TEMPERATURE SENSOR DATA-------");
}

void loop() {
  // Temperature measurement
  int adcData = analogRead(tempPin);
  float voltage = adcData * (refVoltage / 1024.0);
  float temperature = voltage * 100.0;
  Serial.print("Temperature: ");
  Serial.print(temperature, 2);
  Serial.println("*C");

  delay(5000);
}