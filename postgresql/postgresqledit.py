import psycopg2

hostname = 'localhost'
database = 'imageTiming'
username = 'postgres'
pwd = 'W1nter@2023Hydro'
port_id = 5432

conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port=port_id)

# Set up cursor
cur = conn.cursor()

# Specify the name of the table to delete all data from
table_name = "results"

# Construct the DELETE query
query = f"DELETE FROM {table_name};"

# Execute the DELETE query
cur.execute(query)

# Commit the transaction
conn.commit()

# Close cursor and connection
cur.close()
conn.close()

print(f"All data entries have been deleted from {table_name}")