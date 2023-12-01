SELECT ROUND(AVG(m.mark), 2) as max_avg_mark, s.student
FROM marks m
JOIN students s ON m.student_id = s.id
WHERE subject_id = :subject_id
GROUP BY m.student_id, s.student
ORDER BY max_avg_mark DESC 
LIMIT 1
