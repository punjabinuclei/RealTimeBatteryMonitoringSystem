# RealTimeBatteryMonitoringSystem


# Real-Time Battery Monitoring System Using Machine Learning
* Introduction

Lithium-ion batteries are now employed in a wide range of applications, from personal electronic gadgets like cell phones to the rising class of electric vehicles. Because these batteries are more vulnerable than lead-acid or NiCd batteries, they require more sophisticated monitoring to ensure safe operation.
The EV sector is experiencing a surge in demand for an effective battery management system, but this requires initial battery monitoring. In India, we can see an exponential increase in the number of electric Rickshaws that use lead acid batteries rather than more efficient lithium-ion batteries. Because the cost of a lead acid battery is significantly lower than that of a lithium-ion battery, it is critical to develop a battery monitoring and management system for lead acid batteries.
These lead acid batteries perform well at room temperature but poorly at lower temperatures. The existing technology is not adaptive to changing air conditions, and in a country like India, temperature plays a vital part in determining battery performance because temperatures here can reach 51.0 °C.
Battery Management System

The primary function of a Battery Management System (BMS) is to guarantee that the energy stored in the battery that powers the portable device is utilised optimally and that the battery is protected from damage. This is accomplished by monitoring and managing the charging and draining process of the battery.
In general, the BMS consists of the following functionalities
	Sensing Functionalities
	Current
	Voltage
	Temperature
	Protection Functionalities
	Short circuits
	Over voltage, current and temperature
	Disconnecting a faulty cell
	Estimation
	State of charge
	State of health
As well as data communication between BMS master module and BMS acquisition modules as well as battery pack and surrounding applications


Temperature Acquisition

One of the most difficult jobs when developing a BMS is determining the most precise temperature achievable. Not only must the pros and disadvantages of the different available sensor types (completely digital interface or analogue) be considered, but also where to measure the temperature of the pack. As a result, the needed number of cell temperature sensors is determined. In order to establish the optimal placement for a limited number of sensors, simulations may be necessary. When conceptualising a battery pack optimised for light weight, hefty copper busbars must be avoided as much as possible, forcing the design engineer to address possible thermal peaks during high power operation, necessitating thermal monitoring of busbars as well.
A temperature requirement must, in general, address three use cases: charging, discharging, and storage. Batteries based on lithium cannot function adequately in extreme temperatures. Even within these constraints, though, accurate temperature readings are critical. At too high current rates, the significant effect of lithium plating can occur in the usual temperature range. Temperature, voltage, and current must be accurately measured to avoid lithium plating. Battery cells have a high thermal capacitance and strong thermal conductivity (in particular geometric routes), which are influenced and limited by thermal isolation boundary layers (housing, geometry of cells, etc.). If temperature sensors are not set properly, misreadings and thermal blind spots can occur.
Voltage Acquisition

A traditional lithium-ion battery management system must include at least one voltage acquisition channel per serially connected cell. Specific charging profiles are required for various battery chemistry to improve performance and prevent safety hazards during charge. Almost all Li-ion battery chargers use a constant current/constant voltage charging strategy in general. Once the charger enters constant voltage mode, it is critical to ensure that the charge does not exceed the maximum level permitted in order to prevent exposing them to overcharge circumstances, which can cause excessive internal temperature rise and early failure. Rechargeable lithium ion battery cells can safely run at 2.75V per cell. However, if an unprotected lithium cell is discharged over the minimum voltage level, the cell may be damaged, resulting in decreased cycle life, unpredictable voltage characteristics, and enlargement of cells due to internal chemical reaction. 
Current Acquisition

Current sensors, in addition to being imperfect systems, suffer from drift, offset, and temperature inaccuracy. Furthermore, the current sensors that are used frequently must meet contradictory requirements at the same time: it is not uncommon for current sensors in automotive applications to be able to measure currents starting in the milliampere range while also being able to measure currents up to 1000 Ampere. Depending on the application, the sensor might need to have a high bandwidth to capture fast current changes. Furthermore, the existing sensor's precision and immunity to EMI noise should be evaluated.
Definitions

