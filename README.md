
# Real-time prediction of Battery SoC in UAVs: A Machine Learning Perspective



## Introduction

In this project, we explore a machine learning-driven prediction approach, leveraging the power of **XGBoost** as our algorithm of choice. The methodology involved meticulous problem identification, complemented by robust statistical analysis to validate our outcomes. We constructed a resilient **Battery Management System (BMS) module**, integrating diverse software and hardware components. The module collected real-world data from a quadcopter, establishing a comprehensive training dataset for **predicting State of Charge (SoC)**.

To enhance realism, we introduced three types of noise and evaluated the model's performance under distinct charging conditions. The results were promising, revealing nuanced behavior: as battery charging levels decreased, prediction errors increased to a certain extent, introducing inaccuracies. Notably, our model showcased heightened accuracy at higher charging levels.

While our findings indicate substantial potential for refining model parameters to achieve optimal accuracy across all charging levels, our current results mark a significant step forward in **machine learning-based battery prediction.**

## Code Structure
The Code folder contains three sub-folders:

- **DataCollection_Arduino**: Arduino codes for collecting data (current, voltage, temperature, SOC) and a combined sensor data collection script.

- **Notebook**: Python scripts for machine learning algorithms, preprocessing, and analysis.

- **RealTimePredictionScripts**: Python scripts for real-time BMS predictions, including data logging, preprocessing, machine learning model execution, and script execution.
  
## Project Features

#### Smart Battery Predictions with XGBoost:
- Leverages XGBoost, a robust machine learning algorithm, for precise battery state predictions.
#### Thorough Selection Process:

- Details the meticulous approach to problem identification and statistical validation.
#### Integrated Battery Management System (BMS) Module:

- Incorporates a well-structured BMS module, combining software and hardware components seamlessly.
#### Real-world Data Collection from Quadcopter:

- Gathers practical data from a quadcopter, forming the foundation for accurate State of Charge (SoC) predictions.
#### Real-world Scenario Emulation:

- Simulates real-world conditions by introducing various types of noise, evaluating the model's resilience under different charging scenarios.
#### Diverse and Cost-effective Sensor Array:

- Utilizes budget-friendly sensors including ACS712 for current measurement, LM35 for temperature, Voltage Detection Sensor Module 25V for voltage, Raspberry Pi for computation, and PDB-XT60 for power distribution.
#### Error Evaluation and Insights:

- Analyzes prediction errors across charging levels, offering valuable insights into model accuracy.
#### Potential for Optimization:

 - Identifies opportunities for refining model parameters to enhance accuracy, particularly in lower charging states.
#### Flexible and Adaptable Design:

- Built to accommodate future enhancements and modifications, ensuring adaptability for evolving needs.
#### Practical Applicability:

- Extends usability to diverse scenarios, particularly beneficial for drone operations and other applications requiring accurate battery predictions.
# Project Setup

## Requirements

### Hardware

Ensure the availability of the following hardware components:

- **ADC Converter (ADS1115):** To convert analog signals to digital for precise measurements.
- **Power Distribution Board (PDB-XT60):** For efficient power distribution within the system.
- **Microprocessor (Raspberry Pi 4):** Serving as the computational brain of the system.
- **Orange 2000mAh 3S 25C Lithium Polymer Battery:** The power source for the entire system or any other battery you want to use for your BMS
- **Temperature Sensor (LM35):** Measuring the temperature of the battery.
- **Current Sensor (ACS712):** For accurate measurement of the battery's current.
- **Voltage Sensor (Voltage Detection Sensor Module 25V):** Measuring the battery voltage.
- **Raspberry Pi and Arduino:** Integral components for data processing and initial data collection.

Additionally, you'll need a PC to run initial data collection, train the model used for prediction, and collect data.


## Software Requirements

Before getting started, make sure your system meets the following software requirements:

- **Operating System:** Ensure that your system is running the latest updated operating system.

- **Python:** Install the latest version of Python. You can download it [here](https://www.python.org/downloads/).

  ```bash
  pip install pandas numpy matplotlib termcolor scikit-learn xgboost keras


#### The required Python libraries for data processing, visualization, preprocessing, and model evaluation will be installed using the above command.

- **Arduino IDE**: Install the Arduino IDE for uploading Arduino codes to your hardware.

- **Visual Studio Code (VSCode)**: A code editor for running machine learning algorithms efficiently.

- **Chrome Browser**: Required for running machine learning algorithms if your machine has limited processing power using google collab.


### Required Python Libraries

    import pandas as pd  # Data processing
    import numpy as np  # Working with arrays
    from matplotlib import pyplot as plt  # Visualization
    from termcolor import colored as cl  # Text customization

    from sklearn import preprocessing  # Preprocess data
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.model_selection import train_test_split

    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  # Evaluation metrics

    # Models
    from sklearn.linear_model import LinearRegression  # OLS algorithm
    from sklearn.tree import DecisionTreeRegressor  # Decision Tree
    from sklearn.ensemble import RandomForestRegressor  # Random Forest
    from sklearn.ensemble import GradientBoostingRegressor  # Gradient Boosting
    import xgboost as xgb  # Extreme Gradient Boosting
    import keras  # Neural Networks
    from keras.models import Sequential
    from keras.layers import Dense
    from sklearn.svm import SVR  # Support Vector Machines
    
    
Ensure the installation of these libraries to run the scripts seamlessly.
Now, you're ready to explore and enhance the capabilities of our Battery Management System!


## Project Usage Instructions

## Usage

### 1. Data Collection for Model Training

- Connect your Arduino setup with the required sensors (ACS712 for current, LM35 for temperature, and Voltage Detection Sensor Module 25V for voltage).
- Use Arduino IDE to upload the codes from the `DataCollection_Arduino` folder to your Arduino hardware.
- Run the Arduino setup to collect data for model training.

### 2. Machine Learning Model Training and Analysis

- Utilize the Jupyter notebook in the `Notebook` folder to explore and train various machine learning algorithms.
- Compare the algorithms based on metrics like RMSE, MAE, and R-Squared.
- Select the most accurate algorithm for your Battery Management System (BMS).

### 3. Real-Time Battery Predictions

- Deploy the Raspberry Pi setup for real-time battery predictions.
- Execute scripts from the `RealTimePredictionScripts` folder, including `SensorDataLogger.py` for data collection and preprocessing, and `MLModelScript.py` for real-time predictions.
- Refer to `Script_Execution_Guide.md` for detailed step-by-step instructions.


### 4. Further Exploration

- Explore the `Reports` folder for in-depth insights into project development and results.
- Feel free to experiment with different sensors or adapt the code for various battery-powered devices.

Now, you're all set to leverage our Battery Management System! If you have any questions or improvements, don't hesitate to reach out and contribute.
