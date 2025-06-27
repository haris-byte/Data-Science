CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INT,
    gender TEXT,
    marks REAL
);

INSERT OR REPLACE INTO students (id,name,age,gender,marks)
VALUES
    (1, "Alice", 22, "F", 88),
    (2, "Bob", 24, "M", 76),
    (3, "Charlie", 23, "M", 65),
    (4, "Diana", 21, "F", 92),
    (5, "Eva", 25, "F", 71);

SELECT * FROM students;
SELECT name, grade FROM students WHERE grade >=90;
UPDATE students SET grade=95 WHERE name='Alice';
DELETE FROM students WHERE grade < 80;




-- | id | name    | age | gender | marks |
-- | -- | ------- | --- | ------ | ----- |
-- | 1  | Alice   | 22  | F      | 88    |
-- | 2  | Bob     | 24  | M      | 76    |
-- | 3  | Charlie | 23  | M      | 65    |
-- | 4  | Diana   | 21  | F      | 92    |
-- | 5  | Eva     | 25  | F      | 71    |



SELECT id ,marks FROM students;
SELECT * FROM students;

SELECT * FROM students WHERE age >= 22
SELECT id , name, marks FROM students WHERE gender = "F"

SELECT  * FROM students ORDER BY age ASC;
LIMIT 4

UPDATE students SET marks = marks - 5 WHERE id = 2;

DELETE FROM students WHERE marks < 70;

SELECT gender, COUNT(*) FROM students GROUP BY gender;

SELECT AVG(marks) FROM students;
SELECT MAX(marks) FROM students;
SELECT MIN(age) FROM students;

SELECT * FROM students WHERE name LIKE "%ha%" -- IN MIDDLE 

SELECT * FROM students WHERE marks BETWEEN 80 AND 90 




--QUESTIONS Answer:
1. SELECT name ,marks FROM students WHERE gender = 'F' ORDER BY marks;
2. SELECT name ,age,marks FROM students WHERE age > 22 AND marks < 80;
3. SELECT COUNT(marks) FROM students WHERE marks > 75;
4. SELECT name, marks FROM students ORDER BY marks DESC LIMIT 2;
5. SELECT name FROM students WHERE age > 23 marks = marks + (0.1*marks);
-- Use UPDATE name FROM students WHERE age > 23 marks = marks + (0.1*marks);
6. DELETE FROM students WHERE marks < 50;
7. SELECT AVG(marks) FROM students GROUP BY gender;
8. SELECT MAX(marks) FROM WHERE marks < SELECT MAX(marks) FROM students
-- SELECT MAX(marks) FROM students 
-- WHERE marks < (SELECT MAX(marks) FROM students);


