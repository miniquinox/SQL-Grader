-- Query 1: List all students
SELECT * FROM students;

-- Query 2: Incorrect calculation of average age
SELECT SUM(age) / COUNT(*) FROM students;

-- Query 3: Incorrect JOIN results in error
SELECT s.name, g.grade 
FROM students s, grades g 
WHERE g.course = 'Mathematics' AND g.grade > 80;

-- Query 4: Correct number of students in each major
SELECT major, COUNT(*) 
FROM students 
GROUP BY major;
