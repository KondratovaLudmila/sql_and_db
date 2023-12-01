SELECT ROUND(AVG(m.mark), 2) average_mark, s.subject
FROM marks m
JOIN subjects s ON s.id = m.subject_id 
WHERE s.teacher_id = :teacher_id
GROUP BY s.subject
