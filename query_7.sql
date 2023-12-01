SELECT m.mark, m.date, s.student
FROM marks m
JOIN students s ON s.id = m.student_id 
WHERE s.grup_id = :grup_id AND m.subject_id = :subject_id
