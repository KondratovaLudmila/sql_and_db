SELECT s.subject
FROM marks m
JOIN subjects s ON s.id = m.subject_id 
WHERE m.student_id = :student_id AND s.teacher_id = :teacher_id
GROUP BY s.subject;
