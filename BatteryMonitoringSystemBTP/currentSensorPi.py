import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
ads.gain = 2/3

# create single-ended input channel 0
chan = AnalogIn(ads, ADS.P1)

# Set up ACS712 calibration parameters
REF_VOLTAGE = 5.0  # Supply voltage of the ADC
SENSITIVITY = 0.100  # Sensitivity of the ACS712 (mV/A)
ZERO_CURRENT_VOLTAGE = 2.5  # Voltage read when there is no current flow
CURRENT_PIN = 0  # Analog input pin for ACS712
CURRENT_SAMPLES = 25  # Number of samples to average for current calculation

# Main loop to read sensor data
while True:
    # Read the raw ADC value
    adc_value = chan.value
    # print(adc_value)
    # Convert ADC value to voltage
    # voltage = (adc_value / 32767.0) * REF_VOLTAGE

    # Convert voltage to current using ACS712 calibration
    current_sum = 0
    for i in range(CURRENT_SAMPLES):
        analog_voltage = (adc_value / 32767.0) * REF_VOLTAGE
        current = (analog_voltage - (REF_VOLTAGE / 2.0)) / SENSITIVITY
        current_sum += current
        time.sleep(0.01)
    current_avg = current_sum / CURRENT_SAMPLES
    current_avg+=3.84

    # Print the current value
    print("Current: %.2f A" % current_avg)

    # Wait for 1 second
    time.sleep(0.1)
