import sqlite3

# Connect to SQLite database
connect_to_Sq3 = sqlite3.connect(".school.db")
cursor = connect_to_Sq3.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT,
    marks INTEGER
)
''')

# Insert sample data
sample_data = [
    (1, "Alice", 22, "F", 88),
    (2, "Bob", 24, "M", 76),
    (3, "Charlie", 23, "M", 65),
    (4, "Diana", 21, "F", 92),
    (5, "Eva", 25, "F", 71)
]
cursor.executemany("INSERT OR REPLACE INTO students VALUE (?, ?, ?, ?, ?)",sample_data)
connect_to_Sq3.commit()

# Can Run ANY QURISE NOW 
# 1.
cursor.execute("SELECT name, marks FROM students WHERE gender = 'F' ORDER BY marks")
print(cursor.fetchall())
# 2. 
cursor.execute("SELECT name, age, marks FROM students WHERE age > 22 AND marks < 80")
print(cursor.fetchall())
# 3.
cursor.execute("SELECT COUNT(marks) FROM students WHERE marks > 75")
print(cursor.fetchone()[0])
# 4.
cursor.execute("SELECT name, marks FROM students ORDER BY marks DESC LIMIT 2")
print(cursor.fetchall())

# 5.
cursor.execute("UPDATE students SET marks = marks + (marks * 0.1) WHERE age > 23")
connect_to_Sq3.commit()

# 6.
cursor.execute("DELETE FROM students WHERE marks < 50")
connect_to_Sq3.commit()

# 7.
cursor.execute("SELECT gender, AVG(marks) FROM students GROUP BY gender")
print(cursor.fetchall())

# 8.
cursor.execute("""
SELECT MAX(marks) FROM students 
WHERE marks < (SELECT MAX(marks) FROM students)
""")
print("Second highest marks:", cursor.fetchone()[0])

connect_to_Sq3.close()
