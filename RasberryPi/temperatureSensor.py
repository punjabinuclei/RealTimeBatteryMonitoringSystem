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

# create single-ended input channel 0
chan_voltage = AnalogIn(ads, ADS.P0)
chan_lm35 = AnalogIn(ads, ADS.P2)

# Set up LM35 calibration parameters
TEMP_SAMPLES = 25  # Number of samples to average for temperature calculation
LM35_SENSITIVITY = 0.01 # Sensitivity of the LM35 (10mV/°C)

# Create CSV file and write headers

# Main loop to read sensor data
while True:
    # Read the voltage value
    voltage = chan_voltage.voltage
    voltage = (voltage / 0.2) + 0.27
    
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
    # print("Voltage: %.2f V" % voltage)
    print("Temperature: %.2f °C" % temp_avg)
    
    # Wait for 1 second
    time.sleep(1)
