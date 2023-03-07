import psycopg2
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

# example array
initalArray = [0, 0, 0, 0]

# new array
newArray = [1, 1, 1, 0]

# new array2
newArray2 = [1, 1, 1, 1]

# pass array into class
bna = BinaryNameAssigner(initalArray)

# ask user to name each occurance in array
assigned_names = bna.assign()
print(assigned_names)

timing = imageTiming(initalArray, assigned_names, db_config)

# Feed in arrays of responses
timing.record(newArray)

calculation = imageAverage(db_config)
calculation.average


