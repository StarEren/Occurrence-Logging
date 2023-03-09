import psycopg2
import random
import time
from imageRenamingClasses import BinaryNameAssigner
from imageTimingClasses import imageTiming
from imageAverageClasses import imageAverage

db_config = {
    "hostname": "localhost",
    "database": "imageTiming",
    "username": "postgres",
    "pwd": "W1nter@2023Hydro",
    "port_id": 5432
}

# define the initial array
arr = [random.randint(0, 1) for i in range(4)]


# pass array into class
bna = BinaryNameAssigner(arr)

# ask user to name each occurance in array
assigned_names = bna.assign()
print(assigned_names)

timing = imageTiming(assigned_names, db_config)

# loop until all elements are 1
while 0 in arr:

    # generate a new array
    arr = [random.randint(0, 1) for i in range(4)]
    
    # Feed in arrays of responses
    response = timing.record(arr)
    
    # wait for a random amount of time between 1 and 4 seconds
    wait_time = 0.3
    time.sleep(wait_time)
    
    # print the new array
    print(arr)
    
calculation = imageAverage(db_config)
calculation.average(arr)