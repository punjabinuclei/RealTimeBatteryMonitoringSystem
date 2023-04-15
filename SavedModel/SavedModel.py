import pandas as pd
import numpy as np

import pickle
pickled_model = pickle.load(open('model.pkl', 'rb'))


df = pd.read_csv("data.csv")
print(df)

Voltage=df.loc[0,'Voltage']
Current=df.loc[0,'Current']
Temperature=df.loc[0,'Temperature']
MeanV=df.loc[0,'EcellMean']
MeanI=df.loc[0,'I_Mean']
MeanT=df.loc[0,'TemperatureMean']
MedianV=df.loc[0,'EcellMedian']
MedianI=df.loc[0,'ImaMedian']
MedianT=df.loc[0,'TempMedian']
StdV=df.loc[0,'Ecell_Vstd']
StdI=df.loc[0,'I_mA_std']
StdT=df.loc[0,'TempStd']
VarianceV=df.loc[0,'Ecell_Variance']
VarianceI=df.loc[0,'I_mA_Variance']
VarianceT=df.loc[0,'Temperature__C_Variance']
Power=df.loc[0,'Power']
Resistance=df.loc[0,'Resistance']
Conductance=df.loc[0,'Conductance']
TempChange=df.loc[0,'temp_change']



Model_Input=[[0.4000000000000057,0.0,1.0,1.0,0.0,0.22222222222222854,0.0,0.0,0.0,1.0,1.0,1.0,1.0,0.9999999999999998,0.9999999999999999,0.0,0.9999999999999999,0.0,0.6666666666666675]]

SOC=pickled_model.predict(Model_Input)
print(100-SOC[0]*100)
# # SOC