import random
import datetime
import time

class imageTiming:
    def __init__(self, responses):
        self.responses = responses
        self.timestamps = [datetime.datetime.now() for _ in range(len(responses))]
    
    def record(self, assigned_names):
        self.assigned_names = assigned_names
        results = []

        for i in range(len(self.responses)):
            #random waittime for test
            wait = random.uniform(1, 5)
            time.sleep(wait)
            curr_timestamp = datetime.datetime.now()
            time_elapsed = (curr_timestamp - self.timestamps[i]).total_seconds()
            result = {
                "time_elapsed": time_elapsed,
                "response": "pass" if int(self.responses[i]) == 1 else "fail"
            }
            results.append(result)

            with open('recording_results.txt', 'a') as f:
                f.write(f"Part: {self.assigned_names[i]}, DateTime: {self.timestamps[i]}, Response: {result['response']}, Time Elapsed: {result['time_elapsed']} seconds\n")

        return results

    
#random pass or fail inputs for test    
#responses = [1, 1, 0]
# Create an instance of the class
#timing = imageTiming(responses)
#results = timing.record()