In addition to being non-ideal systems, current sensors are also subject to a certain amount of drift, offset, and temperature inaccuracy. In addition to this, the present sensors that are employed often have to fulfil contradictory requirements at the same time:
State-of-Charge (SoC) - State-of-Charge is the proportion of a rechargeable battery's maximum possible charge that is present. The SoC indicator consists of battery readings and modelling. As a simple illustration, the battery voltage (V) can be sensed and the V-SoC relationship can be stored in a microcontroller's look-up table function.
State-of-Health (SoH) – State of Health is a'measure' that represents the general state of a battery and its ability to deliver the specified performance relative to a brand-new battery. State-of-Health (SoH) is an indication of the point in the battery's life cycle that has been reached and a measurement of its state relative to a new battery. The SoH indicator may incorporate cycle-counting, for instance. In the simplest example, the number of full charge/discharge cycles (Cn) can be counted and the SoH can be calculated using a maximum capacity-Cn function that has been previously stored.
The remaining run-time (tr) is the expected amount of time a battery can continue to give power to a portable device under valid discharge conditions before the device ceases to function. Depending on the type of load, the remaining run-time can be deduced from the remaining capacity in one of two ways: in the case of a current-type load, the remaining capacity in mAh, so expressed as charge, is divided by the drawn current in mA, and in the case of a power-type load, the remaining capacity in mWh, so expressed as energy, is divided by the drawn power in mW.
Working of a BMS System

The battery management system monitors each individual battery cell. It then estimates how much current can enter and exit the battery without causing damage. The current restrictions prevent the source and load from excessively discharging or charging the battery. This protects the battery pack against excessively high or low cell voltages, extending the battery's life.
The BMS also monitors the battery's remaining charge. It continuously monitors cell voltages and the quantity of energy entering and leaving the battery pack. It uses this information to determine when the battery is depleted and shut it down. Following data capture, the data is routed via the necessary components in order to complete the appropriate activities via the Control Area Network Network. 

Applications of a BMS

Battery monitoring systems are used in a variety of applications where the performance and health of a battery are critical. Some common examples include in electric vehicles, renewable energy systems (such as solar and wind power systems), and backup power systems (such as in hospitals and data centers). Battery monitoring systems can also be used in consumer electronics, such as smartphones and laptops, to provide users with information about the battery life and health of their devices.
 
Figure 3- Application Areas

	Determining the state of charge in electric vehicles and autonomous vehicles
	Maintaining the temperature of a charger
	Battery monitoring of a multicopters and drones
	BMS is used in service robots
	Small sized power tools using DC motors require BMS for the users safety
	Wearables also use BMS
	Home appliances operated with battery need a good BMS

Methodology


Literature Review
 
 

 
 
 

 
 



 

 

Problem Statement

The majority of battery monitoring systems used today rely on the measurement of current, voltage, and, ultimately, state of charge (SOC) through the use of hardware circuits and methods. These methods do not take into account the temperature of the surrounding environment, which is a parameter that is quite important in determining the accurate estimate of the battery's runtime Current algorithms (such as Coulomb Counting and the Voltage Method) are susceptible to hysteresis, which is a condition in which there is a delay in the output of a system and results in a certain amount of error in measurements. The effects of ageing batteries are not taken seriously, which has a negative impact on accuracy.
Objectives

In this day and age of artificial intelligence, there are very few BMS systems that are based on machine learning. One of the best solutions to overcome the challenges that were mentioned is to use a data driven approach in order to be efficient and accurate. In order to achieve the best possible outcome, it is necessary to investigate the various approaches to machine learning and to identify the method that is most effective. Additionally, it is necessary to take into account the impact of the temperature of the battery.An enormous quantity of data sets needs to be gathered at a variety of temperature extremes, and on the basis of those data sets, with the assistance of machine learning, a successful model needs to be developed.

Procedure

	To develop a battery monitoring hardware system

