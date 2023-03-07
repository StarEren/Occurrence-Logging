import datetime
import random
import time
import os
import psycopg2

class imageTiming:
    def __init__(self, assigned_names, db_config):
        self.prev_timestamp = datetime.datetime.now()
        self.db_config = db_config
        self.assigned_names = assigned_names
        self.current_array = None
        self.current_index = 0
    
    def record(self, new_array):
        if self.current_array is None:
            self.current_array = new_array
        
        conn_string = "host={0} port={1} dbname={2} user={3} password={4}".format(
            self.db_config["hostname"],
            self.db_config["port_id"],
            self.db_config["database"],
            self.db_config["username"],
            self.db_config["pwd"]
         )

        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        
        new_results = []

        for i, val in enumerate(new_array):

            if self.current_array[i] != val:
                curr_timestamp = datetime.datetime.now()
                if self.prev_timestamp is not None:
                    time_elapsed = (curr_timestamp - self.prev_timestamp).total_seconds()
                else:
                    time_elapsed = 0
                
                result = {"assigned_name": self.assigned_names[i], "response": val, "time_elapsed": time_elapsed}
                new_results.append(result)
                
                self.prev_timestamp = curr_timestamp
                self.current_array[i] = val
                
                self.current_index = i
            
            elif i == self.current_index:
                curr_timestamp = datetime.datetime.now()
                if self.prev_timestamp is not None:
                    time_elapsed = (curr_timestamp - self.prev_timestamp).total_seconds()
                else:
                    time_elapsed = 0
                
                result = {"assigned_name": self.assigned_names[i], "response": val, "time_elapsed": time_elapsed}
                new_results.append(result)
                
                self.prev_timestamp = curr_timestamp
        
        # Determine the shift based on the current time
        curr_hour = datetime.datetime.now().hour
        if 7 <= curr_hour < 15:
            shift = "Day"
        elif 15 <= curr_hour < 23:
            shift = "Afternoon"
        else:
            shift = "Night"
        
        # Insert the results into the PostgreSQL database
        for result in new_results:
            cur.execute(
                "INSERT INTO results (assigned_name, timestamp, response, time_elapsed, shift) VALUES (%s, %s, %s, %s, %s)",
                (result["assigned_name"], datetime.datetime.now(), result["response"], result["time_elapsed"], shift)
            )
        
        conn.commit()
        
        # Close the database cursor and connection
        cur.close()
        conn.close()
        
        return new_results
