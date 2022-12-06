# RealTimeBatteryMonitoringSystem
* Implementation of research papers with the goal of improving the existing system for monitoring batteries using machine learning and deep learning techniques.
##  Dataset Details:
https://data.mendeley.com/datasets/cp3473x7xv/3

Description
The included tests were performed at McMaster University in Hamilton, Ontario, Canada by Dr. Phillip Kollmeyer (phillip.kollmeyer@gmail.com). If this data is utilized for any purpose, it should be appropriately referenced.
-A brand new 3Ah LG HG2 cell was tested in an 8 cu.ft. thermal chamber with a 75amp, 5 volt Digatron Firing Circuits Universal Battery Tester channel with a voltage and current accuracy of 0.1% of full scale. these data are used in the design process of an SOC estimator using a deep feedforward neural network (FNN) approach. The data also includes a description of data acquisition, data preparation, development of an FNN example script.

-Instructions for Downloading and Running the Script:
1-Select download all files from the Mendeley Data page (https://data.mendeley.com/datasets/cp3473x7xv/2).  
2-The files will be downloaded as a zip file.  Unzip the file to a folder, do not modify the folder structure.  
3-Navigate to the folder with "FNN_xEV_Li_ion_SOC_EstimatorScript_March_2020.mlx"
4-Open and run "FNN_xEV_Li_ion_SOC_EstimatorScript_March_2020.mlx"
5-The matlab script should run without any modification, if there is an issue it's likely due to the testing and training data not being in the expected place.
6-The script is set by default to train for 50 epochs and to repeat the training 3 times.  This should take 5-10 minutes to execute.
7-To recreate the results in the paper, set number of epochs to 5500 and number of repetitions to 10.

-The test data, or similar data, has been used for some publications, including:
[1] C. Vidal, P. Kollmeyer, M. Naguib, P. Malysz, O. Gross, and A. Emadi, “Robust xEV Battery State-of-Charge Estimator Design using Deep Neural Networks,” in Proc WCX SAE World Congress Experience, Detroit, MI, Apr 2020
[2] C. Vidal, P. Kollmeyer, E. Chemali and A. Emadi, "Li-ion Battery State of Charge Estimation Using Long Short-Term Memory Recurrent Neural Network with Transfer Learning," 2019 IEEE Transportation Electrification Conference and Expo (ITEC), Detroit, MI, USA, 2019, pp. 1-6.
            
