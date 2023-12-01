SELECT m.mark, s.student, m.date
FROM marks m
JOIN students s ON s.id = m.student_id
JOIN grups g ON g.id = s.grup_id
INNER JOIN(
		SELECT MAX(date) last_lesson_date, grup_id, subject_id
		FROM marks
		JOIN students ON students.id = marks.student_id
		WHERE students.grup_id = :grup_id AND marks.subject_id = :subject_id
		) t ON t.last_lesson_date = m.date AND t.subject_id = m.subject_id AND t.grup_id = g.id


