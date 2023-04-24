import time
import board
import busio
import csv
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
ads.gain = 2/3

# create single-ended input channels
chan_voltage = AnalogIn(ads, ADS.P0)
chan_current = AnalogIn(ads, ADS.P1)
chan_lm35 = AnalogIn(ads, ADS.P2)

# Set up LM35 calibration parameters
TEMP_SAMPLES = 25  # Number of samples to average for temperature calculation
LM35_SENSITIVITY = 0.01 # Sensitivity of the LM35 (10mV/°C)


# Set up ACS712 calibration parameters
REF_VOLTAGE = 5.0  # Supply voltage of the ADC
SENSITIVITY = 0.100  # Sensitivity of the ACS712 (mV/A)
ZERO_CURRENT_VOLTAGE = 2.5  # Voltage read when there is no current flow
CURRENT_SAMPLES = 25  # Number of samples to average for current calculation
R1 = 30000
R2 = 7500

# Create CSV file and write headers
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Voltage', 'Current', 'Temperature', 'SOC'])

# Main loop to read sensor data
while True:
    # Read the voltage value
    voltage = chan_voltage.voltage
    voltage = (voltage) / 0.2
    voltage += 0.27
    # SOC
    SOC=0
    SOC = (voltage - 8.0) / 3.1 * 100.0;
    # Read the current value
    current_sum = 0
    for i in range(CURRENT_SAMPLES):
        adc_value = chan_current.value
        analog_voltage = (adc_value / 32767.0) * REF_VOLTAGE
        current = (analog_voltage - (REF_VOLTAGE / 2.0)) / SENSITIVITY
        current_sum += current
        time.sleep(0.1)
    current_avg = current_sum / CURRENT_SAMPLES
    current_avg += 3.56



     # Read the LM35 temperature value
    temp_sum = 0
    for i in range(TEMP_SAMPLES):
        voltage_lm35 = chan_lm35.voltage
        temp = (voltage_lm35 / LM35_SENSITIVITY)
        temp_sum += temp
        time.sleep(0.1)
    temp_avg = temp_sum / TEMP_SAMPLES
    temp_avg+=10
    
    
      
    # Print the values
    print("Voltage: %.2f V" % voltage)
    print("Current: %.2f A" % current_avg)
    print("Temperature: %.2f C" % temp_avg)
    print("SOC: %.2f percent" % SOC)
    
    
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([voltage, current_avg, temp, SOC])

    # Wait for 1 second
    time.sleep(1)
