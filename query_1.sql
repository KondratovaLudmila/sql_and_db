SELECT s.student, ROUND(AVG(m.mark), 2) as average_mark
FROM marks m
JOIN students s ON m.student_id = s.id
GROUP BY m.student_id, s.student
ORDER BY average_mark DESC
LIMIT 5