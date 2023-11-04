# BMS CODE EXPLANATION

```python
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
```



> This code is a Python script that defines a class called "SensorDataLogger". The purpose of this script is to gather data from a battery monitoring system using a set of sensors connected to an analog-to-digital converter (ADC), which is in turn connected to a Raspberry Pi.
> 
> 
> The script initializes the ADC and the pins to which the sensors are connected, and sets the parameters for the different sensors. Then, the script enters a loop where it reads data from the sensors every 100 milliseconds. It calculates the voltage, current, temperature, and state of charge (SOC) of the battery using the readings from the sensors. The calculated data is then printed to the console and logged to a CSV file.
> 
> The data logger can be started by instantiating the "SensorDataLogger" class and calling the "start" method. The data logger will continue to run until it is manually stopped. This script serves as the first step in gathering data for analysis and training machine learning models for battery state prediction.
> 







```python
import pandas as pd # data processing
import numpy as np # working with arrays
import csv
# preprocessData------------------------------------------------------------------------------------
from sklearn import preprocessing 
from sklearn.preprocessing import MinMaxScaler

class CSVPreprocessor:
    def __init__(self, input_file):
        self.input_file = input_file
        
    def delete_data(self):
    # Open the file in write mode
        with open(self.input_file, 'w', newline='') as file:
            file.write('')    
            writer = csv.writer(file)
            writer.writerow(['Voltage', 'Current', 'Temperature', 'SOC'])
    def preprocess(self):
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(self.input_file)
        self.delete_data()
        
        df=df.abs()
        # Mean-------------------------
        def sliding_window_mean(values, window_size):
            result = np.zeros(len(values) - window_size + 1)
            for i in range(len(result)):
                result[i] = np.mean(values[i:i+window_size])
            return result

        for column_name in ["Voltage", "Current", "Temperature"]:
            column = df[column_name]
            print(column)
            window_size = 10
            mean_values = sliding_window_mean(column, window_size)

            padding = np.empty(len(df.index) - len(mean_values))
            padding[:] = np.nan
            mean_values = np.concatenate((mean_values, padding))

            df[f"{column_name}Mean"] = mean_values

        # Median----------------------------
        
        def sliding_window_stat(values, window_size, stat_func):
            result = np.zeros(len(values) - window_size + 1)
            for i in range(len(result)):
                result[i] = stat_func(values[i:i+window_size])
            padding = np.empty(len(df.index) - len(result))
            padding[:] = np.nan
            result = np.concatenate((result, padding))
            return result

        # Select columns of interest
        columns = ["Voltage", "Current", "Temperature"]
        stat_funcs = [np.median, np.median, np.median]
        prefixes = ["V", "I", "T"]

        # Compute sliding window statistics and save to new columns
        for i, column in enumerate(columns):
            stat_values = sliding_window_stat(df[column], window_size=10, stat_func=stat_funcs[i])
            new_column_name = prefixes[i] + "Median"
            df[new_column_name] = stat_values

        # STd---------------

        def sliding_window_stddev(values, window_size):
            return [np.std(values[i:i+window_size]) for i in range(len(values) - window_size + 1)]

        window_size = 10
        for col in ["Voltage", "Current", "Temperature"]:
            std_values = sliding_window_stddev(df[col], window_size)
            df[f"{col[0]}std"] = np.concatenate((std_values, np.full(len(df.index)-len(std_values), np.nan)))

        # Variance-----------------------

        # Define function to calculate sliding window variance
        def sliding_window_variance(values, window_size):
            return np.array([np.var(values[i:i+window_size]) for i in range(len(values) - window_size + 1)])

        # Loop over columns of interest
        for col in ["Voltage", "Current", "Temperature"]:
            # Calculate sliding window variance
            variance_values = sliding_window_variance(df[col], window_size=10)
            # Pad the variance_values array with NaNs to match the length of the DataFrame's index
            padding = np.full(len(df.index) - len(variance_values), np.nan)
            variance_values = np.concatenate((variance_values, padding))
            # Save the result to a new column in the DataFrame
            df[f"{col}Variance"] = variance_values

        
        # Calculate power, resistance, and conductance
        df["Power"] = df["Voltage"] * df["Current"] / 1000
        df["Resistance"] = df["Voltage"] / df["Current"] * 1000
        df["Conductance"] = 1 / df["Resistance"]
        # Calculate temperature difference
        df["temp_change"] = df["Temperature"].diff().fillna(0)

        # 
        # Replace inf values with NaN and remove rows containing NaN values
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)

        # Take absolute values of columns containing 'temp_change' in the name
        df[[col for col in df.columns if 'temp_change' in col]] = df[[col for col in df.columns if 'temp_change' in col]].abs()

        # Separate the target variable (SOC) from the features, apply min-max scaling to the features only, and combine with the target variable
        X = df.drop('SOC', axis=1)
        y = df['SOC']
        scaler = MinMaxScaler()
        X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
        df = pd.concat([X_scaled, y], axis=1)

        # Reorder the columns in the dataframe
        df = df[['Voltage', 'Current'] + [col for col in df.columns if col not in ['Voltage', 'Current']]]
        # df = df.drop('SOC', axis=1)
                
        # Write the preprocessed DataFrame to a new CSV file
        output_file = self.input_file.split('.')[0] + '_preprocessed.csv'
        df.to_csv(output_file, index=False)
        
        # Return the name of the output file
        return output_file

# Create an instance of the CSVPreprocessor class
# preprocessor = CSVPreprocessor('dataSensor.csv')

# # Call the preprocess method to preprocess the CSV file
# preprocessed_file = preprocessor.preprocess()

# # The preprocess method returns the name of the preprocessed file
# print('PreprocessedFileNew:', preprocessed_file)
```



