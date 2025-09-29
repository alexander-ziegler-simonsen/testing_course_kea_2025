import sqlite3

# Connect to the database file (creates it if it doesn't exist)
conn = sqlite3.connect("gradeDatabase.db")
cursor = conn.cursor()

# Load SQL script
with open("init.sql", "r") as f:
    sql_script = f.read()
    cursor.executescript(sql_script)

conn.commit()

# Example query
cursor.execute("SELECT * FROM grades")
for row in cursor.fetchall():
    print(row)

conn.close()
