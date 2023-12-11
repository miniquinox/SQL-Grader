-- Query 1: List all students
SELECT * FROM students;

-- Query 2: Average age of students
SELECT AVG(age) FROM students;

-- Query 3: List students with grades above 80 in Mathematics
SELECT s.name, g.grade 
FROM students s 
JOIN grades g ON s.id = g.student_id 
WHERE g.course = 'Mathematics' AND g.grade > 80;

-- Query 4: Number of students in each major
SELECT major, COUNT(*) 
FROM students 
GROUP BY major;