A microcontroller such as an Arduino or a Raspberry Pi to collect and process data from the battery; a voltage measurement device, such as a voltage divider or a voltage sensor, to measure the battery's voltage; a current measurement device, such as a current shunt or a current sensor, to measure the battery's current; a display, such as an LCD screen or an OLED screen, to display the battery's voltage, current, and any other pertinent information; a power supply. This will enable the microcontroller to measure the voltage of the battery. Connect the device for measuring current to the battery and microcontroller. This will enable the microcontroller to measure the current of the battery. Establish a connection between the display and the microcontroller. This will allow the microcontroller to display the battery's voltage, current, and other pertinent information. Programming the microcontroller to collect data from the voltage and current measurement devices and display it on the displayThe code for the microcontroller can be written using a programming language, such as C or Python. Verify the functionality of the battery monitoring hardware by performing a series of tests. This can be accomplished by measuring the voltage and current of the battery and comparing the displayed values to the actual values.

	Testing the hardware system

First of all, ensuring that the bms hardware system is properly installed and connections are valid. Next, power on the system and verify that every component is operating properly. This can be accomplished by manually inspecting each component or by employing diagnostic software to perform a system test. Once confirmed that all of the system's components are functioning properly, you can begin performance testing. This can be accomplished by simulating different operating conditions, such as temperature and load scenarios, and observing the system's response. As you test the system, be aware of any errors or malfunctions that may occur and make a note of any problems you encounter. You can then use this data to troubleshoot and resolve any potential issues. After a system has been thoroughly tested, it is essential to perform routine maintenance and inspections to ensure that it continues to operate properly over time. This may involve routinely inspecting and replacing components, as well as performing periodic diagnostic tests to ensure the optimal operation of the system. 

	Select a Machine Learning Algorithm with necessary requirements

When selecting a machine learning algorithm for a specific task, numerous considerations must be taken into account. Consider the type of data you have access to, the nature of the problem you are attempting to solve, and the objectives you wish to accomplish. The following steps will assist you in selecting an appropriate machine learning algorithm: Define the problem you are attempting to solve and the type of machine learning problem you must address (e.g., classification, regression, clustering, etc.). Comprehend the various types of algorithms and their respective strengths and weaknesses. Certain types of problems or data are better suited to algorithms than others. Think about the quantity and quality of your data. Some algorithms require a large amount of training data, while others can function with a smaller amount. Using metrics such as accuracy, precision, and recall, evaluate the performance of different algorithms on your data. Select the algorithm that performs the best on your dataset and aligns with your objectives. Noting that there is no one-size-fits-all solution for selecting a machine learning algorithm is crucial. The optimal algorithm for your problem will be determined by a number of variables and may require experimentation.

	Training and Testing the machine learning model

Collect and prepare the training dataset: To begin, collect and prepare the training dataset. This requires cleansing the data, ensuring it is in a usable format, and separating it into training and validation sets. After selecting a model and preparing the training data, the model needs to be trained using the training data. This involves feeding the data into the model and adjusting the parameters of the model to minimise the error on the training data. Evaluate the model: After training the model, its performance on the validation data must be evaluated. This will provide insight into how well the model generalises to new data. After evaluating the model, it may be necessary to fine-tune its parameters to improve its performance on the validation data. This may involve modifying the model's learning rate, regularisation intensity, or other hyperparameters. Finally, test the model on a held-out test set to determine how well it performs on unseen data. This will provide a final estimate of the performance of the model. Hardware Requirements. 

Voltage Sensor – (Voltage Detection Sensor Module 25V )

A voltage detection sensor module 25V is a device designed to measure the voltage of a circuit with a maximum voltage of 25V. It typically consists of a sensor, amplifier, and output interface, which enables a microcontroller or other device to read the measured voltage. Typically, the sensor consists of a voltage divider circuit that transforms the input voltage into a smaller, more easily measurable voltage. The amplifier amplifies the sensor's output signal to make it more accurate and easier to read, and the output interface permits a microcontroller or other device to read the measured voltage. This type of voltage sensor module is typically employed in applications where the input voltage is restricted to 25V or less, such as in battery-powered devices or low-voltage electrical systems. This module is based on the principle of resistive voltage divider design, can make the red terminal connector input voltage to 5 times smaller. Arduino analog input voltages up to 5 v, the voltage detection module input voltage not greater than 5Vx5=25V (if using 3.3V systems, input voltage not greater than 3.3Vx5=16.5V). Arduino AVR chips have 10-bit AD, so this module simulates a resolution of 0.00489V (5V/1023), so the minimum voltage of input voltage detection module is 0.00489Vx5=0.02445V.

