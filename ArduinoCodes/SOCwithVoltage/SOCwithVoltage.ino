#define ANALOG_IN_PIN A0 // Volatge A0
// #define sensorPin A0 // LM35 is connected to this PIN
 
// Floats for ADC voltage & Input voltage
float adc_voltage = 0.0;
float in_voltage = 0.0;
 
// Floats for resistor values in divider (in ohms)
float R1 = 30000.0;
float R2 = 7500.0; 
 
// Float for Reference Voltage
float ref_voltage = 5.0;
 
// Integer for ADC value
int adc_value = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("DC Voltage Test");
   Serial.println("Temp");
}

void loop() {



  adc_value = analogRead(ANALOG_IN_PIN);
   
   // Determine voltage at ADC input
   adc_voltage  = (adc_value * ref_voltage) / 1024.0; 
   
   // Calculate voltage at divider input
   in_voltage = adc_voltage / (R2/(R1+R2)) ; 
   in_voltage+=0.27;

  float SOC=0.0;
  SOC=(in_voltage-8)/(3.1);
  SOC=SOC*100;

  // Voltage
  Serial.print("voltage = ");
  Serial.println(in_voltage, 2);

   // Print results to Serial Monitor to 2 decimal places
  // Serial.print("SOC = ");
  // Serial.println(SOC, 2);
  // Short delay
  delay(3000);


}



  