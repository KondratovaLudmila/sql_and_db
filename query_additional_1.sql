SELECT ROUND(AVG(m.mark), 2) as average_mark
FROM marks m
JOIN subjects s ON s.id = m.subject_id 
WHERE m.student_id = :student_id AND s.teacher_id = :teacher_id

