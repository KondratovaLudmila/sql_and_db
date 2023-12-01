SELECT ROUND(AVG(m.mark),2) as max_avg_mark, g.grup
FROM marks m
JOIN students s ON m.student_id = s.id
JOIN grups g ON s.grup_id = g.id
WHERE m.subject_id = :subject_id
GROUP BY g.grup;