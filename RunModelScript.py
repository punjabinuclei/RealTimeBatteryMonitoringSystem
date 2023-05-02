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
