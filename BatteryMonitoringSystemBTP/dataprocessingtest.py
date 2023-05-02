
import pandas as pd # data processing
import numpy as np # working with arrays

# preprocessData------------------------------------------------------------------------------------
from sklearn import preprocessing 
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# evaluation metric-----------------------------------------------------------------------------------
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score as r2_score 


# Models
#. Extreme Gradient Boosting--------
import xgboost as xgb

df = pd.read_csv("data.csv")
df=df.abs()



# Mean-------------------------

def sliding_window_mean(values, window_size):
    result = np.zeros(len(values) - window_size + 1)
    for i in range(len(result)):
        result[i] = np.mean(values[i:i+window_size])
    return result

for column_name in ["Voltage", "Current", "Temperature"]:
    column = df[column_name]
    window_size = 10
    mean_values = sliding_window_mean(column, window_size)

    padding = np.empty(len(df.index) - len(mean_values))
    padding[:] = np.nan
    mean_values = np.concatenate((mean_values, padding))

    df[f"{column_name}Mean"] = mean_values



# Median----------------------------
import numpy as np

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



df.to_csv('DataTest.csv', index=False)