-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.
DELIMITER //

CREATE TRIGGER reset_valid_email_on_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email is being changed (i.e., it's different from the current value)
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;  -- Reset valid_email to 0 when email changes
    END IF;
END //

DELIMITER ;