Current Sensor – ACS712

The ACS712 is a module for measuring the current flowing through an electrical circuit. It consists of a Hall effect sensor, which detects the magnetic field generated by a conductor's current, and an amplifier circuit, which amplifies the sensor's output signal. Depending on the model, the ACS712 can measure both AC and DC currents with a range of 5A, 20A, or 30A. The measured current can be output as an analogue voltage or a digital pulse-width modulation (PWM) signal, which can be read by a microcontroller or other device. Common applications for the ACS712 include motor control, overcurrent protection, and power supply design.

Temperature Sensor – LM35 
The LM35 is a temperature sensor used to measure the temperature of a physical object or the surrounding environment. It is a precision integrated-circuit temperature sensor, so it is extremely accurate and stable over a broad temperature range. With a scale factor of 10 mV/°C, the LM35 outputs an analogue voltage that is proportional to the temperature in degrees Celsius. This means that the output voltage of the LM35 will vary by 10 millivolts for every degree Celsius of temperature change. The LM35 is utilised in numerous temperature sensing applications, including thermostats, temperature-controlled fans, and temperature data loggers.

Lemon 1800mAh 3S 25C Lithium Polymer Battery
The Lemon 1800mAh 3S 25C/50C Lithium Polymer battery is a common rechargeable battery found in radio-controlled (RC) vehicles and other electronic devices. It has a capacity of 1800mAh, indicating that it can store a substantial quantity of energy. The "3S" designation denotes that the battery consists of three lithium-ion cells connected in series, resulting in a nominal voltage of 11.1V. The designation "25C/50C" indicates that the battery can deliver a continuous discharge current of 25C or 50C, depending on the application. The "Lemon" brand produces premium lithium polymer batteries, and the 1800mAh 3S 25C/50C battery is a popular option for RC vehicles and other high-performance electronic devices.
Microprocessor – Raspberry Pi 4    
The Raspberry Pi Foundation designs and manufactures the Raspberry Pi 4, a small, low-cost, single-board computer. It was released in June 2019 and is the most recent instalment in the Raspberry Pi computer line. Compared to its predecessor, the Raspberry Pi 3 Model B+, the Raspberry Pi 4 has a faster processor, more memory, and dual-display output support. Common applications include a home media centre, a do-it-yourself gaming console, and an inexpensive computer for education and programming. The Raspberry Pi 4 is a highly capable single-board computer that can perform a variety of tasks, such as media playback, gaming, and basic computing.
Power Distribution Board – PDB-XT60
Within an electronic system, a power distribution board (PDB) is a device used to distribute electrical power to multiple circuits or devices. A PDB-XT60 is a specific type of PDB that provides power to devices via XT60 connectors. XT60 connectors are a common type of high-current connector found on radio-controlled aircraft and vehicles. Typically, a PDB-XT60 is used to power the electronic speed controllers (ESCs) and other devices in a radio-controlled aircraft or vehicle. It assists in power distribution and protects against overcurrent and short-circuit conditions. 









Hardware Circuit

 

Figure 10 - Circuit diagram of BMS Module
Overview of machine learning

