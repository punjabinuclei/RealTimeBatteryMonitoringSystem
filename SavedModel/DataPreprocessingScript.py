import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# evaluation metric-----------------------------------------------------------------------------------
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score as r2_score 
import xgboost as xgb

df = pd.read_csv("Test.csv")


# # -----------------------------------------------------------Mean Calculation
def sliding_window_mean(values, window_size):
    result = np.zeros(len(values) - window_size + 1)
    for i in range(len(result)):
        result[i] = np.mean(values[i:i+window_size])
    return result

# # -----------------------------
# # Select the column of interest
column = df["Voltage"]

window_size = 10
mean_values = sliding_window_mean(column, window_size)

# Pad the mean_values array with NaNs to match the length of the DataFrame's index
padding = np.empty(len(df.index) - len(mean_values))
padding[:] = np.nan
mean_values = np.concatenate((mean_values, padding))

# Save the result to a new column in the DataFrame
df["EcellMean"] = mean_values

# # -----------------------------

# # Select the column of interest
column = df["Current"]

window_size = 10
mean_values = sliding_window_mean(column, window_size)

# Pad the mean_values array with NaNs to match the length of the DataFrame's index
padding = np.empty(len(df.index) - len(mean_values))
padding[:] = np.nan
mean_values = np.concatenate((mean_values, padding))

# Save the result to a new column in the DataFrame
df["I_Mean"] = mean_values

# # -------------------------------
# # Select the column of interest
column = df["Temperature"]

window_size = 10
mean_values = sliding_window_mean(column, window_size)

# Pad the mean_values array with NaNs to match the length of the DataFrame's index
padding = np.empty(len(df.index) - len(mean_values))
padding[:] = np.nan
mean_values = np.concatenate((mean_values, padding))

# Save the result to a new column in the DataFrame
df["TemperatureMean"] = mean_values

# print(df)





# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# # ----------------------------------------------------------------------Median

def sliding_window_median(values, window_size):
    result = np.zeros(len(values) - window_size + 1)
    for i in range(len(result)):
        result[i] = np.median(values[i:i+window_size])
    return result

# # ------------------------------


# # Select the column of interest
column = df["Voltage"]

window_size = 10
median_values = sliding_window_median(column, window_size)

# Pad the median_values array with NaNs to match the length of the DataFrame's index
padding = np.empty(len(df.index) - len(median_values))
padding[:] = np.nan
median_values = np.concatenate((median_values, padding))

# Save the result to a new column in the DataFrame
df["EcellMedian"] = median_values



# # ------------------------------

# # Select the column of interest
column = df["Current"]

window_size = 10
median_values = sliding_window_median(column, window_size)

# Pad the median_values array with NaNs to match the length of the DataFrame's index
padding = np.empty(len(df.index) - len(median_values))
padding[:] = np.nan
median_values = np.concatenate((median_values, padding))

# Save the result to a new column in the DataFrame
df["ImaMedian"] = median_values
df


# # ----------------------------
# # Select the column of interest
column = df["Temperature"]

window_size = 10
median_values = sliding_window_median(column, window_size)

# Pad the median_values array with NaNs to match the length of the DataFrame's index
padding = np.empty(len(df.index) - len(median_values))
padding[:] = np.nan
median_values = np.concatenate((median_values, padding))

# Save the result to a new column in the DataFrame
df["TempMedian"] = median_values
# print(df)




# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# # ------------------------------------------------------Standard Deviatoion------------------------------------

def sliding_window_stddev(values, window_size):
    result = np.zeros(len(values) - window_size + 1)
    for i in range(len(result)):
        result[i] = np.std(values[i:i+window_size])
    return result
# # --------------------------------------------------

# # Select the column of interest
column = df["Voltage"]

window_size = 10
stddev_values = sliding_window_stddev(column, window_size)

# Pad the stddev_values array with NaNs to match the length of the DataFrame's index
padding = np.empty(len(df.index) - len(stddev_values))
padding[:] = np.nan
stddev_values = np.concatenate((stddev_values, padding))

# Save the result to a new column in the DataFrame
df["Ecell_Vstd"] = stddev_values
df

