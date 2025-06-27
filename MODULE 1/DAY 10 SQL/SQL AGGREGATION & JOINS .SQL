CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_name TEXT,
    score REAL
);
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade REAL
);

INSERT INTO courses (student_id, course_name, score) VALUES
(1, 'Math', 85),
(1, 'Science', 90),
(2, 'Math', 95),
(3, 'Math', 70);
INSERT INTO students (name, grade) VALUES ('Alice', 89), ('Bob', 92), ('Charlie', 78);


SELECT AVG(score) FROM courses;
SELECT student_id ,AVG(score) FROM courses GROUP BY student_id;
SELECT course_name, MAX(score) FROM courses GROUP BY course_name


SELECT students.name, courses.course_name, courses.score
FROM students
INNER JOIN courses
ON students.id = courses.student_id;

SELECT students.name, courses.course_name, courses.score
FROM students
left JOIN courses
ON students.id = courses.student_id;