Machine learning is a subfield of artificial intelligence that employs algorithms and statistical models to enable a system's performance on a particular task to improve over time. Machine learning algorithms can make predictions, classifications, and decisions based on what they have learned from examples and data. Several tasks, including image and speech recognition, natural language processing, and predictive modelling, are amenable to machine learning. It is a rapidly expanding field that is utilised in numerous industries, including healthcare, finance, transportation, and retail.
Models for machine learning include supervised learning, unsupervised learning. Training a model on a labelled dataset in which the correct outputs are provided for each example in the training data constitutes supervised learning. The model uses this information to determine the relationship between input and output, and can then make predictions based on new, unobserved data. Regression and classification assignments are examples of supervised learning. 
Unsupervised learning entails training a model with an unlabeled dataset in which the correct outputs are not provided. The model must self-learn to recognise patterns and structure in the data. Unsupervised learning includes tasks like clustering and dimensionality reduction.
Choice of model
We choose supervised learning because the goal is to train a model to make predictions or decisions based on labeled training data. In supervised learning, the training data includes both the input features and the corresponding correct outputs. The model uses this information to learn the relationship between the input and the output, and can then make predictions on new, unseen data.
Regression models was implemented because the voltage, current and temperature are continuous variable, such as a price or a probability. They are frequently employed in applications where the objective is to comprehend the relationship between various variables and to make predictions based on this relationship. A regression model could be used, for instance, to predict the sale price of a house based on its size, location, and other characteristics.
Ordinal Least Square Regression 
Ordinary Least Squares (OLS) regression is a popular method for estimating the coefficients of linear regression equations that describe the relationship between one or more independent quantitative variables and a dependent variable (simple or multiple linear regression). Least squares represent the least squares error (SSE). In our case the model is multivariable regression which uses more than one variables as input to predict the output.
The governing equation behind the regression is to calculate the slope and coefficients of a linear equation 
Y= β_0+ β_1 X_1+ β_2 X_2+⋯.+ β_k X_k+ ε	 						(1)	
For two variables, the slope can be calculated by:
β_0=Y ̅- β_1 (X_1 ) ̅- β_2 (X_2 ) ̅  									(2)
β_1 & β_2 are the coefficients of the variables   
β_1 = ((∑▒x_2^2 )(∑▒〖x_1 y〗)- (∑▒〖x_1 x_2 〗)(∑▒〖x_2 y〗))/((∑▒x_1^2 )(∑▒x_2^2 )- (∑▒x_1  x_2 )^2 )								(3)
β_2 = ((∑▒x_1^2 )(∑▒〖x_2 y〗)- (∑▒〖x_1 x_2 〗)(∑▒〖x_1 y〗))/((∑▒x_1^2 )(∑▒x_2^2 )- (∑▒x_1  x_2 )^2 )								(4)
∑▒〖x_1^2= ∑▒〖X_1 X_1- (∑▒X_1 )(∑▒X_1 )/N〗〗 								(5)
∑▒〖x_2^2= ∑▒〖X_2 X_2- (∑▒X_2 )(∑▒X_2 )/N〗〗 								(6)
∑▒〖x_1 y= ∑▒〖X_1 Y- (∑▒X_1 )(∑▒Y)/N〗〗 									(7)
∑▒〖x_2 y= ∑▒〖X_2 Y- (∑▒X_2 )(∑▒Y)/N〗〗 									(8)
∑▒〖x_1 x_2= ∑▒〖X_1 X_2- (∑▒X_1 )(∑▒X_2 )/N〗〗 								(9)
here 
Y ̅ = mean of the dependent variable known as ‘label’
(X_1 ) ̅ & (X_2 ) ̅ are the mean values of independent variables known as ‘features’
β_0 is the intercept, β_1 & β_2 are the coefficients
Line of Best Fit
The main purpose of the best fit line is that our predicted values should be closer to our actual or the observed values, because there is no point in predicting values which are far away from the real values. In other words, we tend to minimize the difference between the values predicted by us and the observed values, and which is actually termed as error.
Bias

Bias is the difference between our actual and predicted values. Bias is the simple assumptions that our model makes about our data to be able to predict new data. When the Bias is high, assumptions made by the model are too basic, the model can’t capture the important features of the data. Thus the model hasn’t captured patterns in the training data and hence cannot perform well on the testing data too. This instance, where the model cannot find patterns in our training set and hence fails for both seen and unseen data, is called Underfitting. 


