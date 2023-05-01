# importing the multiprocessing module
import multiprocessing
import os
import RunModelScript
import testClass1
import DataPreprocessingScript
import time

def worker1():
    lastFileLength = 0 
    bm=RunModelScript.BatteryMonitor('noNoise.pkl')
    while True:
        time.sleep(40)
        # try:
        print("in try")
        preprocessor=DataPreprocessingScript.CSVPreprocessor('data14.csv')
        print("in try 2")
        preprocessed_file = preprocessor.preprocess()
        print("in try 3")
        print('PreprocessedFile:', preprocessed_file)
        predicted_SOC, real_SOC = bm.predict_SOC('data14_preprocessed.csv')
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
