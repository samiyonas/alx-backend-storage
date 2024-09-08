-- stored procedure 1

DELIMITER $$

CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
DECLARE projId INT;
SELECT id INTO projId FROM projects
WHERE name = project_name;

IF projId IS NULL THEN
INSERT INTO projects (name) VALUES (project_name);
SET projId = LAST_INSERT_ID();
END IF;

INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, projId, score);
END$$

DELIMITER ;
