const int currentPin = A0;
int sensitivity = 100;
int adcValue= 0;
int offsetVoltage = 2500;
double adcVoltage = 0;
double currentValue = 0;
float samples = 0.0;
float AvgAcs = 0.0;
float AcsValueF = 0.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop()
{
  adcValue = analogRead(currentPin);
  adcVoltage = (adcValue / 1024.0) * 5200;
  currentValue = ((adcVoltage - offsetVoltage) / sensitivity);
  
  samples = samples + adcValue;
  delay(5);

  AvgAcs = samples/150.0;
  AcsValueF = (2.5 - (AvgAcs*(5/1024)))/100;

  Serial.print("Raw Sensor Value = " );
  Serial.print(adcValue);

  Serial.print("\t Current = ");
  Serial.println(AcsValueF,3);

  

  delay(1500);
}