# # --------------------------------------------------------


# # Select the column of interest
column = df["Current"]

window_size = 10
stddev_values = sliding_window_stddev(column, window_size)

# Pad the stddev_values array with NaNs to match the length of the DataFrame's index
padding = np.empty(len(df.index) - len(stddev_values))
padding[:] = np.nan
stddev_values = np.concatenate((stddev_values, padding))

# Save the result to a new column in the DataFrame
df["I_mA_std"] = stddev_values
df


# # -----------------------------------------------------

# # Select the column of interest
column = df["Temperature"]

window_size = 10
stddev_values = sliding_window_stddev(column, window_size)

# Pad the stddev_values array with NaNs to match the length of the DataFrame's index
padding = np.empty(len(df.index) - len(stddev_values))
padding[:] = np.nan
stddev_values = np.concatenate((stddev_values, padding))

# Save the result to a new column in the DataFrame
df["TempStd"] = stddev_values
# print(df)













# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # -------------------------------------------------------------Variance


def sliding_window_variance(values, window_size):
    result = np.zeros(len(values) - window_size + 1)
    for i in range(len(result)):
        result[i] = np.var(values[i:i+window_size])
    return result


# # -----------------------------------------------------------------

# # Select the column of interest
column = df["Voltage"]

window_size = 10
variance_values = sliding_window_variance(column, window_size)

# Pad the variance_values array with NaNs to match the length of the DataFrame's index
padding = np.empty(len(df.index) - len(variance_values))
padding[:] = np.nan
variance_values = np.concatenate((variance_values, padding))

# Save the result to a new column in the DataFrame
df["Ecell_Variance"] = variance_values

# # -------------------------------------------------------------------

# # Select the column of interest
column = df["Current"]

window_size = 10
variance_values = sliding_window_variance(column, window_size)

# Pad the variance_values array with NaNs to match the length of the DataFrame's index
padding = np.empty(len(df.index) - len(variance_values))
padding[:] = np.nan
variance_values = np.concatenate((variance_values, padding))

# Save the result to a new column in the DataFrame
df["I_mA_Variance"] = variance_values

# # 

# # Select the column of interest
column = df["Temperature"]

window_size = 10
variance_values = sliding_window_variance(column, window_size)

# Pad the variance_values array with NaNs to match the length of the DataFrame's index
padding = np.empty(len(df.index) - len(variance_values))
padding[:] = np.nan
variance_values = np.concatenate((variance_values, padding))

# Save the result to a new column in the DataFrame
df["Temperature__C_Variance"] = variance_values



# # --------------------------------------------------------Power

# # Select the columns of interest
voltage_column = df["Voltage"]
current_column = df["Current"]

# Multiply the columns to get the power
power_column = (voltage_column * current_column)/1000

# Save the result to a new column in the DataFrame
df["Power"] = power_column
df


# # ---------------------------------------------------------Resistance


# # Select the columns of interest
voltage_column = df["Voltage"]
current_column = df["Current"]

# Multiply the columns to get the power
resistance_column = (voltage_column / current_column)*1000

# Save the result to a new column in the DataFrame
df["Resistance"] = resistance_column
df


# # ----------------------------------------------------------Conductance




conductance_column = 1/resistance_column

# # Save the result to a new column in the DataFrame
df["Conductance"] = conductance_column
df




# ---------------------------------------------------------Temperature Differnce
# # Select the column of interest
temp_column = df["Temperature"]

# Calculate the difference between consecutive rows
temp_change = temp_column.diff()
# Fill the first row with 0
temp_change.iloc[0] = 0


# Save the result to a new column in the DataFrame
df["temp_change"] = temp_change
df

# print(df)




# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Replace inf values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)



# Remove rows containing NaN values
df.dropna(inplace=True)


# Initialize the scaler
scaler = MinMaxScaler()

# Fit and transform the data
df_scaled = scaler.fit_transform(df)

# Put the transformed data back into a dataframe
df = pd.DataFrame(df_scaled, columns=df.columns)


# print(df)


# --------------------------------------------------------
# df.drop('SOC', axis=1, inplace=True)
df.to_csv('data.csv', index=False)