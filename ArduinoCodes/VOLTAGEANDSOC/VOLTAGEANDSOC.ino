// SOC-------------------------------------------

// #define VIO 2 // Just used for the HIGH reference voltage
// #define INT 3 // On 328 Arduinos, only pins 2 and 3 support interrupts
// #define POL 4 // Polarity signal
// #define GND 5 // Just used for the LOW reference voltage
// #define CLR 6 // Unneeded in this sketch, set to input (hi-Z)
// #define SHDN 7 // Unneeded in this sketch, set to input (hi-Z)

// #define LED 13 // Standard Arduino LED

// // Change the following two lines to match your battery
// // and its initial state-of-charge:

// volatile double battery_mAh = 2000.0; // milliamp-hours (mAh)
// volatile double battery_percent = 100.0;  // state-of-charge (percent)

// // Global variables ("volatile" means the interrupt can
// // change them behind the scenes):

// volatile boolean isrflag;
// volatile long int time, lasttime;
// volatile double mA;
// double ah_quanta = 0.17067759; // mAh for each INT
// double percent_quanta; // calculate below

// Current Sensor-----------------------------

// const int currentPin = A0;


// Voltage and Current-------------------------

// Define analog input

#define ANALOG_IN_PIN A1 // Volatge A0
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

// SOC
// Set up I/O pins:
  
//   pinMode(GND,OUTPUT); // Make this pin LOW for "ground"
//   digitalWrite(GND,LOW);

//   pinMode(VIO,OUTPUT); // Make this pin HIGH for logic reference
//   digitalWrite(VIO,HIGH);

//   pinMode(INT,INPUT); // Interrupt input pin (must be D2 or D3)

//   pinMode(POL,INPUT); // Polarity input pin

//   pinMode(CLR,INPUT); // Unneeded, disabled by setting to input
  
//   pinMode(SHDN,INPUT); // Unneeded, disabled by setting to input

//   pinMode(LED,OUTPUT); // Standard Arduino status LED
//   digitalWrite(LED,LOW);  

//   // Enable serial output:
//   Serial.println("LTC4150 Coulomb Counter BOB interrupt example");
//   // One INT is this many percent of battery capacity:
  
//   percent_quanta = 1.0/(battery_mAh/1000.0*5859.0/100.0);

//   // Enable active-low interrupts on D3 (INT1) to function myISR().
//   // On 328 Arduinos, you may also use D2 (INT0), change '1' to '0'. 

//   isrflag = false;
//   attachInterrupt(1,myISR,FALLING);
}

void loop() {
  // float currentSum = 0;
  // for(int i = 0; i < 25; i++) {
  //   float analogVoltage = (analogRead(currentPin) * 5.0) / 1024.0;
  //   float current = (analogVoltage - 2.5) / 0.100;
  //   currentSum += current;
  //   delay(100);
  // }
  // float currentAvg = currentSum / 25.0;
  // Serial.print("Average current: ");
  // Serial.println(currentAvg+0.0932);
  // delay(1000);




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


// Temperature -----------------------------------------------------

 //Read Raw ADC Data
  // int adcData = analogRead(sensorPin);
  // // Convert that ADC Data into voltage
  // float voltage = adcData * (5.0 / 1024.0);
  // // Convert the voltage into temperature 
  // float temperature = voltage * 100;
  // // Print the temperature data
  // Serial.print("Temperature: ");
  // Serial.print(temperature);
  // Serial.println("*C");
  // delay(1000); // wait a second between readings





// SOC-------------------------------------------------------------------

// static int n = 0;

//   // When we detect an INT signal, the myISR() function
//   // will automatically run. myISR() sets isrflag to TRUE
//   // so that we know that something happened.

//   if (isrflag)
//   {
//     // Reset the flag to false so we only do this once per INT
    
//     isrflag = false;

//     // Blink the LED

//     digitalWrite(LED,HIGH);
//     delay(100);
//     digitalWrite(LED,LOW);

//     // Print out current status (variables set by myISR())

//     Serial.print("mAh: ");
//     Serial.print(battery_mAh);
//     Serial.print(" soc: ");
//     Serial.print(battery_percent);
//     Serial.print("% time: ");
//     Serial.print((time-lasttime)/1000000.0);
//     Serial.print("s mA: ");
//     Serial.println(mA);
//   }

  // You can run your own code in the main loop()
  // myISR() will automatically update information
  // as it needs to, and set isrflag to let you know
  // that something has changed.

}

// SOC TEST----------------------------------------




// void myISR() // Run automatically for falling edge on D3 (INT1)
// {
//   static boolean polarity;
  
//   // Determine delay since last interrupt (for mA calculation)
//   // Note that first interrupt will be incorrect (no previous time!)

//   lasttime = time;
//   time = micros();

//   // Get polarity value 

//   polarity = digitalRead(POL);
//   if (polarity) // high = charging
//   {
//     battery_mAh += ah_quanta;
//     battery_percent += percent_quanta;
//   }
//   else // low = discharging
//   {
//     battery_mAh -= ah_quanta;
//     battery_percent -= percent_quanta;
//   }

//   // Calculate mA from time delay (optional)

//   mA = 614.4/((time-lasttime)/1000000.0);

//   // If charging, we'll set mA negative (optional)
  
//   if (polarity) mA = mA * -1.0;
  
//   // Set isrflag so main loop knows an interrupt occurred
  
//   isrflag = true;
// }





  