from imageRenamingClasses import BinaryNameAssigner
from imageTimingClasses import imageTiming

# example array
responses = [1, 0, 1, 0]

# pass array into class
bna = BinaryNameAssigner(responses)

# ask user to name each occurance in array
assigned_names = bna.assign()
print(assigned_names)

# pass in names and array into class
timing = imageTiming(responses, assigned_names)

# record time elasped for each pass or fail and write to rescording_results.txt
timing.record()