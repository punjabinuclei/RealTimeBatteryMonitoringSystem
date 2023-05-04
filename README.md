# **Real Time Battery Monitoring System USing MAchine Learning and Deep Learning**  

# **Abstract**

Every battery-operated device, including electric cars, smartphones, drones, etc., typically has a battery monitoring system (BMS) attached. This system's primary responsibility is to control battery levels and keep track of a battery's State of Charge and State of Health. These systems currently rely on the Kalman Filter, Coulomb Counting, and Voltage Measurement to estimate the state of charge, but these systems have some limitations. A thorough literature review revealed that the traditional systems' hysteresis—a condition in which a system's output is delayed and causes a certain amount of measurement error—can affect the performance of current algorithms. Additionally, these hardware circuits can now use sensors to capture the dynamic environment of the real-world condition. Because heat has a major impact on battery capacity, temperature of a battery is a crucial parameter that is neglected in traditional methods. This project focuses on a thorough analysis of 9 regression algorithms based on the accuracy of the results and execution time of the algorithms to get faster predictions. From this analysis, Extreme Gradient Boosting was found to be the robust algorithm providing the accurate results in less than few seconds, which is what machine learning is used for.  Following this, the model was implemented on an in-house hardware system made with the aid of sensors and microcontrollers. Utilizing three evaluation metrics, including RMSE, MAE, and R-Squared Error, the analysis was conducted on two distinct datasets to better capture the nonlinearity in the data set. Additionally, the circuit was tested on a drone with a single motor, two motors, and then three motors, and data was collected to simulate the conditions in real life. The results of using these data to train and implement the online prediction were quite promising. The results were subsequently examined in order to determine the degree of error for various charging states as well as the lack of training datasets. The errors were quite high at certain charging levels. However, there is always room for improvement.   **Keywords:** Machine Learning, Deep Learning, Neural Networks, Battery Monitoring System, State of Charge, Evaluation Metrics, Coulomb Counting

# **Acknowledgement**

We want to sincerely thank everyone who helped finish this report by expressing my gratitude. First of all, we want to express my gratitude to Dr. Jagat Rath (Assistant Professor, Department of Mechanical and Aero-Space Engineering (IITRAM)) my supervisor, for their direction, encouragement, and feedback throughout the project. Their knowledge and opinions were extremely helpful in determining the project’s course.

Additionally, we want to thank Dr. Ajit Kumar for his assistance and insightful criticism. Their suggestions and insights helped the report's quality. We also want to be recognized for our efforts due to the dedication to the project and careful research that contributed to its completion.

Finally, we would like to express our gratitude to IITRAM, Ahmedabad, for giving us this wonderful opportunity and resources as well as to all of our friends who contributed significantly to the success of this project.

**Tathya Bhatt**

**Gurpreet Singh**

Department of Mechanical and Aerospace Engineering

IITRAM, Ahmedabad

# **List of Figures**

[Figure 1.1 - Voltage Region. 13](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007902)

[Figure 1.2 - SOH Visualization. 14](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007903)

[Figure 1.3 - Architecture of a typical BMS. 15](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007904)

[Figure 1.4- Application Areas. 16](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007905)

[Figure 3.1 - Visualization of OLS. 32](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007906)

[Figure 4.1 - Feature Selection Example. 43](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007907)

[Figure 5.1 - Feature Correlation Heatmap. 47](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007908)

[Figure 5.2 - RMSE Histogram of 80:20 Ratio. 51](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007909)

[Figure 5.3 - RMSE Histogram of 60:40 Ratio. 51](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007910)

[Figure 5.4 - RMSE of 70:30 Ratio. 52](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007911)

[Figure 5.5 - Mean MAE Bar Chart 52](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007912)

[Figure 5.6- Mean RMSE Bar Chart 52](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007913)

[Figure 5.7 - Cycle Radar Charts. 54](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007914)

[Figure 5.8 - Time vs Algorithms. 55](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007915)

[Figure 6.1 - Real Life Module. 59](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007916)

[Figure 6.2 - Schematic Circuit 59](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007917)

