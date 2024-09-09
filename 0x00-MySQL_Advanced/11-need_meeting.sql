-- no table for a meeting
CREATE OR REPLACE VIEW need_meeting AS
SELECT name FROM students
WHERE score > 80 AND (last_meeting IS NULL or last_meeting < ADDDATE(CURDATE(), interval -1 MONTH);
