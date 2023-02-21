from ImageRenamingClasses import BinaryNameAssigner
from imageTimingClasses import imageTiming

# ask user for names and store them in an array
responses = [1, 0, 1, 0, 1]
bna = BinaryNameAssigner(responses)
assigned_names = bna.assign()

print(assigned_names)

# record the time elapsed for each name
it = imageTiming(responses)
it.record(assigned_names)