Variance

During training, it allows the model to ‘see’ the data a certain number of times to find patterns in it. If it does not work on the data for long enough, it will not find patterns and bias occurs. On the other hand, if the model is allowed to view the data too many times, it will learn very well for only that data. It will capture most patterns in the data,  but it will also learn from the unnecessary data present, or from the noise. We can define variance as the model’s sensitivity to fluctuations in the data. Our model may learn from noise. This will cause our model to consider trivial features as important. For any model, we have to find the perfect balance between Bias and Variance. This just ensures that we capture the essential patterns in our model while ignoring the noise present it in. This is called Bias-Variance Tradeoff. It helps optimize the error in our model and keeps it as low as possible. 
Cost Function 
After training the model, we need to check how well the model is performing. Hence, the function which corrects the model is required in order to get accuracy and make it the best trained model. A Cost Function is used to measure just how wrong the model is in finding a relation between the input and output. It tells us how badly the model is predicting.
Cost Function =  1/n ∑_0^n▒(Y_pred- Y_actual )^2 							(10)
Gradient Descent

Gradient Descent is an algorithm that is used to optimize the cost function or the error of the model. It is used to find the minimum value of error possible in your model. Gradient Descent can be thought of as the direction one have to take to reach the least possible error. The error in the model can be different at different points, and a quickest method to reduce the computational efficiency needs to be found.
Gradient Descent can be visualized as a ball rolling down a hill. Here, the ball will roll to the lowest point on the hill. It can take this point as the point where the error is least as for any model, the error will be minimum at one point and will increase again after that. In gradient descent, the error for individual input variables are found. This is repeated, and soon the error values keep getting smaller and smaller. Soon we can get the values for variables when the error is the least, and the cost function is optimized. 
Root Mean Squared Error (RMSE)
The RMSE serves as a cost function to minimize the error in linear regression. The RMSE estimates the deviation of the actual y-values from the regression line. RMSE value with zero indicates that the model has a perfect fit. The lower the RMSE, the better the model and its predictions. A higher RMSE indicates that there is a large deviation from the residual to the ground truth.
RMSE  = √((∑_0^N▒(Y_(pred - Y_actual ) )^2 )/N)								(11)
R Squared
R-squared is a statistical measure that indicates how well a regression model fits the data. The ideal r-square value is 1. The more closely r-square approaches 1, the better the model's fit. R-square is the ratio between the residual sum of squares (SSres) and the total sum of squares. The residual sum of squares is calculated by the summation of squares of perpendicular distance between data points and the best-fitted line. 
The goodness of fit of regression models can be analyzed on the basis of the R-square method. The more the value of r-square near 1, the better is the model. The value of R-square can also be negative when the model fitted is worse than the average fitted model. As new variables are added to the model, the value of r-square always increases or remains constant, without detecting the significance of this newly added variable (i.e value of r-square never decreases on the addition of new attributes to the model). Consequently, non-significant attributes can also be added to the model with an increase in the value of r-square. This is because SStot is always constant and the regression model attempts to reduce the value of SSres by finding a correlation with the new attribute; as a result, the overall value of r-square rises, which can result in a poor regression model.
R-Squared=1-(∑▒(y_act- y_pred )^2 )/(∑▒(y_act- y_avg )^ ) 							(12)

 

Choice of Dataset

Our requirements included the dataset which consists of continuous voltage, current, temperature and battery capacity measured every second accurately. An LG 18650HG2 Li-ion Battery Data is used in the model. The data was taken from the HPPC Tests performed at McMaster University in Hamilton, Ontorio, Canada by Dr. Phillip Kollmeyer. 
Specifications of the dataset

A brand new 3Ah LG HG2 cell was tested in an 8 cu.ft. thermal chamber with a 75amp, 5 volt Digatron Firing Circuits Universal Battery Tester channel with a voltage and current accuracy of 0.1% of full scale.
	A series of tests were performed at different temperatures (10℃, 25℃, 40℃) and the battery was charged after each test at 1C rate to 4.2V.
	The discharge tests were performed with different C ratings in the data provided
	The data was collected using 4 pulse Hybrid Pulse Power Characterization Test (HPPC Test).
	We have collected and made a combined dataset at different temperature and at different C ratings because the aim is to train the model at different temperatures in real life circumstances and can be made versatile with different discharging rates.
	Around 14960 datapoints are obtained and used in the model.
