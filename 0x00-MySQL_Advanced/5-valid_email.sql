-- Email validation to sent 
DELIMITER $$

CREATE TRIGGER email_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		IF NEW.valid_email = 0 THEN
			SET NEW.valid_email = 1;
		ELSE
			SET NEW.valid_email = 0;
		END IF;
	END IF;
END$$

DELIMITER ;
