import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Execute a query to retrieve data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Close the connection
conn.close()
