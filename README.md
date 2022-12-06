# RealTimeBatteryMonitoringSystem

## Purpose
* With the rise of electrification in various tech products, many countries are
working towards optimizing the performance and safety of battery
operated machines.
* Lithuim-ion battery is used widely. This wide usage is primarily because it is
lighter, efficient, charge faster and have a longer lifespan than other.
* Practically, Li-ion batteries are susceptible to many conditions that can
damage the battery pack.
* Thus a typical Battery Monitoring System (BMS) became a revolutionary
component which has the capability to monitor and optimize various
parameters like Current, Voltage, Temperature, concerned for the safety.


## Functions
* The primary function of the BMS is to protect the battery cells from
damage caused by being overcharged or over-discharged.
* But it has many more functionalities apart from protecting:

### Sensing Functionalities
Measures cell voltages
Measure cell current
Measure cell temperature

### Protection Functionalities
* Over Voltage , Current & Temperature
* Short Circuits
* Disconnecting a cell if faulty

### Estimation
**State of Charge (SOC)
* It is the level of charge of a battery relative to its capacity of charge
**State of Health (SOH)
* It is the measure of a performance of a battery considering the difference of
the maximum capacity currently in use to the maximum capacity of a fresh
battery.

## Working

* BMS gets the data from various sensors
* Measuring with the help of a Microcontroller unit
* Estimation of State of Charge, State of Health, Thermal Status with various algorithms
* Data sent through Control Area Network of that system to perform require actions

## Problem Statement

* Currently, battery monitoring system rely mostly on measurement of current and
voltage and ultimately SOC through hardware systems.
* These methods neglect to consider temperature of surroundings as a parameter,
which are pretty critical in understanding the true runtime of the battery
* Current algorithms (such as Coulomb Counting, Voltage Method) suffer from
* Hysterisis — a condition where there is a delay in the output of a system —causing
a certain error in measurements
* Battery aging effects are not taken seriously which effects the accuracy

## Objectives
* In this age of Artificial Intelligence, there are very few BMS systems based on
Machine Learning
* One of the best solution to overcome the challenges aforementioned is to use
data driven approach in order to be efficient and accurate.
* To study different machine learning approach and to find the best approach
* To bring into account the effect of battery temperature in order to get the
optimum result


## Methodology

1. To make a BMS Hardware system to get a real time current, voltage data
2. Testing the hardware system Methodology
3. Select a Machine Learning Algorithm with necessary requirements
4. Train the model with a specific data set
5. Validate the model and implement on the
system





##  Dataset Details:
https://data.mendeley.com/datasets/cp3473x7xv/3

Description
The included tests were performed at McMaster University in Hamilton, Ontario, Canada by Dr. Phillip Kollmeyer (phillip.kollmeyer@gmail.com). If this data is utilized for any purpose, it should be appropriately referenced.
-A brand new 3Ah LG HG2 cell was tested in an 8 cu.ft. thermal chamber with a 75amp, 5 volt Digatron Firing Circuits Universal Battery Tester channel with a voltage and current accuracy of 0.1% of full scale. these data are used in the design process of an SOC estimator using a deep feedforward neural network (FNN) approach. The data also includes a description of data acquisition, data preparation, development of an FNN example script.
