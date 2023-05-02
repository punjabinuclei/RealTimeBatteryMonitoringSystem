import subprocess
import time

while True:
    # run script 1 for 40 seconds to get sensor data and save it to data.csv
    subprocess.call(['python', 'combinedCode.py'])
    time.sleep(40)

    # run script 2 for 20 seconds to preprocess the data and save it to ModelTestData.csv
    subprocess.call(['python', 'DataPreprocessingScript.py'])
    time.sleep(20)

    # run script 3 for 10 seconds to run the model on the preprocessed data
    subprocess.call(['python', 'RunModelScript.py'])
    time.sleep(10)
