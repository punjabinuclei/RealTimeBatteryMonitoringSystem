// Code to test the functionality of the GY712/ACS712 sensor board.
//
// Marco Colli, June 2016.
//
// The board is an implementation of the ACS712 hall effect current sensor and
// is commonly available from many generic sources.
// 
// The sensor consists of a linear Hall circuit with a copper conduction 
// path located near the surface of the chip. Applied current flowing through 
// the copper conduction path generates a magnetic field which the sensor  
// converts into a linearly proportional voltage +/- 2.5V around a central 2.5V.
//
// This voltage is read through the Arduino ADC as a 10 bit number, from 
// which the DC or AC current can be calculated. All calculations in these 
// examples are done in integer maths.
//

const uint8_t SENSOR_PIN = A0;

const uint8_t SENS = 100;   // sensor sensitivity from datasheet in mV/A. 5A sensor=185, 20A=100, 30A=66
int16_t sensorZeroAdj = 0;  // calculate in setup()

#define SENSE_DC  0   // sense DC or AC - changes how the current is calculated

void setup() 
{
  Serial.begin(9600);
  
  pinMode(SENSOR_PIN, INPUT);

  // Read the analog input a few times to makes sure that we get
  // a good zero adjustment from nominal center value. There should be no
  // current flowing while this is happening.
  for (uint8_t i=1; i<=10; i++)
  {
    uint16_t error = 512 - analogRead(SENSOR_PIN);
    sensorZeroAdj = ((sensorZeroAdj * (i-1)) + error)/i;
  }
  Serial.print("Acquired zero adjust @");
  Serial.println(sensorZeroAdj);
}

int32_t readVcc()
// Calculate current Vcc in mV from the 1.1V reference voltage
{
  int32_t result = 5000L;

  // Read 1.1V reference against AVcc - hardware dependent
  // Set the reference to Vcc and the measurement to the internal 1.1V reference
#if defined(__AVR_ATmega32U4__) || defined(__AVR_ATmega1280__) || defined(__AVR_ATmega2560__)
  ADMUX = _BV(REFS0) | _BV(MUX4) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1);
#elif defined (__AVR_ATtiny24__) || defined(__AVR_ATtiny44__) || defined(__AVR_ATtiny84__)
  ADMUX = _BV(MUX5) | _BV(MUX0);
#elif defined (__AVR_ATtiny25__) || defined(__AVR_ATtiny45__) || defined(__AVR_ATtiny85__)
  ADMUX = _BV(MUX3) | _BV(MUX2);
#else
  ADMUX = _BV(REFS0) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1);
#endif  
  
#if defined(__AVR__)
  delay(2);         // Wait for Vref to settle
  ADCSRA |= _BV(ADSC);    // Convert, result is stored in ADC at end
  while (bit_is_set(ADCSRA,ADSC)); // measuring
  result = ADCL; // must read ADCL (low byte) first - it then locks ADCH 
  result |= ADCH<<8; // // unlocks both

  result = 1125300L / result; // Back-calculate AVcc in mV; 1125300 = 1.1*1023*1000
#endif
  
  return(result);
}

#if SENSE_DC

int32_t senseCurrent(void)
// Sense the DC current
{
  // read the value from the sensor:
  int32_t sensorValue = analogRead(SENSOR_PIN) + sensorZeroAdj;
  int32_t Vcc = readVcc();
  
  int32_t convertedmA = (1000L * (((Vcc*sensorValue)/1024L)-(Vcc/2)))/SENS;

  Serial.print(sensorValue);
  Serial.print(" @Vcc ");
  Serial.print(Vcc);
  Serial.print (" mV: ");

  return(convertedmA);
}

#else // SENSE_DC

const uint8_t AC_FREQUENCY = 50;  // in Hz

int32_t senseCurrent(void)
// Sense the AC RMS current
// We get a sinusoidal signal so need to detect when the signal stops changing
// over a period that would encompass 1 or 2 waveforms.
{
  const uint8_t timeSampling = 2 * (1000 / AC_FREQUENCY);
  
  int32_t convertedmA;
  uint16_t sampleMin = 1024, sampleMax = 0;
  int32_t Vpp, Vcc = readVcc();   // both in milliVolts

  // Collect samples over the time sampling period and 
  // work out the min/max readings for the waveform
  for (uint32_t timeStart = millis(); millis() - timeStart < timeSampling; )
  {
    int16_t sensorValue = analogRead(SENSOR_PIN) + sensorZeroAdj;
    
    if (sensorValue > sampleMax) sampleMax = sensorValue;
    if (sensorValue < sampleMin) sampleMin = sensorValue;
  }

  // now calculate the current
  Vpp = (((sampleMax-sampleMin)/2)*Vcc)/1024L;
  convertedmA = (707L * Vpp)/SENS;  // 1/sqrt(2) = 0.7071 = 707.1/1000

  Serial.print("(");
  Serial.print(sampleMin);
  Serial.print(",");
  Serial.print(sampleMax);
  Serial.print(") @Vcc ");
  Serial.print(Vcc);
  Serial.print (" mV: ");

  return(convertedmA);
}

#endif // SENSE_DC

void loop() 
{
  Serial.print(senseCurrent());
  Serial.println(" mA");
  delay(1500);
}