int acs712_pin = A0;

// Define the voltage reference for the ADC (usually 5V)
float vref = 5.0;

// Define the sensitivity of the ACS712 sensor (usually 185mV/A for the 5A version)
float sensitivity = 0.100;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Read the raw analog value from the ACS712 sensor
  int raw_value = analogRead(acs712_pin);

  // Convert the raw value to a voltage
  float voltage = (raw_value / 1023.0) * vref;

  // Convert the voltage to a current using the sensitivity of the ACS712 sensor
  float current = (voltage - (vref / 2)) / sensitivity;

  // Print the current value to the serial monitor
  Serial.print("Current: ");
  Serial.print(current);
  Serial.println(" A");

  // Wait for 500 milliseconds before taking the next measurement
  delay(00);
}