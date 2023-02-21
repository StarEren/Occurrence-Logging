import random
import datetime
import time

class imageTiming:
    def __init__(self, responses, assigned_names):
        self.responses = responses
        self.prev_timestamp = None
        self.assigned_names = assigned_names
    
    def record(self):
        while True:
        
            results = []
            for i in range(len(self.responses)):
                
                #random waittime for test
                wait = random.uniform(1, 5)
                print(f"Wait time for image {i+1}: {wait}")
                time.sleep(wait)
                
                curr_timestamp = datetime.datetime.now()
                if self.prev_timestamp is not None:
                    time_elapsed = (curr_timestamp - self.prev_timestamp).total_seconds()
                else:
                    time_elapsed = 0
                result = {
                    "time_elapsed": time_elapsed,
                    "response": "pass" if int(self.responses[i]) == 1 else "fail"
                }
                results.append(result)
                self.prev_timestamp = curr_timestamp

                with open('recording_results.txt', 'a') as f:
                    f.write(f"Part: {self.assigned_names[i]}, DateTime: {curr_timestamp}, Response: {result['response']}, Time Elapsed: {result['time_elapsed']} seconds\n")

            return results


    
#random pass or fail inputs for test    
#responses = [1, 1, 0]
# Create an instance of the class
#timing = imageTiming(responses)
#results = timing.record()