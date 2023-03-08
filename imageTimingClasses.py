import datetime
import random
import time
import os
import psycopg2
import pytz

class imageTiming:
    def __init__(self, assigned_names, db_config):
        self.prev_timestamp = datetime.datetime.now()
        self.db_config = db_config
        self.assigned_names = assigned_names
        self.current_array = None
        self.current_index = None
        self.last_updated = [datetime.datetime.now(pytz.utc) for _ in assigned_names]
        
    def record(self, new_array):
        if self.current_array is None:
            self.current_array = new_array
            self.current_index = 0
        
        conn_string = "host={0} port={1} dbname={2} user={3} password={4}".format(
            self.db_config["hostname"],
            self.db_config["port_id"],
            self.db_config["database"],
            self.db_config["username"],
            self.db_config["pwd"]
         )

        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        
        curr_timestamp = datetime.datetime.now(datetime.timezone.utc)
        new_results = []

        for i, val in enumerate(new_array):
            if self.current_array[i] != val:
                time_elapsed = round((curr_timestamp - self.last_updated[i]).total_seconds(), 2)
                
                result = {"assigned_name": self.assigned_names[i], "response": val, "time_elapsed": time_elapsed}
                new_results.append(result)
                
                self.last_updated[i] = curr_timestamp
                self.current_array[i] = val
                
                self.current_index = i
            
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
                (result["assigned_name"], curr_timestamp, result["response"], result["time_elapsed"], shift)
            )
        

        conn.commit()
        
        # Close the database cursor and connection
        cur.close()
        conn.close()
        
        return new_results