Hybrid Pulse Power Characterization (HPPC)

The method of testing and evaluating the performance of batteries, fuel cells, and other energy storage devices is known as hybrid pulse power characterization (HPPC). It involves applying a combination of constant current and voltage pulses to the device under test and measuring its voltage, current, and power response. In the development and optimization of batteries and other energy storage technologies, HPPC testing is commonly employed. It can aid in identifying areas for improvement and provide valuable insights into the device's performance under various operating conditions.
Feature Extraction
Features are the input variables that we provide to our machine learning models. Each column within the dataset represents a feature. To train an optimal model, we must utilise only the most important features. If there are too many features, the model may learn from noise and capture unimportant patterns. Feature Selection refers to the process of selecting the most relevant data parameters. To train a model, we collect massive amounts of data to help the machine learn more effectively. Typically, a significant portion of the data collected is noise, and certain columns of our dataset may not significantly contribute to the performance of our model. In addition, having a large amount of data can slow down the training process and result in a slower model. The model may also be inaccurate if it learns from irrelevant data. Feature selection is what distinguishes high-quality data from the rest. correct response is Feature Selection. In addition to selecting the appropriate model for our data, we must also select the appropriate data for our model.
Feature Selection is the method of reducing the input variable to your model by using only relevant data and getting rid of noise in data.


Data splitting

The greatest challenge for ML/DL practitioners is determining how to divide data for training and testing. Although it initially appears to be a simple problem, its complexity can only be determined by delving deeper into it. Inadequate training and testing sets can have unpredictable effects on the model's output. It may result in overfitting or underfitting of the data, causing our model to produce biassed outcomes. Ideally, the data should be divided into three sets: train, test, and validation/dev. 
Training Set - The data which will be fed into the model will be contained within the train set. Simply put, our model would gain knowledge from this data. For instance, a Regression model would use these examples to identify gradients in order to decrease the cost function. Then, these gradients will be utilised to reduce costs and accurately predict data.
Validation Set - Validate the trained model with the development set. This is the most crucial setting because it will serve as the foundation for our model evaluation. If the difference between error on the training set and error on the test set is extremely large, this indicates that the model has a high variance and is therefore overfit.
Testing Set - The test set consists of the data used to evaluate the trained and validated model. It tells us how efficient our overall model is and the likelihood that it will predict something illogical. Numerous evaluation metrics (such as precision, recall, and accuracy, etc.) can be used to measure the performance of our model.
Normalization

