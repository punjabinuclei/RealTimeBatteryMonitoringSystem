import Adafruit_ADS1x15
import time

# Initialize ADC1115
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 2/3

# Set up voltage sensor calibration parameters
VREF = 5.0  # Supply voltage of the ADC
VOLTAGE_DIVIDER_RATIO = 5  # Voltage divider ratio of the voltage sensor module

# Main loop to read sensor data
while True:
    # Read the raw ADC value
    adc_value = adc.read_adc(1, gain=GAIN)

    # Convert ADC value to voltage
    voltage = (adc_value / 32767.0) * VREF * VOLTAGE_DIVIDER_RATIO

    # Print the voltage value
    print("Voltage: %.2f V" % voltage)

    # Wait for 1 second
    time.sleep(1)
