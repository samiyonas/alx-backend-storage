-- Procedure that calculates average score
DELIMITER $$

CREATE PROCEDURE computeAverageScoreForUser(user_id INT)
BEGIN
DECLARE average FLOAT;
SELECT AVG(score) INTO average
FROM corrections
WHERE corrections.user_id = user_id;

IF average IS NOT NULL THEN
UPDATE users SET average_score = average WHERE id = user_id;
END IF;

END$$

DELIMITER ;
