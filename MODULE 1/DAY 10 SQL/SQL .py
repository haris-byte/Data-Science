import sqlite3
connect = sqlite3.connect("school.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade REAL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_name TEXT,
    score REAL,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
""")

cursor.executemany("""
INSERT OR IGNORE INTO students (id, name, grade) VALUES (?, ?, ?)
""", [
    (1, 'Alice', 89),
    (2, 'Bob', 92),
    (3, 'Charlie', 78)
])


cursor.executemany("""
INSERT OR IGNORE INTO courses (id, student_id, course_name, score) VALUES (?, ?, ?, ?)
""", [
    (1, 1, 'Math', 85),
    (2, 1, 'Science', 90),
    (3, 2, 'Math', 95),
    (4, 3, 'Math', 70)
])
connect.commit()

#Aggregation
print(cursor.execute("SELECT AVG(score) FROM courses").fetchall()[0])

print(cursor.execute("SELECT student_id, AVG(score) FROM courses GROUP BY student_id").fetchall())

print(cursor.execute("SELECT course_name, MAX(score) FROM courses GROUP BY course_name").fetchall())

# JOIN query
print("Student Course Scores:")
cursor.execute("""
SELECT students.name, courses.course_name, courses.score
FROM students
LEFT JOIN courses ON students.id = courses.student_id
""")

for row in cursor.fetchall():
    print(row)

# Close connection
connect.close()
