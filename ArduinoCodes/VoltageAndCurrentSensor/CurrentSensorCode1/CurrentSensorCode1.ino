#define sensorPin A0

void setup()
{
Serial.begin(9600);
}
void loop()

{

unsigned int x = 0;

float AcsValue = 0.0;

float Samples = 0.0; float AvgAcs = 0.0;

float AcsValueF = 0.0;

for (int x=0; x < 150; x++) //Get 150 sample
{

AvgAcs=Samples/150.0; //Taking Average of Samples 
AcsValueF = (2.5 -(AvgAcs* (5.0/1024.0)))/0.100;
Serial.println(AcsValueF);//Print the read current on Serial monitor 
 delay(1500);
 }
}