The purpose of normalization is to transform data in a way that they are either dimensionless and/or have similar distributions. This process of normalization is known by other names such as standardization, feature scaling etc. Normalization is an essential step in data pre-processing in any machine learning application and model fitting. Normalization gives equal weights/importance to each variable so that no single variable steers model performance in one direction just because they are bigger numbers.
Rescaling: also known as “min-max normalization”, it is the simplest of all methods and calculated as:
x^`=  (x- x_min)/x_max⁡〖- x_max 〗   										(13)

	
Ridge Regression

A generalized model should have a low bias and low variance in order to be a good model. Overfitting occurs due to the result of high variance. In Linear regression the cost function was R-Squared. Thus we reduce the overfitting with the help of Ridge Regression.
Cost Function =  1/n ∑_0^n▒〖(Y_pred- Y_actual )^2+ (∑_0^n▒〖m_i^2)〗〗
Here we have an extra penalty term known as lambda. It reduces the error and hence tries to make the slope close to zero but not zero. Thus we are penalizing the higher slopes. It shrinks the parameters and thus it prevents multicollinearity (one predicted value in multiple regression models is linearly predicted with others to attain a certain level of accuracy.). It uses L2 Regularization technique. Higher the values of penalty, therefore the magnitude of slopes are reduced to zero.
Lasso Regression
Lasso is similar to ridge regression instead it has a modulus which tries to make the slope zero. Therefore, lasso selects the only some feature while reduces the coefficients of others to zero. This property is known as feature selection and which is absent in case of ridge. It is generally used when we have more number of features, because it automatically does feature selection. It uses L1 regularization technique. Finally it reduces the variance obtained by the huge variables in dataset.

Cost Function =  1/n ∑_0^n▒〖(Y_pred- Y_actual )^2+ (|∑_0^n▒m_i |)〗					(14)



Model Evaluation

The more the value of r-square near 1, the better is the model. Here from the three regression models, OLS is the most accurate model with the data but there is drawback that it overfits the data and there is multicollinearity. Thus ridge and lasso regression are used when thereare more features and lasso regression also helps in feature selection by reducing the unneccessary features.

 
Future Work

Although the regression is giving the maximum accuracy, it can not work with huge amount of data and thus the role of deep learning comes to play. In coming months our main goal will be to use neural network models such as Support Vector Machine (SVM), Artificial Neural Networks (ANN) to predict the state of charge. 
After testing the model, our next goal would be to integrate the hardware system with this model and real time data can be collected and predicted with the help of this system.
References

	Building Better Batteries: Characterize Battery Parameters for Simulation (ansys.com)
	Li, Z., Shi, X., Shi, M., Wei, C., Di, F., & Sun, H. (2020). Investigation on the Impact of the HPPC Profile on the Battery ECM Parameters’ Offline Identification. 2020 Asia Energy and Electrical Engineering Symposium (AEEES), 753–757. https://doi.org/10.1109/AEEES48850.2020.9121487
	Vilsen, S. B., & Stroe, D.-I. (2021). Battery state-of-health modelling by multiple linear regression. Journal of Cleaner Production, 290, 125700. https://doi.org/10.1016/j.jclepro.2020.125700
	Yang, H., Cao, Y., Xie, H., Shao, S., Zhao, J., Gao, T., Zhang, J., & Zhang, B. (2020). Lithium-ion Battery Life Cycle Prediction with Deep Learning Regression Model. 2020 IEEE Applied Power Electronics Conference and Exposition (APEC), 3346–3351. https://doi.org/10.1109/APEC39645.2020.9124049
	Jin, S., Sui, X., Huang, X., Wang, S., Teodorescu, R., & Stroe, D.-I. (2021). Overview of Machine Learning Methods for Lithium-Ion Battery Remaining Useful Lifetime Prediction. Electronics, 10(24), 3126. https://doi.org/10.3390/electronics10243126
	Man-Fai Ng ; Jin Zhao ; Qingyu Yan ; Gareth J. Conduit ; Zhi Wei Seh - Predicting the Current and Future State of Batteries using Data-Driven Machine Learning - Nature Machine Intelligence 
	Ardeshiri, R. R., Balagopal, B., Alsabbagh, A., Ma, C., & Chow, M.-Y. (2020). Machine Learning Approaches in Battery Management Systems: State of the Art: Remaining useful life and fault detection. 2020 2nd IEEE International Conference on Industrial Electronics for Sustainable Energy Systems (IESES), 61–66. https://doi.org/10.1109/IESES45645.2020.9210642
	P. P. L. Regtien; H. J. Bergveld; Dmitry Danilov; Valer Pop - Battery Management Systems: Accurate State-of-Charge Indication for Battery-Powered Applications - ISBN: 978-1-4020-6944-4
	Niraj Agarwal; Phulchand Saraswati; Ashish Malik; Yogesh Bateshwar - Design a Battery Monitoring System for Lead-Acid Battery - International Journal of Creative Research Thoughts (IJCRT)
	Lelie, M., Braun, T., Knips, M., Nordmann, H., Ringbeck, F., Zappen, H., & Sauer, D. (2018). Battery Management System Hardware Concepts: An Overview. Applied Sciences, 8(4), 534. https://doi.org/10.3390/app8040534