[Figure 8.1 - Pi's GPIO Pins. 64](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007918)

[Figure 8.2 - ADS1115 with Pi 65](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007919)

[Figure 8.3 - Real vs Predicted SOC at Cruise Condition. 67](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134007920)

# **List of Tables**

[Table 2.1 - Review 1. 17](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008689)

[Table 2.2 - Review 2. 18](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008690)

[Table 2.3 - Review 3. 18](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008691)

[Table 2.4 - Review 4. 19](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008692)

[Table 2.5 - Review 5. 20](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008693)

[Table 2.6 - Review 6. 20](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008694)

[Table 2.8 - Review 7. 21](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008695)

[Table 2.7 - Review 8. 21](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008696)

[Table 2.9 - Review 9. 22](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008697)

[Table 2.10 - Review 10. 22](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008698)

[Table 2.11 - Review 11. 23](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008699)

[Table 2.12 - Review 12. 23](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008700)

[Table 2.13 - Review 12. 24](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008701)

[Table 2.14 - Review 14. 24](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008702)

[Table 2.15 - Review 15. 25](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134008703)

**Table of Contents**

**[Abstract** iv](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009547)

**[Acknowledgement** v](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009548)

**[List of Figures**. vi](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009549)

**[List of Tables**. vii](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009550)

**[Chapter 1 Introduction**. 1](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009551)

**[1.1 Battery Management System**.. 1](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009552)

**[1.2 Temperature Acquisition**. 2](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009553)

**[1.3 Voltage Acquisition**. 3](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009554)

**[1.4 Current Acquisition**. 3](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009555)

**[1.5 Terminologies**. 4](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009556)

**[1.6 Working of a BMS System**.. 5](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009557)

**[1.7 Applications of a BMS**. 6](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009558)

**[Chapter 2 Methodology**. 7](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009559)

**[2.1 Literature Review**.. 7](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009560)

**[2.2 Problem Statement** 15](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009561)

**[2.3 Objectives**. 15](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009562)

**[2.4 Procedure**. 16](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009563)

**[Chapter 3 Overview of machine learning**. 18](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009564)

**[3.1 Choice of model** 19](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009565)

**[3.2 Basic Regression Working**. 19](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009566)

**[3.2.1**  **Line of Best Fit** 20](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009567)

**[3.2.2 Bias**. 20](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009568)

**[3.2.3 Variance**. 21](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009569)

**[3.2.4 Cost Function**. 21](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009570)

**[3.2.5 Gradient Descent** 22](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009571)

**[3.3 Models used in this study**. 22](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009572)

**[3.3.1 Ordinal Least Square Regression**. 22](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009573)

**[3.3.2 Decision Tree**. 23](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009574)

**[3.3.3 Random Forest** 24](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009575)

**[3.3.4 Gradient Boosting**. 24](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009576)

**[3.3.5 Extreme Gradient Boosting**. 25](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009577)

**[3.3.6 Neural Network**. 25](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009578)

**[3.3.7 Deep Neural Networks**. 26](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009579)

**[3.3.8 Support Vector Machine (SVM Linear Kernel)** 26](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009580)

**[3.3.9 Support Vector Machine Radial Basis Function**. 27](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009581)

**[3.4 Rationale behind these model selection**. 27](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009582)

**[Chapter 4 Dataset** 29](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009583)

**[4.1 LG 18650HG2 Li-ion Battery Data**. 29](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009584)

**[4.2 Selecting an alternative dataset** 29](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009585)

**[4.3 eVTOL Dataset** 30](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009586)

**[4.4 Data Selection**. 32](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009587)

**[4.5 Feature Engineering**. 32](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009588)

**[4.6 Normalization**. 34](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009589)

**[Chapter 5 Comprehensive Analysis**. 36](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009590)

**[5.1 Data Splitting & Training Ratios**. 36](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009591)

**[5.1.1 Training Ratio**. 36](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009592)

**[5.1.2 Feature Correlation**. 37](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009593)

**[5.2 Evaluation Metrics**. 38](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009594)

**[5.2.1 Root Mean Squared Error (RMSE)** 38](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009595)

**[5.2.2 R-Squared Error**. 39](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009596)

**[5.2.3 Mean Absolute Error (MAE)** 39](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009597)

**[5.3 Results**. 40](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009598)

**[5.3.1 R-Squared Comparison of models with & without features (60:40)** 40](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009599)

**[5.3.2 RMSE Comparison of 80:20, 70:30, and 60:40 training ratios with features**. 40](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009600)

**[5.3.3 Choosing 5 algorithms by comparing their MAE and RMSE**.. 42](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009601)

**[5.3.4 Choosing 3 algorithms by individual cycle study of five conditions each**. 43](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009602)

**[5.3.5 Execution Time Analysis of top three algorithms**. 45](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009603)

**[Chapter 6 BMS Module**. 46](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009604)

**[6.1 Hardware Requirements**. 46](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009605)

**[6.1.1 Voltage Sensor – (Voltage Detection Sensor Module 25V )**. 46](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009606)

**[6.1.2 Current Sensor (ACS712)** 46](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009607)

**[6.1.3 Temperature Sensor (LM35)** 47](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009608)

**[6.1.4 Lemon 1800mAh 3S 25C Lithium Polymer Battery**. 47](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009609)

**[6.1.5 Microprocessor (Raspberry Pi 4**) 47](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009610)

**[6.1.6 Power Distribution Board (PDB-XT60)** 48](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009611)

**[6.1.7 ADC Converter (ADS1115)** 48](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009612)

**[6.2 Module Circuit** 48](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009613)

**[Chapter 7 Data Collection & Results**. 50](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009614)

**[7.1 Data Collection using single motor**. 50](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009615)

**[7.2 Data Collection for two & three motor runs**. 50](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009616)

**[7.3 Noise**. 51](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009617)

**[7.4 Gaussian Noise**. 52](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009618)

**[7.5 Evaluation Results**. 52](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009619)

**[Chapter 8 Real-time Interfacing**. 54](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009620)

**[8.1 I2C Communication**. 54](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009621)

**[8.2 ADS1115 with Raspberry PI and Display**. 55](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009622)

**[8.3 Code Explanation**. 56](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009623)

**[8.4 Results**. 56](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009624)

**[Chapter 9 Conclusion and Future Work**. 58](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009625)

**[9.1 Conclusion**. 58](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009626)

**[9.2 Future Work**. 59](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009627)

**[Bibliography**. 59](notion://www.notion.so/fd443cef69e444818844ac12fba227e7#_Toc134009628)

# **Nomenclature**

|  | mean of the dependent variable known as ‘label’ |
| --- | --- |
|  | the mean values of independent variables known as ‘features’ |
|  | intercept |
| V | Voltage |
| n | Cycle Number |
| Wh | Energy Charge/Discharge |
| mAh | QDischarge/QCharge |
| ℃ | Temperature |
| mA | Current |
| s | Time |

# **Chapter 1 Introduction**

Lithium-ion batteries are now employed in a wide range of applications, from personal electronic gadgets like cell phones to the rising class of electric vehicles. Because these batteries are more vulnerable than lead-acid or NiCd batteries, they require more sophisticated monitoring to ensure safe operation.

The EV sector is experiencing a surge in demand for an effective battery management system, but this requires initial battery monitoring. In India, we can see an exponential increase in the number of electric Rickshaws that use lead acid batteries rather than more efficient lithium-ion batteries. Because the cost of a lead acid battery is significantly lower than that of a lithium-ion battery, it is critical to develop a battery monitoring and management system for lead acid batteries.

These lead acid batteries perform well at room temperature but poorly at lower temperatures. The existing technology is not adaptive to changing air conditions, and in a country like India, temperature plays a vital part in determining battery performance because temperatures here can reach 51.0 °C.

## **1.1 Battery Management System**

The basic task of a Battery Management System (BMS) is to ensure that optimum use is made of the energy inside the battery powering the portable product and that the risk of damage to the battery is prevented. This is achieved by monitoring and controlling the battery’s charging and discharging process.

In general, the BMS consists of the following functionalities

- Sensing Functionalities
    - Current
    - Voltage
    - Temperature
- Protection Functionalities
    - Short circuits
    - Over voltage, current and temperature
    - Disconnecting a faulty cell
- Estimation
    - State of charge
    - State of health

As well as data communication between BMS master module and BMS acquisition modules as well as battery pack and surrounding applications

## **1.2 Temperature Acquisition**

One of the most difficult jobs when developing a BMS is determining the most precise temperature achievable. Not only must the pros and disadvantages of the different available sensor types (completely digital interface or analogue) be considered, but also where to measure the temperature of the pack. As a result, the needed number of cell temperature sensors is determined. Simulations may be required to determine the best placement for a limited number of sensors. When conceptualizing a battery pack optimized for light weight, hefty copper busbars must be avoided as much as possible, forcing the design engineer to address possible thermal peaks during high power operation, necessitating thermal monitoring of busbars as well.

A temperature requirement must, in general, address three use cases: charging, discharging, and storage. Batteries based on lithium cannot function adequately in extreme temperatures. Even within these constraints, though, accurate temperature readings are critical. At too high current rates, the significant effect of lithium plating can occur in the usual temperature range. Temperature, voltage, and current must be accurately measured to avoid lithium plating. Battery cells have a high thermal capacitance and strong thermal conductivity (in particular geometric routes), which are influenced and limited by thermal isolation boundary layers (housing, geometry of cells, etc.). If temperature sensors are not set properly, misreading’s and thermal blind spots can occur.

## **1.3 Voltage Acquisition**

Figure 1.1 - Voltage Region

---

A traditional lithium-ion battery management system must include at least one voltage acquisition channel per serially connected cell. Specific charging profiles are required for various battery chemistry to improve performance and prevent safety hazards during charge. Almost all Li-ion battery chargers use a constant current/constant voltage charging strategy in general. Once the charger enters constant voltage mode, it is critical to ensure that the charge does not exceed the maximum level permitted in order to prevent exposing them to overcharge circumstances, which can cause excessive internal temperature rise and early failure. Rechargeable lithium ion battery cells can safely run at 2.75V per cell. However, if an unprotected lithium cell is discharged over the minimum voltage level, the cell may be damaged, resulting in decreased cycle life, unpredictable voltage characteristics, and enlargement of cells due to internal chemical reaction.

## **1.4 Current Acquisition**

Current sensors, in addition to being imperfect systems, suffer from drift, offset, and temperature inaccuracy. Furthermore, the current sensors that are used frequently must meet contradictory requirements at the same time: it is not uncommon for current sensors in automotive applications to be able to measure currents starting in the milliampere range while also being able to measure currents up to 1000 Ampere. Depending on the application, the sensor might need to have a high bandwidth to capture fast current changes. Furthermore, the existing sensor's precision and immunity to EMI noise should be evaluated. 

## **1.5 Terminologies**

In addition to being non-ideal systems, current sensors are also subject to a certain amount of drift, offset, and temperature inaccuracy. In addition to this, the present sensors that are employed often have to fulfil contradictory requirements at the same time:

Figure 1.2 - SOH Visualization

---

State-of-Charge (SoC) - State-of-Charge is the percentage of the maximum possible charge that is present inside a rechargeable battery. The SoC indication involves battery measurements and modelling . As a simple example the battery voltage (V) can be measured and the V-SoC relationship can be stored in a look-up table function in a microcontroller.

State-of-Health (SoH) – State of Health is a ‘measure’ that reflects the general condition of a battery and its ability to deliver the specified performance in comparison with a fresh battery. The State-of-Health (SoH) is an indication of the point that has been reached in the battery’s life cycle and is a measure of its condition relative to a fresh battery. The SoH indication may involve for example cycle-counting. In the simplest case the number of full charge/discharge cycles (Cn) can be counted and the SoH can be calculated on the basis of a stored maximum capacity-Cn function

The remaining run-time (tr) is the estimated time that the battery can supply current to a portable device under valid discharge conditions before it will stop functioning. The remaining run-time can be inferred from the remaining capacity in two ways, depending on the type of load: in the case of a current-type load the remaining capacity in mAh, so expressed as charge, is divided by the drawn current in mA and in the case of a power-type load the remaining capacity in mWh, so expressed as energy, is divided by the drawn power in mW.

## **1.6 Working of a BMS System**

The battery management system monitors individual cells in the battery pack. It then calculates how much [current](https://battlebornbatteries.com/what-are-amps/) can safely go in and come out without damaging the battery. The current limits prevent the source and the load from overdrawing or overcharging the battery. This protects the battery pack from cell voltages getting too high or low, which helps increase the battery’s longevity.

The BMS also monitors the remaining charge in the battery. It continually tracks the amount of energy entering and exiting the battery pack and monitors cell voltages. It uses this data to know when the battery is drained and shut the battery down.

Figure 1.3 - Architecture of a typical BMS

---

Following data capture, the data is routed via the necessary components in order to complete the appropriate activities via the Control Area Network Network.

## **1.7 Applications of a BMS**

Battery monitoring systems are used in a variety of applications where the performance and health of a battery are critical. Some common examples include in electric vehicles, renewable energy systems (such as solar and wind power systems), and backup power systems (such as in hospitals and data centers). Battery monitoring systems can also be used in consumer electronics, such as smartphones and laptops, to provide users with information about the battery life and health of their devices.

Figure 1.4- Application Areas

1. Determining the state of charge in electric vehicles and autonomous vehicles
2. Maintaining the temperature of a charger
3. Battery monitoring of a multicopters and drones
4. BMS is used in service robots
5. Small sized power tools using DC motors require BMS for the users safety
6. Wearables also use BMS
7. Home appliances operated with battery need a good BMS

# **Chapter 2 Methodology**

## **2.1 Literature Review**

Table 2.1 - Review 1

Table 2.2 - Review 2

Table 2.3 - Review 3

Table 2.4 - Review 4

Table 2.5 - Review 5

Table 2.6 - Review 6

Table 2.7 - Review 8

---

Table 2.8 - Review 7

Table 2.9 - Review 9

Table 2.10 - Review 10

Table 2.11 - Review 11

Table 2.12 - Review 12

Table 2.13 - Review 12

Table 2.14 - Review 14

Table 2.15 - Review 15

## **2.2 Problem Statement**

The majority of battery monitoring systems in use today rely on hardware circuits and techniques to measure current, voltage, and ultimately state of charge (SOC). The temperature of the surrounding environment, which is crucial for estimating the battery's runtime accurately, is not taken into account by these methods. Hysteresis, which is a condition in which there is a delay in a system's output and results in a certain amount of error in measurements, can affect current algorithms (such as Coulomb Counting and the Voltage Method). Accuracy suffers because the effects of ageing batteries are not taken seriously..

## **2.3 Objectives**

In this day and age of artificial intelligence, there are very few BMS systems that are based on machine learning.

1. One of the best solutions to overcome the challenges that were mentioned is to use a data driven approach in order to be efficient and accurate. In order to achieve the best possible outcome, it is necessary to investigate the various approaches to machine learning and to identify the method that is most effective.
2. Additionally, it is necessary to take into account the impact of the temperature of the battery. An enormous quantity of data sets needs to be gathered at a variety of temperature extremes, and on the basis of those data sets, with the assistance of machine learning, a successful model needs to be developed.
3. Making a BMS system using sensors and microcontrollers to get the required amount of data to train the model.
4. Another objective is the Real time implementation of the desired algorithm on this BMS System on a drone.

## **2.4 Procedure**

1. *To develop a battery monitoring hardware system*  A microcontroller such as an Arduino or a Raspberry Pi to collect and process data from  the battery; a voltage measurement device, such as a voltage divider or a voltage sensor,  to measure the battery's voltage; a current measurement device, such as a current shunt or a current sensor, to measure the battery's current; a display, such as an LCD screen or an OLED screen, to display the battery's voltage, current, and any other pertinent information; a power This will enable the microcontroller to measure the voltage of the battery. Connect the device for measuring current to the battery and microcontroller. This will enable the microcontroller to measure the current of the battery. Establish a connection between the display and the microcontroller. This will allow the microcontroller to display  the battery's voltage, current, and other pertinent information. Programming the microcontroller to collect data from the voltage and current measurement devices and display it on the displayThe code for the microcontroller can be written using a programming language, such as C or Python.Verify the functionality of the battery monitoring hardware by  performing a series of tests. This can be accomplished by measuring the voltage and current of the battery and comparing the displayed values to the actual values.
2. *Testing the hardware system*  First of all, ensuring that the BMS hardware system is properly installed and connections are valid. Next, power on the system and verify that every component is operating properly. This can be accomplished by manually inspecting each component or by employing diagnostic software to perform a system test. Once confirmed that all of the system's components are functioning properly, you can begin performance testing. This can be accomplished by simulating different operating conditions, such as temperature and load scenarios, and observing the system's response. As you test the system, be aware of any errors or malfunctions that may occur and make a note of any problems you encounter. You can then use this data to troubleshoot and resolve any potential issues. After a system has been thoroughly tested, it is essential to perform routine maintenance and inspections to ensure that it continues to operate properly over time. This may involve routinely inspecting and replacing components, as well as performing periodic diagnostic tests to ensure the optimal operation of the system.  
3. *Select a Machine Learning Algorithm with necessary requirements*  When selecting a machine learning algorithm for a specific task, numerous considerations must be taken into account. Consider the type of data you have access to, the nature of the problem you are attempting to solve, and the objectives you wish to accomplish. The following steps will assist you in selecting an appropriate machine learning algorithm: Define the problem you are attempting to solve and the type of machine learning problem you must address (e.g. classification, regression, clustering, etc.). Comprehend the various types of algorithms and their respective strengths and weaknesses. Certain types of problems or data are better suited to particular algorithms than others. Think about the quantity and quality of your data. Some algorithms require a large amount of training data, while others can function with a smaller amount. Using metrics such as accuracy, precision, and recall, evaluate the performance of different algorithms on your data. Select the algorithm that performs the best on your dataset and aligns with your objectives. Noting that there is no one-size-fits-all solution for selecting a machine learning algorithm is crucial. The optimal algorithm for your problem will be determined by a number of variables and may require experimentation.
4. *Training and Testing the machine learning model*  Collect and prepare the training dataset: To begin, collect and prepare the training dataset. This requires cleansing the data, ensuring it is in a usable format, and separating it into training and validation sets. After selecting a model and preparing the training data, the model needs to be trained using the training data. This involves feeding the data into the model and adjusting the parameters of the model to minimize the error on the training data. Evaluate the model: After training the model, its performance on the validation data must be evaluated. This will provide insight into how well the model generalizes to new data. After evaluating the model, it may be necessary to fine-tune its parameters to improve its performance on the validation data. This may involve modifying the model's learning rate, regularization intensity, or other hyperparameters. Finally, test the model on a held-out test set to determine how well it performs on unseen data. This will provide a final estimate of the performance of the model.

# **Chapter 3 Overview of machine learning**

Machine learning is a subfield of artificial intelligence that employs algorithms and statistical models to enable a system's performance on a particular task to improve over time. Machine learning algorithms can make predictions, classifications, and decisions based on what they have learned from examples and data. Several tasks, including image and speech recognition, natural language processing, and predictive modelling, are amenable to machine learning. It is a rapidly expanding field that is utilized in numerous industries, including healthcare, finance, transportation, and retail.

Models for machine learning include supervised learning and unsupervised learning. Training a model on a labelled dataset in which the correct outputs are provided for each example in the training data constitutes supervised learning. The model uses this information to determine the relationship between input and output, and can then make predictions based on new, unobserved data. Regression and classification assignments are examples of supervised learning.

Unsupervised learning entails training a model with an unlabeled dataset in which the correct outputs are not provided. The model must self-learn to recognize patterns and structure in the data. Unsupervised learning includes tasks like clustering and dimensionality reduction.

## **3.1 Choice of model**

We choose supervised learning because the goal is to train a model to make predictions or decisions based on labeled training data. In supervised learning, the training data includes both the input features and the corresponding correct outputs. The model uses this information to learn the relationship between the input and the output, and can then make predictions on new, unseen data..

Regression models were implemented because the voltage, current and temperature are continuous variable, such as a price or a probability. They are frequently employed in applications where the objective is to comprehend the relationship between various variables and to make predictions based on this relationship. A regression model could be used, for instance, to predict the sale price of a house based on its size, location, and other characteristics.

## **3.2 Basic Regression Working**

Ordinary Least Squares (OLS) regression is a popular method for estimating the coefficients of linear regression equations that describe the relationship between one or more independent quantitative variables and a dependent variable (simple or multiple linear regression). Least squares represent the least squares error (SSE). In our case the model is multivariable regression which uses more than one variables as input to predict the output.

The governing equation behind the regression is to calculate the slope and coefficients of a linear equation

(1)

For two variables, the slope can be calculated by:

(2)

&   are the coefficients of the variables

=                                                                                                (3)

=                                                                                                (4)

(5)

(6)

(7)

(8)

(9)

here

= mean of the dependent variable known as ‘label’

&   are the mean values of independent variables known as ‘features’

is the intercept,   &   are the coefficients

### **3.2.1**  **Line of Best Fit**

The main purpose of the best fit line is that our predicted values should be closer to our actual or the observed values, because there is no point in predicting values which are far away from the real values. In other words, we tend to minimize the difference between the values predicted by us and the observed values, and which is actually termed as error.

### **3.2.2**  **Bias**

Figure 3.3 - Underfitting

---

Figure 3.2 - Bias

---

Figure 3.4 -Overfitting

---

Figure 3.1 - Linear regression of a 2d dataset

---

Bias is the difference between our actual and predicted values. Bias is the simple assumptions that our model makes about our data to be able to predict new data. When the Bias is high, assumptions made by the model are too basic, the model can’t capture the important features of the data. Thus the model hasn’t captured patterns in the training data and hence cannot perform well on the testing data too. This instance, where the model cannot find patterns in our training set and hence fails for both seen and unseen data, is called Underfitting.

### **3.2.3 Variance**

During training, it allows the model to ‘see’ the data a certain number of times to find patterns in it. If it does not work on the data for long enough, it will not find patterns and bias occurs. On the other hand, if the model is allowed to view the data too many times, it will learn very well for only that data. It will capture most patterns in the data,  but it will also learn from the unnecessary data present, or from the noise.

We can define variance as the model’s sensitivity to fluctuations in the data. Our model may learn from noise. This will cause our model to consider trivial features as important. For any model, we have to find the perfect balance between Bias and Variance. This just ensures that we capture the essential patterns in our model while ignoring the noise present it in. This is called Bias-Variance Tradeoff. It helps optimize the error in our model and keeps it as low as possible.

### **3.2.4 Cost Function**

After training the model, we need to check how well the model is performing. Hence, the function which corrects the model is required in order to get accuracy and make it the best trained model. A Cost Function is used to measure just how wrong the model is in finding a relation between the input and output. It tells us how badly the model is predicting.

Cost Function =                                                                                  (10)

### **3.2.5 Gradient Descent**

Gradient Descent is an algorithm that is used to optimize the cost function or the error of the model. It is used to find the minimum value of error possible in your model. Gradient Descent can be thought of as the direction one have to take to reach the least possible error. The error in the model can be different at different points, and a quickest method to reduce the computational efficiency needs to be found.

Figure 3.5 - Gradient Descent

---

Gradient Descent can be visualized as a ball rolling down a hill. Here, the ball will roll to the lowest point on the hill. It can take this point as the point where the error is least as for any model, the error will be minimum at one point and will increase again after that. In gradient descent, the error for individual input variables are found. This is repeated, and soon the error values keep getting smaller and smaller. Soon we can get the values for variables when the error is the least, and the cost function is optimized.

## **3.3 Models used in this study**

### **3.3.1 Ordinal Least Square Regression**

An approach to statistical regression known as ordinary least squares is used to forecast unknown values from a set of data. Ordinary Least Squares, or OLS, can be used, for instance, to predict shoe size from a data set that includes height and shoe size. Given the information, one can calculate a rate of change and predict shoe size based on a subject's height using the ordinary least squares formula. In essence, OLS creates a dependent variable from an input, the independent variable.

Figure 3.1 - Visualization of OLS

---

Using addition and multiplication, ordinary least squares combines the input, an independent variable, with additional variables known as betas. The slope of the function is determined by the first beta, abbreviated "beta_1". Essentially, it reveals what the output would be if the input were 0. The coefficient, or how much of a difference there is between increments in the independent variable, is represented by the second beta, designated as "beta_2" in the equation.

OLS determines the best slope for the data by using the errors, or the vertical separation between a data point and a regression line, to determine the betas. Finding the regression line by computing the squares of the errors is demonstrated in the image above. To find the smallest value for the sum of all squared errors, OLS squares the errors and locates the line that passes through the sample data.

### **3.3.2 Decision Tree**

A machine learning algorithm called decision tree regression employs a decision tree to forecast continuous numeric values. According to the values of the independent variables, the data is divided into smaller subsets, and these subsets are recursively split until the final prediction is reached. Each leaf node in the tree represents a predicted numerical value, and each internal node in the tree represents a decision based on the value of an independent variable.

The algorithm first chooses the variable that best splits the data based on a predetermined criterion, such as minimizing the sum of squared errors, before building a decision tree regression model. After dividing the data into two subsets based on the value of that variable, the algorithm repeats the process until the tree is fully formed. Based on the values of the independent variables, the final prediction for a new data point is made by moving up the tree from the root node to a leaf node.

In disciplines like finance, engineering, and environmental science, decision tree regression is a powerful tool for forecasting continuous numeric values. But it might be prone to overfitting and struggle with complicated data distributions. To increase the precision and generalizability of the model, it is crucial to carefully tune the hyperparameters of the algorithm and use the right regularization techniques.

### **3.3.3 Random Forest**

An ensemble of decision trees are used by the machine learning algorithm known as random forest to increase prediction accuracy. It functions by constructing numerous decision trees, each trained on a randomized subset of the training data and features. The algorithm then combines the individual trees' predictions to arrive at a final prediction.

Comparing a random forest to a single decision tree reveals several benefits. It can first handle many input variables and model intricate relationships between them. Second, because the randomness introduced by the random subsets reduces the correlation between the trees, it is less prone to overfitting than a single decision tree. The third benefit is that it can offer an estimation of the feature importance, which is helpful for comprehending the underlying data.

A versatile algorithm, random forest can be applied to both classification and regression tasks. It is widely used to forecast outcomes and highlight key elements in a variety of disciplines, including finance, healthcare, and environmental science. However, because there are so many trees involved, it might need more computational power than a single decision tree.

### **3.3.4 Gradient Boosting**

A predictive model created using the machine learning technique of gradient boosting is an ensemble of weak prediction models, typically decision trees. With gradient boosting, weak models are iteratively added to the ensemble, each one aiming to correct the flaws in the previous models. A simple initial model, like a decision tree, is typically used in the process. The algorithm then examines the mistakes made by the first model, focusing on those mistakes while training a new model. The algorithm then repeats the process, training a new model to concentrate on the mistakes made by the ensemble of the first two models before the second model is added. This keeps going until either the stopping criterion is satisfied, or the desired level of accuracy is attained.

Both regression and classification tasks can be accomplished using the potent technique of gradient boosting. It is frequently used to forecast outcomes and highlight crucial elements in industries like finance, healthcare, and marketing. If not carefully tuned, it can be prone to overfitting and may use more computing power than other algorithms.

### **3.3.5 Extreme Gradient Boosting**

Extreme Gradient Boosting (XGBoost) is an advanced implementation of gradient boosting that uses a combination of regularization techniques and parallel processing to enhance the performance and scalability of the algorithm.

Similar to conventional gradient boosting, XGBoost builds an ensemble of weak prediction models, typically decision trees, iteratively in order to boost the model's predictive performance. However, XGBoost makes use of a number of improvements to increase its strength and power. For example, XGBoost uses a technique called "gradient-based sampling" to select the most informative samples for each new model in the ensemble, which reduces the computational cost and improves the accuracy. To avoid overfitting and enhance the model's generalization capabilities, XGBoost also employs regularization methods like L1 and L2 regularization as well as dropout.

A wide variety of objective functions and evaluation metrics are supported by XGBoost, which can be easily customized. Additionally, it has a number of sophisticated features that can boost the algorithm's precision and effectiveness, including early stopping, cross-validation, and parallel processing. XGBoost has been widely used in various industries such as finance, healthcare, and e-commerce for predictive modeling, feature selection, and anomaly detection.

### **3.3.6 Neural Network**

A machine learning model called a neural network is based on the structure and operation of the human brain. It is made up of layers of interconnected nodes, or neurons, which cooperate to process input data and arrive at predictions or classifications. A single neuron serves as the fundamental building block of a neural network. It accepts one or more input values, applies a mathematical function to them, and outputs a value. Weighted connections, which regulate the strength of the signal passed between neurons, are used to link neurons to one another.

The neurons in a neural network with multiple layers are arranged in layers, with each layer processing the results of the layer before it. The raw input data is sent to the first layer, which is referred to as the input layer. One or more hidden layers take the output of the input layer and apply a number of nonlinear transformations to the data. The output layer—the top layer—is where the final predictions or classifications based on the transformed data are generated.

In order to reduce the error between the predicted output and the actual output, the weights of the connections between the neurons are changed during the training process. Usually, an optimization algorithm like gradient descent is used for this. Predictive modelling, speech and image recognition, natural language processing—there are many applications for neural networks. They can learn patterns and relationships in the data that may be challenging or impossible for a human to discern, making them particularly useful for tasks involving large amounts of complex data.

### **3.3.7 Deep Neural Networks**

A deep neural network is a kind of neural network with many layers of neurons in between the input and output layers. With each layer building on the features learned by the previous layer, these layers allow the network to learn progressively more complex representations of the data. Depending on how complex the problem being solved is, there can be a few, hundreds, or even thousands of layers in a DNN. A DNN has layers of interconnected neurons that process the input data, similar to a regular neural network in terms of its basic structure. DNNs can learn more complex patterns and relationships in the data because they have more layers and neurons per layer than regular neural networks.

The activation function employed controls the computations carried out by each neuron in a DNN. For the network to be able to learn complex relationships in the data, the activation function introduces nonlinearity into the model. The ReLU (Rectified Linear Unit) function, the sigmoid function, and the tanh (hyperbolic tangent) function are a few examples of common activation functions used in DNNs.

### **3.3.8 Support Vector Machine (SVM Linear Kernel)**

It is a supervised machine learning algorithm which can be applied to both classification and regression tasks. The objective of SVM in regression tasks is to learn a function that forecasts a continuous target variable's value based on a set of input features. The SVM algorithm looks for the hyperplane that maximizes the distance between the hyperplane and the nearest data points while best separating the data points in the feature space. The algorithm searches for the hyperplane that maximizes the margin between the hyperplane and the nearest data points when performing SVM regression with a linear kernel.

### **3.3.9 Support Vector Machine (Radial Basis Function)**

The kernel based on RBF is a common pick for SVMs because it is capable of recording nonlinear relationships between variables that are input and output. SVMs with RBF kernels are designed to find a function that can approximate the underlying relationship between input and output variables. In other words, given a set of labelled data, SVMs with RBF kernel seek the best function that can map the input data to the output data. The RBF kernel computes the similarity between input data points in a high-dimensional feature space, and SVMs use this similarity measure to learn a nonlinear function that can predict the output variable.

SVM performance with RBF kernel regression is affected by several factors, including the kernel parameters chosen, the size and quality of the training data, and the complexity of the underlying relationship between the input and output variables. To achieve optimal performance, SVMs with RBF kernels can be computationally expensive to train and may require tuning of the kernel parameters.

## **3.4 Rationale behind these model selection**

For this project, as we need to predict the continuous output variable i.e State of Charge, supervised machine learning regression models which implement a mathematical function or model that can predict the output variable accurately for new, unknown input data. This is accomplished by training the model on a labelled dataset of input-output pairs with continuous output values.

As a part of our comprehensive analysis, we wanted to test every regression models’ results in the analysis so that a proper more firm understanding can be built with this analysis. So we’ve analyzed these nine models which best suits our problem statement of supervised learning based on the labeled dataset.

# **Chapter 4 Dataset**

## **4.1 LG 18650HG2 Li-ion Battery Data**

This project requires the dataset consisting of temperature, current, battery capacity and voltage data because these variables are the sole support for machine learning models without which the models will fail to predict the output. So at first LG 18650HG2 Li-ion Battery Data is used to train the model. The dataset was collected using HPPC Tests (Hybrid Pulse Power Characterization) performed at McMaster University in Hamilton, Ontario, Canada by Dr. Phillip Kollmeyer.A brand new 3Ah LG HG2 cell was tested rigorously and A series of tests were performed at different temperatures (10℃, 25℃, 40℃) and the battery was charged after each test at 1C rate to 4.2V.

## **4.2 Selecting an alternative dataset**

Our objective was to make a robust system which should reduce the overall cost of the BMS system. Currently BMS systems have complex circuits which has a huge impact on its costs. By incorporating data driven methods and using a microprocessor we are aiming to make it robust system which can predict the charging state accurately with different operating conditions.

Previously we had tried estimating the State of Charge with an LG Battery dataset at different temperatures but there were certain problems

- The results with these dataset were similar irrespective of the algorithm choices. With further rumination it was found that the dataset of each cycle was quite linear which won’t be helpful for the models as it will be easier for them to train and predict with higher accuracy.
- Secondly, This dataset had a lot less data which cant be used in real life accurate predictions and furthermore data driven approaches provides the best results when a large amount of dataset is available and trained.
- Moreover, in ML, Features play an important role in improving models performance and thus including more features can impact the models accuracy which was not there in the previous dataset.
- The results of the experiments were on the same training ratio which was 75:25 and with only 3 regression-based algorithms. This was not enough and won't justify the overall algorithm selection and performance.

Thus we found another dataset which could provide a more robust and accurate predictions.

## **4.3 eVTOL Dataset**

The eVTOL (Electric Vertical Take-Off and Landing) Battery Dataset is a freely accessible dataset containing sensor measurements of battery voltage and current during flights of a small electric vertical take-off and landing aircraft (eVTOL). Researchers at Carnegie Mellon University's Robotics Institute gathered the data, which was released in 2021. Battery used was – Sony  Murata 18650 VTC – 6Cell. The data collection was authored by Alexander Bills, Venkatasubramaniam Vishwanathan, Shashank Sripad, Evan Frank, Devin Charles, William Leif Fredericks is used to train the model. Each file consisted these variables

- Temperature (℃)
- Time (s)
- Cell Voltage (V)
- Current (mA)
- QCharge (mAh)
- Energy Discharge (Wh)
- QDischarge (mAh)
- Energy Charge (Wh)
- Cycle Number (n)

The folder consists of around 22 csv files at different conditions of eVtol usage. Each file contains data from experimental testing performed on a single cell over the course of that cell's life.

Conditions –

VAH01.csv: Baseline

VAH02.csv: Extended cruise (1000 sec)

VAH05.csv: 10% power reduction during discharge (flight)

VAH06.csv: CC charge current reduced to C/2

VAH07.csv: CV charge voltage reduced to 4.0V

VAH09.csv: Thermal chamber temperature of 20 degrees C

VAH10.csv: Thermal chamber temperature of 30 degrees C

VAH11.csv: 20% power reduction during discharge (flight)

VAH12.csv: Short cruise length (400 sec)

VAH13.csv: Short cruise length (600 sec)

VAH15.csv: Extended cruise (1000 sec)

VAH16.csv: CC charge current reduced to 1.5C

VAH17.csv: Baseline

VAH20.csv: Charge current reduced to 1.5C

VAH22.csv: Extended cruise (1000 sec)

VAH23.csv: CV charge voltage reduced to 4.1V

VAH24.csv: CC charge current reduced to C/2

VAH25.csv: Thermal chamber temperature of 20 degrees C

VAH26.csv: Short cruise length (600 sec)

VAH27.csv: Baseline

VAH28.csv: 10% power reduction during discharge (flight)

VAH30.csv: Thermal chamber temperature of 35 degrees C

## **4.4 Data Selection**

Out of these 22 conditions, fives different conditions’ data was taken into the analysis namely

- VAH01: Baseline Condition
- VAH02:Extended Cruise
- VAH05: 10% power reduction during discharge (flight)
- CV charge voltage reduced to 4.0V
- VAH09: Thermal chamber temperature of 20 degrees C.

Every condition had numerous cycle iterations and from these we considered five cycle’ analyses for our model training. Then each model was studied for five cycles to make the analysis robust in different conditions and three evaluation metrics were compared.

## **4.5 Feature Engineering**

Features are the input variables that we provide to our machine learning models. Each column within the dataset represents a feature. To train an optimal model, we must utilize only the most important features. If there are too many features, the model may learn from noise and capture unimportant patterns. Feature Selection refers to the process of selecting the most relevant data parameters. To train a model, we collect massive amounts of data to help the machine learn more effectively. Typically, a significant portion of the data collected is noise, and certain columns of our dataset may not significantly contribute to the performance of our model. In addition, having a large amount of data can slow down the training process and result in a slower model. The model may also be inaccurate if it learns from irrelevant data. Feature selection is what distinguishes high-quality data from the rest. Given the same model and computational resources, why do some competitors with faster and more accurate models win competitions? The correct response is Feature Selection. In addition to selecting the appropriate model for our data, we must also select the appropriate data for our model.

Feature Selection is the method of reducing the input variable to your model by using only relevant data and getting rid of noise in data.

Figure 4.1 - Feature Selection Example

Thus, in order to create a robust algorithm for our BMS System, we added several features which can help to train the model better. Machine learning (ML) relies heavily on statistical features to quantify and summarize the characteristics of the data. The development of ML models can be influenced by statistical features, which offer a way to analyze and comprehend data patterns.

We can identify significant patterns and characteristics of the electrical system under analysis by adding statistical features of mean, median, variance, and standard deviation to current, voltage, and temperature data using a sliding window technique with a window size of 10. Using the sliding window technique, data is divided into overlapping windows, and statistical features are computed for each window. This method can be helpful for tasks like fault detection, anomaly detection, or system optimization because it can help to capture local patterns in the data.

In comparison to larger window sizes, which might miss significant changes or trends in the data, we are able to gather information about the electrical system at a more granular level when using a window size of 10. Additionally, the use of statistical features like mean, median, variance, and standard deviation can give important information about the distribution, variability, and central tendency of the data for current, voltage, and temperature. We can increase the precision and performance of our predictions or classifications by incorporating these statistical features into our machine learning models.

Power, resistance, conductance, and temperature change have all been calculated from the input variables in addition to the statistical features of mean, median, variance, and standard deviation of current, voltage, and temperature data using a sliding window technique. These characteristics can offer more information about how the electrical system behaves and can be applied to the creation of machine learning models that are more precise and efficient.

Features:

| ·       Mean Temperature | ·       Variance of Voltage |
| --- | --- |
| ·       Mean Current | ·       Standard Deviation of Current |
| ·       Mean Voltage | ·       Standard Deviation of Voltage |
| ·       Median Temperature | ·       Standard Deviation of Temperature |
| ·       Median Voltage | ·       Power |
| ·       Median Current | ·       Resistance |
| ·       Variance of Current | ·       Conductance |
| ·       Variance of Temperature | ·       Temperature Change
 
 |

## **4.6 Normalization**

To transform the data into a standard format and increase the model's accuracy and performance, normalization is a crucial data preprocessing technique in machine learning. The input data is scaled to a standard range, such as between 0 and 1 or -1 and 1, as part of the normalization process. The Min-Max Scaler is a popular normalization technique that scales the data to a particular range by taking away the minimum value and dividing it by the data range. The performance of the machine learning model can be impacted by problems like data skewness, outliers, and different units of measurement. This is why normalization is crucial. Different scales or ranges in the input data may cause the model to prioritize some features over others, which may result in skewed or incorrect predictions. Normalization makes sure that each feature is given the same weight and can help the model learn from the data.

A popular normalization method is the Min-Max Scaler because it is straightforward, simple to use, and has minimal impact on the data's shape or distribution. The procedure involves dividing by the data range and subtracting the minimum value of each feature (i.e., the maximum value minus the minimum value). This guarantees that all features are weighted equally in the model and scaled to the same range.

(10)

# **Chapter 5 Comprehensive Analysis**

## **5.1 Data Splitting & Training Ratios**

The greatest challenge for ML/DL practitioners is determining how to divide data for training and testing. Although it initially appears to be a simple problem, its complexity can only be determined by delving deeper into it. Inadequate training and testing sets can have unpredictable effects on the model's output. It may result in overfitting or underfitting of the data, causing our model to produce biased outcomes.

Training Set - The data which will be fed into the model will be contained within the train set. Simply put, our model would gain knowledge from this data. For instance, a Regression model would use these examples to identify gradients in order to decrease the cost function. Then, these gradients will be utilized to reduce costs and accurately predict data.

Testing Set - The test set consists of the data used to evaluate the trained and validated model. It tells us how efficient our overall model is and the likelihood that it will predict something illogical. Numerous evaluation metrics (such as precision, recall, and accuracy, etc.) can be used to measure the performance of our model.

### **5.1.1 Training Ratio**

The term "training ratio" describes the ratio between the amount of data used to train a machine learning model and the amount used to test or validate the model. Usually expressed as a percentage, the training ratio has typical values between 60 and 80% for training and 20 to 40% for testing or validation.

The performance and accuracy of the model are directly impacted by the training ratio, which is crucial in machine learning. The model may not be able to recognize the underlying patterns and relationships in the data if the training ratio is too low. It may also be vulnerable to overfitting, in which case the model memorizes the training data but performs poorly on new, untried data. On the other hand, if the training ratio is too high, the model might underfit, where it is too simple and fails to adequately represent the complexity of the data, and it might also have trouble generalizing to new data.

Thus, for this comprehensive analysis, three training ratio’s 60:40, 70:30, and 80:20 were selected accordingly because only then it will help to understand how the model behaves with different amount of training dataset.

### **5.1.2 Feature Correlation**

The correlation between two or more variables is found using heatmaps. High correlation between two or more features in a dataset can hinder a model's capacity to learn and make reliable predictions.

A model may be less able to generalize to other datasets with different correlations between the features if it was trained on a dataset with correlated features.

Figure 5.1 - Feature Correlation Heatmap

---

## **5.2 Evaluation Metrics**

A machine learning model's effectiveness and accuracy are assessed using evaluation metrics. These metrics are crucial for evaluating the model's effectiveness and pinpointing potential areas for improvement. Depending on the task and model objectives, a variety of evaluation metrics can be used in machine learning.

### **5.2.1 Root Mean Squared Error (RMSE)**

The most widely used metrics when dealing with regression issues is root mean squared error.The standard deviation of prediction errors serves as the definition of RMSE. These error predictions are sometimes referred to as residuals. In essence, residuals are a measurement of how far data points are from the regression line.

(1)

Where: Σ – Summation

– Predicted Values

– Original Values

N – Number of Observations

The concentration of data points around the regression line is described by RMSE. It is assumed that residuals in RMSE follow a normal distribution and are unbiased. The model performs better at prediction the lower the RMSE value. A model with an RMSE of 0 is the ideal predictor, and a model with a value of 1 is the worst. A small RMSE indicates that the predictions are close to the actual values. A large RMSE indicates that the predictions are far from the actual values.

RMSE is sensitive to outliers, meaning that it penalizes large errors more heavily than smaller ones. This can be useful in situations where large errors are particularly problematic. It can be used for most of the models.

### **5.2.2 R-Squared Error**

R squared is a statistical indicator of how closely the data point fits the regression line. As the coefficient of determination, it has additional names. R-Square is calculated by dividing the variance that is explained by the linear model by the total variance .R-squared value always ranges from 0% to 100%, so 0% denotes that there is no variability in the response data around its mean and 100% denotes that the model fully accounts for all such variability. This demonstrates how much more accurate your model is if the R square value is higher.   R-squared = Explained variation / Total variation

It can be misleading: A high R-squared value does not necessarily mean that the model is a good predictor of the dependent variable. The model may be overfitting the data or missing important predictors that could improve the model's accuracy. It is sensitive to outliers: R-squared is sensitive to outliers in the data, which can cause it to overestimate or underestimate the true relationship between the independent and dependent variables. It only applies to linear regression models: R-squared is only applicable to linear regression models, and cannot be used to evaluate the goodness of fit of other types of models, such as non-linear regression or time series models.

### **5.2.3 Mean Absolute Error (MAE)**

Mean Absolute Error is the average obtained between the original values and the predicted values. Additionally, it gauges how far the predictions deviate from the actual output, or the average magnitude of error. Additionally, MAE does not tell us whether we are underfitting the data or overfitting the data, i.e., the direction of error.                                                                                   (2)

MAE is a good option for datasets that contain outliers because it is less sensitive to outliers than other metrics like Mean Squared Error (MSE). MAE can be applied to non-linear models without a closed-form gradient solution. This makes it useful for assessing the effectiveness of models like random forests and decision trees

## **5.3 Results**

### **5.3.1 R-Squared Comparison of models with & without features (60:40)**

First of all, a study to determine the impact of features during model training was carried out using the data which we combined using the five conditions and five different cycles and trained models using data from five cycles in all five conditions and compared the R-squared metric using a training ratio of 6040 to choose the most accurate result between datasets that included features and those that did not. A bar graph was used to represent the mean R-squared values for the different models, and it was observed that the dataset including features produced an improved result compared to the dataset with only input variables. The inclusion of features resulted in a 10% increase in model accuracy compared to the previous model.  Conclusion – Thus, it is now clear that the models with features provide a better result compared to former.

Figure 5.3 – R-Sq Error Chart without Features

---

Figure 5.2 - R-Sq Error Chart with Features

---

### **5.3.2 RMSE Comparison of 80:20, 70:30, and 60:40 training ratios with features**

After we found the importance of features, we now moved on with the same dataset of five cycles and five different conditions to choose between a good training ratio.

Three histograms were made, to show the normal distribution of RMSE values for each algorithm & to show the count of RMSE values close to 0 for various algorithms. The histograms demonstrated that compared to the 60:40 training ratio and 70:30 training ratio, the 80:20 training ratio had a higher proportion of RMSE values close to 0 and higher peaks in the normal distribution curves. This suggests that when compared to the 60:40 and 70:30 training ratio, the 80:20 ratio produced better results in the output prediction.

Conclusion - The more RMSE values that are close to 0, the more accurate the model's predictions were with the 80:20 training ratio.

Figure 5.3 - RMSE Histogram of 60:40 Ratio

---

Figure 5.2 - RMSE Histogram of 80:20 Ratio

---

Figure 5.4 - RMSE of 70:30 Ratio

---

### **5.3.3 Choosing 5 algorithms by comparing their MAE and RMSE**

Figure 5.5 - Mean MAE Bar Chart

---

Figure 5.6- Mean RMSE Bar Chart

---

Following an analysis of the fundamental ideas that form the strong performance foundations, we are now down to choosing five algorithms with an 80:20 training ratio and features. These graphs show two metrics: on the left, the mean MAE values across all algorithms under study are shown, and on the right, the mean RMSE values are shown. We compared these 2 metrics because they cannot be used alone to determine accuracy due to their limitations. For example, as we have already seen, RMSE takes into account outliers while MAE is not sensitive to them. Because there

could be measurement error and the model could become inaccurate if it is overfitted, we need to be less sensitive to outliers in this case.

From these charts, it can be clearly seen that, Decision Tree, Random Forest, Extreme Gradient Boost, Neural Network, and Deep Neural Network provide the accurate results when compared to other algorithms because in both the evaluation metrics, the value of respective errors from all the algorithms is the least (close to zero).

### **5.3.4 Choosing 3 algorithms by individual cycle study of five conditions each**

In order to conduct a more thorough analysis, we used those five algorithms in five cycles and produced five radar charts that showed how the models' RMSE varied over those five cycles. The radar charts show how closely the RMSE values are spaced in each cycle, creating a web-like structure. It is clear from this that the Extreme Gradient Boosting, Neural Networks and Deep Neural Network offer the best prediction among the five options. because these three algorithms' RMSE values are nearly zero, which is excellent.

Figure 5.7 - Cycle Radar Charts

### **5.3.5 Execution Time Analysis of top three algorithms**

Execution time is crucial in a real-time battery monitoring system for accurately predicting battery health and calculating the battery's remaining life. Estimating the battery's remaining life is crucial for deciding when to charge or replace the battery to maintain continuous operation of the system or device. Additionally, where power consumption is a major concern, battery monitoring systems may be used in mobile devices or remote monitoring applications. The system will use more energy the longer it runs, potentially shortening the battery life even more.

Figure 5.8 - Time vs Algorithms

---

Finally, the chart depicts that the fastest execution was done by XGBoost followed by Neural Network and then Deep Neural Network. As DNN is quite complex and has more hidden layers, it indeed is time consuming and is not good for this system, taking around 43 Seconds to predict an output compared to XGBoost which takes as low as 1.2 Seconds to predict the output.

# **Chapter 6 BMS Module**

## **6.1 Hardware Requirements**

### **6.1.1 Voltage Sensor – (Voltage Detection Sensor Module 25V )**.

A voltage detection sensor module 25V is a device designed to measure the voltage of a circuit with a maximum voltage of 25V. It typically consists of a sensor, amplifier, and output interface, which enables a microcontroller or other device to read the measured voltage. Typically, the sensor consists of a voltage divider circuit that transforms the input voltage into a smaller, more easily measurable voltage. The amplifier amplifies the sensor's output signal to make it more accurate and easier to read, and the output interface permits a microcontroller or other device to read the measured voltage. This type of voltage sensor module is typically employed in applications where the input voltage is restricted to 25V or less, such as in battery-powered devices or low-voltage electrical systems. **This module is based on the principle of resistive voltage divider design, can make the red terminal connector input voltage 5 times smaller.** [Arduino](https://robu.in/product-category/arduino-2/arduino/) **analog input voltages up to 5 v, the voltage detection module input voltage not greater than 5Vx5=25V (if using 3.3V systems, input voltage not greater than 3.3Vx5=16.5V).** Arduino AVR chips have 10-bit AD, so this module simulates a resolution of 0.00489V (5V/1023), so the minimum voltage of input voltage detection module is 0.00489Vx5=0.02445V

### **6.1.2 Current Sensor (ACS712)**

The ACS712 is a module for measuring the current flowing through an electrical circuit. It consists of a Hall effect sensor, which detects the magnetic field generated by a conductor's current, and an amplifier circuit, which amplifies the sensor's output signal. Depending on the model, the ACS712 can measure both AC and DC currents with a range of 5A, 20A, or 30A. The measured current can be output as an analogue voltage or a digital pulse-width modulation (PWM) signal, which can be read by a microcontroller or other device. Common applications for the ACS712 include motor control, overcurrent protection, and power supply design.

### **6.1.3 Temperature Sensor (LM35)**

The LM35 is a temperature sensor used to measure the temperature of a physical object or the surrounding environment. It is a precision integrated-circuit temperature sensor, so it is extremely accurate and stable over a broad temperature range. With a scale factor of 10 mV/°C, the LM35 outputs an analogue voltage that is proportional to the temperature in degrees Celsius. This means that the output voltage of the LM35 will vary by 10 millivolts for every degree Celsius of temperature change. The LM35 is utilized in numerous temperature sensing applications, including thermostats, temperature-controlled fans, and temperature data loggers.

### **6.1.4 Lemon 1800mAh 3S 25C Lithium Polymer Battery**

The Lemon 1800mAh 3S 25C/50C Lithium Polymer battery is a common rechargeable battery found in radio-controlled (RC) vehicles and other electronic devices. It has a capacity of 1800mAh, indicating that it can store a substantial quantity of energy. The "3S" designation denotes that the battery consists of three lithium-ion cells connected in series, resulting in a nominal voltage of 11.1V. The designation "25C/50C" indicates that the battery can deliver a continuous discharge current of 25C or 50C, depending on the application. The "Lemon" brand produces premium lithium polymer batteries, and the 1800mAh 3S 25C/50C battery is a popular option for RC vehicles and other high-performance electronic devices.

### **6.1.5 Microprocessor (Raspberry Pi 4**)

The Raspberry Pi Foundation designs and manufactures the Raspberry Pi 4, a small, low-cost, single-board computer. It was released in June 2019 and is the most recent instalment in the Raspberry Pi computer line. Compared to its predecessor, the Raspberry Pi 3 Model B+, the Raspberry Pi 4 has a faster processor, more memory, and dual-display output support. Common applications include a home media centre, a do-it-yourself gaming console, and an inexpensive computer for education and programming. The Raspberry Pi 4 is a highly capable single-board computer that can perform a variety of tasks, such as media playback, gaming, and basic computing.

### **6.1.6 Power Distribution Board (PDB-XT60)**

Within an electronic system, a power distribution board (PDB) is a device used to distribute electrical power to multiple circuits or devices. A PDB-XT60 is a specific type of PDB that provides power to devices via XT60 connectors. XT60 connectors are a common type of high-current connector found on radio-controlled aircraft and vehicles. Typically, a PDB-XT60 is used to power the electronic speed controllers (ESCs) and other devices in a radio-controlled aircraft or vehicle. It assists in power distribution and protects against overcurrent and short-circuit conditions.

### **6.1.7 ADC Converter (ADS1115)**

ADS1115 is a 16-bit, extremely accurate, low-power analog-to-digital converter (ADC) that is frequently used in a variety of applications that call for precise measurement of analogue signals. The ADS1115 has four input channels with programmable gain amplifiers that support a wide range of input voltages and can convert analogue signals into digital data at up to 860 samples per second (SPS). For increased accuracy, it also includes an integrated voltage reference and temperature sensor. The I2C interface allows the ADS1115 to communicate with a microcontroller, making it simple to integrate into a variety of projects. ADS1115 is frequently used in sectors like medical equipment, industrial automation, and environmental monitoring due to its high precision and low power consumption.

## **6.2 Module Circuit**

Figure 6.1 - Real Life Module

---

Figure 6.2 - Schematic Circuit

# **Chapter 7 Data Collection & Results**

## **7.1 Data Collection using single motor**

Now that we have a thorough understanding of how the Extreme Gradient Boosting Algorithms deliver accurate results while operating extremely quickly, we want to gather data for a single motor with propellers using our custom BMS Module. Therefore, to get started, we connected the module to a hexacopter using the circuit depicted above, then we operated a single motored and recorded the data for a full cycle.  A drone cycle includes

1. Takeoff - Normally, a drone takes 50 secs to takeoff and travels at a high burst speed of 1 to 1.5 m/s.
2. Cruise - Next, the drone is allowed to travel for a predetermined amount of time to ensure consistent battery life and efficiency.
3. Landing - The drone speeds up for another 50 seconds during the landing phase before its propellers are eventually turned off.

To train the model using this data set, a total of three cycles of a single motor run were run for the data collection.

## **7.2 Data Collection for two & three motor runs**

After confirming the module's functionality, it is now time to collect data for two and three motors in order to study how the system behaves when operating in multi-rotor systems like quadcopters and hexcopters. As more motors are running, the load on the battery and the system's overall power consumption will increase. Although there were some voltage reading fluctuations, the data from the two motors was largely linear. Three iterations were performed for the previous full cycles for this as well.

Regarding the three-motor dataset, it was a fairly accurate representation of real-world data collection since most drones have four motors and the data won't be linear when using four motors. And since the dataset was quite nonlinear, we did in fact discover a similar pattern in it. We performed six iterations of this scenario, each iteration lasting until the battery dropped from 11.1 volts to 9 volts as a safety measure. For the purposes of testing and training machine learning, this data was combined.

Unfortunately, the current sensor only measured currents up to 20 Amps, and the load when a quadcopter is connected to the module exceeds 20 Amps. As a result, we implemented three motors to observe the differences.

## **7.3 Noise**

Now as our aim is to test the system in real life conditions, there will always be some kind of noise during sensor readings or any environmental conditions may impact it. Considering this, we introduced noise to our data set and then implemented the models on it. The term "noise" in a dataset describes the presence of random or irrelevant data points that do not accurately reflect any underlying patterns or relationships. Several things, including measurement errors, data entry errors, and outliers, can contribute to noise. Because noise can result in false conclusions or predictions, it can have a negative effect on the accuracy and reliability of statistical models and machine learning algorithms. Therefore, before beginning any data analysis or modelling, it is crucial to recognise and eliminate noise from a dataset.  

## **7.4 Gaussian Noise**

A common type of statistical noise used in signal processing and communication systems is referred to as gaussian noise. A Gaussian or normal distribution is followed by the probability density function (PDF) of this particular type of noise.

Gaussian noise is frequently used in machine learning as a regularization technique to avoid overfitting the model to the training data. During training, it is added to the model's input data, which aids in teaching it more robust and generalizable features. The standard deviation in Gaussian noise has a big impact because it controls how much noise is added to the input data. More noise is introduced as a result of a higher standard deviation, which can make it more challenging to draw conclusions from the input data. A lower standard deviation, on the other hand, leads to less noise being added, which may make it simpler for the model to absorb the input data.

So, for this 3Motors Dataset, we added three deviations—0.0125, 0.025, and 0.05—as noise and compared how different algorithms behaved. The findings of this study are then presented after this section.

## **7.5 Evaluation Results**

First, the Mean Absolute Error (MAE) for each of the three types of noise was examined and contrasted using a bar graph. Understanding which algorithm is operating accurately in each of the three conditions is made easier thanks to this statistical representation. As a result, the following charts show the MAE of 0.0125, 0.025, and 0.05 noise results (from the left). We can identify the top three algorithms under these circumstances by comparing them.

Figure 7.3 - 0.05 SD Results

---

Figure 7.2 - 0.025 SD Results

---

Figure 7.1 - 0.0125 SD Results

---

Figure 7.4 - Time Analysis for 3 Algorithms

---

The aim of this analysis is to determine which algorithms were accurate with increasing noise. Therefore, it is evident from this chart that, out of the nine algorithms, the Random Forest, XGBoost, and Deep Neural Network provided good accuracy.

Additionally, as previously mentioned, their execution time is crucial in determining real-time results; consequently, it was discovered during the time analysis that the XGBoost predicts the results quickly. In all three scenarios, DNN takes around 3.5 seconds to complete its prediction, whereas XGBoost only needs 0.05 seconds.  This is an excellent method.

# **Chapter 8 Real-time Interfacing**

Figure 8.1 - Pi's GPIO Pins

---

Based on the circuit diagram from the previous section, an Analogue to Digital Converter is crucial for connecting the Raspberry Pi to the circuit and reading the data because the sensors produce analogue signals, and the microcontroller does not have an internal ADC. The Raspberry Pi will additionally process the incoming data, run the model, and forecast the State of Charge in a matter of seconds. Pi's primary responsibility in this project is to gather data, preprocess it, use it in a specific way, and forecast the results.  The figure above shows the Graphical Input/Output Pin Headers of a Raspberry Pi

## **8.1 I2C Communication**

When an ADC is connected to raspberry pi, it used the I2C Communication Protocol to transfer and receive the data from the sensors. Two of the most crucial pins used in the I2C communication protocol are SCL and SDA. Serial Data is referred to as SDA, and Serial Clock is referred to as SCL. In an I2C network, these two pins are used to transmit and receive data between devices.

SCL is a signal that gives devices the timing for communication. It transmits a square wave      signal that establishes the communication's frequency. The speed of communication is determined by the signal's frequency. The master device in the I2C network produces the SCL signal.

SDA, on the other hand, is the signal that travels between devices and carries data. Each packet or frame that contains the data has a start bit, eight bits of data, an acknowledge bit, and a stop bit. Since the SDA signal is bidirectional, data can be sent and received using it.

## **8.2 ADS1115 with Raspberry PI and Display**

It's easy to connect the ADS1115 to a microcontroller. Since we are reading voltage and current sensors up to 5V, the ADC must first be powered using the 5V pin on the Pi. The other pins of the ADC must be connected with the sensor output pins, which are P0 with the current sensor, P1 with the voltage sensor, and P2 with the temperature sensor, in order to take readings from them. I2C communication will then transfer the readings to the PI in order to perform the necessary calculations.

Figure 8.2 - ADS1115 with Pi

---

And to get the display of what the results are, we connected the desktop with HDMI cable and performed the machine learning using the visual interface.

## **8.3 Code & Documentation**

## **8.4 Results**

We applied this algorithm to the same three-motor drone module that was used for data collection, and we saw generally positive results. However, the accuracy could be increased, which will be covered in more detail later.

To start, we mimicked three conditions.

1. High Speed Condition - As the drone takes off, it experiences a high burst and maximum throttle, resulting in a high current flow and a quick loss of battery capacity.  2. Cruise Condition - A drone on a cruise basically travels at a constant speed while its battery power steadily depletes. This is another situation that occurs in real life and contributes to battery loss. 3. Variable Speed Conditions - Real-world conditions are a little trickier because they frequently involve unforeseen events like sudden gusts of wind, high altitudes, etc. that necessitate adjusting the drone's speed. Therefore, real-time prediction algorithms need to take this scenario into account.

The images mentioned above show the actual and predicted values for the variable condition and cruise condition states of charge. It is clear that the algorithm behaves inappropriately and generates a significant amount of error at low states of charge. Similar results can be seen when travelling; the prediction is less accurate at lower battery percentages, and as a result, error increases at lower state of charge.

Figure 8.3 - Real vs Predicted SOC at Cruise Condition

---

Figure 8.2 - Real vs Predicated SOC at Variable Condition

---

A specific pattern in the predicted values cannot be seen in the scenario for high-speed conditions, but eventually it can be seen that the error increases at lower percentages of battery state.

Figure 8.4-Real vs Predicated SOC at High Speed

---

Figure 26 represents the error values for the three conditions. And following the similar patterns, it shows that at the end of the cycle, the error increases for all the three scenarios and thus now it is evident that the algorithm is lacking accuracy at low state of charge levels. The main reason for these low accuracy at particular charging level is the lack of datapoints at these low levels. Due to this the model is not able to train at these lower levels and thus prediction is also inaacurate.

Figure 8.5 - Error values of three conditions

---

# **Chapter 9 Conclusion and Future Work**

## **9.1 Conclusion**

This project involved more than just using machine learning in real-time; it also involved selecting the best algorithm to deliver accurate results by feature engineering data preprocessing, data collection at various stages, and simulating real-world conditions using various techniques like noise, drone testing, etc. Knowing how to integrate sensors and software systems, taking into account training ratios while analyzing the effects on the results, monitoring displays in real-time, combining data collection and prediction at the same time, and ultimately obtaining the final State of Charge are all skills that are required.

We acquired a variety of skills over the course of the entire period, which made the project challenging for both of us. The project's goal was to reduce the price of a typical BMS circuit using arcane circuitry and to make it simpler using simple sensors and artificial intelligence. By drawing the conclusions listed below, we were able to accomplish the project's goal.

1. To find the best algorithms for this system by obtaining a suitable dataset that can be used for an offline test of various algorithms.
2. Machine learning techniques were helpful for this project, and an offline analysis of the dataset led to the discovery of a more reliable model.
3. Using various hardware parts, a straightforward BMS Module was created that was nearly flawless given the connection with various components.
4. The module did quite well during the data collection stage, which was important because if there were errors in the dataset, the model would be trained to produce inaccurate results, and the prediction would be uninspiring.
5. Finally, the BMS module's interface with the microcontroller was successful because it quickly and accurately predicted the desired real-time result.

## **9.2 Future Work**

Every system has a room for improvement. This project focused on predicting the State of Charge of a battery while a load is connected to it. More features can be added to this system and future prospects are listed below

1. As a battery works continuously, there are chances of high heat generation and thus a heat sink can be made. A similar AI driven heat sink which activated upon a certain temperature range and helps the battery maintain a constant temperature would suffice the need.
2. Use of high ended sensors which can measure to a quite high range of current and voltage will increase the versatility of this system and can be useful in any electronics devices. Currently it is limited to smaller dimensional aero vehicles like drones.
3. Also, if we collect the data for 2S and 4S batteries, this system can also be run on the devices using these batteries, which will also add up to its versatility.

# **Bibliography**

1. Vilsen, S. B., & Stroe, D.-I. (2021). Battery state-of-health modelling by multiple linear regression. *Journal of Cleaner Production*, *290*, 125700. https://doi.org/10.1016/j.jclepro.2020.125700
2. Lelie, M., Braun, T., Knips, M., Nordmann, H., Ringbeck, F., Zappen, H., & Sauer, D. (2018). Battery Management System Hardware Concepts: An Overview. *Applied Sciences*, *8*(4), 534. https://doi.org/10.3390/app8040534
3. *Battery Management Systems* (Vol. 9). (2008). Springer Netherlands. https://doi.org/10.1007/978-1-4020-6945-1
4. Ardeshiri, R. R., Balagopal, B., Alsabbagh, A., Ma, C., & Chow, M.-Y. (2020). Machine Learning Approaches in Battery Management Systems: State of the Art: Remaining useful life and fault detection. *2020 2nd IEEE International Conference on Industrial Electronics for Sustainable Energy Systems (IESES)*, 61–66. https://doi.org/10.1109/IESES45645.2020.9210642
5. Alzubaidi, L., Zhang, J., Humaidi, A. J., Al-Dujaili, A., Duan, Y., Al-Shamma, O., Santamaría, J., Fadhel, M. A., Al-Amidie, M., & Farhan, L. (2021). Review of deep learning: concepts, CNN architectures, challenges, applications, future directions. *Journal of Big Data*, *8*(1), 53. https://doi.org/10.1186/s40537-021-00444-8
6. Ying LU, Song Y., (2015). Decision tree methods: applications for classification and prediction. Shanghai Archives of Psychiatry, https://doi.org/10.11919%2Fj.issn.1002-0829.215044
7. Henrique, B. M., Sobreiro, V. A., & Kimura, H. (2018). Stock price prediction using support vector regression on daily and up to the minute prices. *The Journal of Finance and Data Science*, *4*(3), 183–201. https://doi.org/10.1016/j.jfds.2018.04.003
8. Smola, A. J., & Schölkopf, B. (2004). A tutorial on support vector regression. *Statistics and Computing*, *14*(3), 199–222. https://doi.org/10.1023/B:STCO.0000035301.49549.88
9. Pahlavan-Rad, M. R., Dahmardeh, K., Hadizadeh, M., Keykha, G., Mohammadnia, N., Gangali, M., Keikha, M., Davatgar, N., & Brungard, C. (2020). Prediction of soil water infiltration using multiple linear regression and random forest in a dry flood plain, eastern Iran. *CATENA*, *194*, 104715. https://doi.org/10.1016/j.catena.2020.104715
10. Chen, T., & Guestrin, C. (2016). XGBoost. *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 785–794. https://doi.org/10.1145/2939672.2939785
11. Vilsen, S. B., & Stroe, D.-I. (2021). Battery state-of-health modelling by multiple linear regression. *Journal of Cleaner Production*, *290*, 125700. https://doi.org/10.1016/j.jclepro.2020.125700
12. Ardeshiri, R. R., Balagopal, B., Alsabbagh, A., Ma, C., & Chow, M.-Y. (2020). Machine Learning Approaches in Battery Management Systems: State of the Art: Remaining useful life and fault detection. *2020 2nd IEEE International Conference on Industrial Electronics for Sustainable Energy Systems (IESES)*, 61–66. https://doi.org/10.1109/IESES45645.2020.9210642
13. Yang, H., Cao, Y., Xie, H., Shao, S., Zhao, J., Gao, T., Zhang, J., & Zhang, B. (2020). Lithium-ion Battery Life Cycle Prediction with Deep Learning Regression Model. *2020 IEEE Applied Power Electronics Conference and Exposition (APEC)*, 3346–3351. https://doi.org/10.1109/APEC39645.2020.9124049
14. Ng, M.-F., Zhao, J., Yan, Q., Conduit, G. J., & Seh, Z. W. (2020). Predicting the state of charge and health of batteries using data-driven machine learning. *Nature Machine Intelligence*, *2*(3), 161–170. https://doi.org/10.1038/s42256-020-0156-7
15. https://www.tytorobotics.com/blogs/articles/a-guide-to-lithium-polymer-batteries-for-drones
