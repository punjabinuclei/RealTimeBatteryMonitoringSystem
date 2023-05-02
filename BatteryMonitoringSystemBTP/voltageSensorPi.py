import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# create the i2c bus
i2c=busio.I2C(board.SCL, board.SDA)

# Create the ADC object using I2c bus
ads=ADS.ADS1115(i2c)
ads.gain=2/3

# create single ended input channl 0
chan=AnalogIn(ads,ADS.P0)

print("{:>5}\t{:>5}".format('raw', 'v'))

R1=30000
R2=7500

voltageOutput=(chan.voltage)/0.2
voltageOutput+=0.27

while True:
     voltageOutput = (chan.voltage / 0.2) + 0.27
     print("{:>5}\t{:>5.2f}".format(chan.value, voltageOutput))
     time.sleep(3)
    