> The code snippet provided utilizes various libraries to preprocess a CSV file containing sensor data. The script begins by defining a **`CSVPreprocessor`** class that takes an input file as an argument. The **`preprocess`** method of this class performs the actual data processing.
> 
> 
> The data processing involves various steps such as computing mean, median, standard deviation, and variance for selected columns of the input data. Additionally, the script also calculates power, resistance, and conductance from voltage and current data, and temperature difference between consecutive time points. The output DataFrame is normalized using the min-max scaling technique, and the resulting preprocessed data is saved to a new CSV file.
> 
> Overall, the script follows a clear and systematic approach to preprocess sensor data, making it ready for further analysis or modeling tasks.
> 

















```python
import pandas as pd
import numpy as np
import time
import pickle
        

class BatteryMonitor:
    def __init__(self, model_path):
        self.pickled_model = pickle.load(open(model_path, 'rb'))
        
    def predict_SOC(self, input_path):
        # Load input data
        df = pd.read_csv(input_path)

        # Store the SOC value in a separate variable
        real_SOC = df.iloc[2]['SOC']

        # Remove 'SOC' column from dataframe
        input_data = df.drop('SOC', axis=1)

        arr = input_data.iloc[2].values
        row_to_predict = arr.reshape(1, -1)

        # Create dataframe from input data with proper column names
        df = pd.DataFrame(row_to_predict, columns=self.pickled_model.feature_names_in_)

        # Get predicted SOC
        print(row_to_predict)
        predicted_SOC = self.pickled_model.predict(df)[0]

       # Save predicted and real SOC to CSV file with current date and time in the filename
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        filename = f"{now}.csv"
        df_result = pd.DataFrame({'predicted_SOC': [predicted_SOC], 'real_SOC': [real_SOC]})
        df_result.to_csv(filename, index=False)
         
        # Print predicted and real SOC side by side
        print("Predicted SOC: {}\tReal SOC: {}".format(predicted_SOC, real_SOC))

        return predicted_SOC, real_SOC



# bm = BatteryMonitor('rasberrypi.pkl')
# predicted_SOC, real_SOC = bm.predict_SOC('dataSensor_preprocessed.csv')

```

> This code defines a Python class called **`BatteryMonitor`** which has a constructor method **`__init__`** and a prediction method **`predict_SOC`**. The **`__init__`** method loads a pickled machine learning model from a specified file path, and the **`predict_SOC`** method uses this model to make a prediction on a given input CSV file containing sensor data.
> 
> 
> The **`predict_SOC`** method first reads the input CSV file using Pandas and extracts the real SOC value from the third row of the input data. It then removes the 'SOC' column from the input data and prepares it for prediction by reshaping it into a NumPy array.
> 
> After creating a new Pandas DataFrame with the reshaped input data, the method uses the pickled machine learning model to make a prediction for the SOC value. The predicted and real SOC values are saved to a new CSV file with a filename containing the current date and time.
> 
> Finally, the method prints the predicted and real SOC values side by side and returns the predicted SOC value.
> 
> The commented out code at the end is an example of how to create an instance of the **`BatteryMonitor`** class, load a pickled model, and call the **`predict_SOC`** method to make a prediction on an input CSV file
> 

```python
# importing the multiprocessing module
import multiprocessing
import os
import RunModelScript
import testClass1
import DataPreprocessingScript
import time

def worker1():
    lastFileLength = 0 
    bm=RunModelScript.BatteryMonitor('rasberrypi.pkl')
    while True:
        time.sleep(40)
        # try:
        print("in try")
        preprocessor=DataPreprocessingScript.CSVPreprocessor('data.csv')
        print("in try 2")
        preprocessed_file = preprocessor.preprocess()
        print("in try 3")
        print('PreprocessedFile:', preprocessed_file)
        predicted_SOC, real_SOC = bm.predict_SOC('data_preprocessed.csv')
        print(predicted_SOC,real_SOC)
            # time.sleep(20)
        # except:
        #     print("er")
        #     # time.sleep(20)
        #     continue
            
	# print("ID of process running worker1: {}".format(os.getpid()))
 

def worker2():
    logger = testClass1.SensorDataLogger('data14.csv')
    logger.start()
	# printing process id
	# print("ID of process running worker2: {}".format(os.getpid()))

if __name__ == "__main__":
	# printing main program process id
	print("ID of main process: {}".format(os.getpid()))

	# creating processes
	p1 = multiprocessing.Process(target=worker1)
	p2 = multiprocessing.Process(target=worker2)

	# starting processes
	p1.start()
	p2.start()

	# wait until processes are finished
	p1.join()
	p2.join()

	# both processes finished
	print("Both processes finished execution!")

	# check if processes are alive
	print("Process p1 is alive: {}".format(p1.is_alive()))
	print("Process p2 is alive: {}".format(p2.is_alive()))
```






> This code is using multiprocessing to run two functions simultaneously: **`worker1`** and **`worker2`**.
> 
> 
> **`worker1`** is continuously running in a loop and doing the following:
> 
> - Reading sensor data from a CSV file called **`data.csv`**
> - Preprocessing the data using **`DataPreprocessingScript`**
> - Using a trained model called **`BatteryMonitor`** to predict the state of charge (SOC) of a battery based on the preprocessed data
> - Writing the predicted and actual SOC to a new CSV file with the current date and time in the file name
> 
> **`worker2`** is continuously running in a loop and doing the following:
> 
> - Logging sensor data to a CSV file called **`data.csv`**
> 
> The main program creates two separate processes for each worker function, starts them, waits for them to finish, and then checks if they are still alive.
>