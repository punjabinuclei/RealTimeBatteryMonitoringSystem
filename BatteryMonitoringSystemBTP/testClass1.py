import time
import board
import busio
import csv
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class SensorDataLogger:
    
    def __init__(self, filename):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
        self.ads.gain = 2/3

        self.chan_current = AnalogIn(self.ads, ADS.P0)        
        self.chan_voltage = AnalogIn(self.ads, ADS.P1)
        self.chan_lm35 = AnalogIn(self.ads, ADS.P2)
        
        self.TEMP_SAMPLES = 25
        self.LM35_SENSITIVITY = 0.01
        
        self.REF_VOLTAGE = 5.0
        self.SENSITIVITY = 0.100
        self.ZERO_CURRENT_VOLTAGE = 2.5
        self.CURRENT_SAMPLES = 25
        self.R1 = 30000
        self.R2 = 7500
        self.counter=0
        self.filename = filename
    
    def start(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Voltage', 'Current', 'Temperature', 'SOC'])
            
        while True:
            voltage = self.chan_voltage.voltage
            voltage = (voltage) / 0.2
            voltage -= 0.4
            SOC = (voltage - 9.0) / 2.3 * 100.0
            
            current_sum = 0
            for i in range(self.CURRENT_SAMPLES):
                adc_value = self.chan_current.value
                analog_voltage = (adc_value / 32767.0) * self.REF_VOLTAGE
                current = (analog_voltage - (self.REF_VOLTAGE / 2.0)) / self.SENSITIVITY
                current_sum += current
                time.sleep(0.01)
            current_avg = current_sum / self.CURRENT_SAMPLES
            current_avg += 3.46

            temp_sum = 0
            for i in range(self.TEMP_SAMPLES):
                voltage_lm35 = self.chan_lm35.voltage
                temp = (voltage_lm35 / self.LM35_SENSITIVITY)
                temp_sum += temp
                time.sleep(0.01)
            temp_avg = temp_sum / self.TEMP_SAMPLES
            temp_avg+=10

            print("Voltage: %.2f V" % voltage)
            print("Current: %.2f A" % current_avg)
            print("Temperature: %.2f C" % temp_avg)
            print("SOC: %.2f percent" % SOC)

            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([voltage, current_avg, temp_avg, SOC])
            
            time.sleep(0.1)


# logger = SensorDataLogger('dataSensor2.csv')
# logger.start()
