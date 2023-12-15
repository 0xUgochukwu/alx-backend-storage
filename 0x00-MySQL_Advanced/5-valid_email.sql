-- creates a trigger that resets the attribute valid_email only when the email has been changed.

DELEMITER //
CREATE TRIGGER after_email_update
BEFORE UPDATE ON users
BEGIN
  IF NEW.email <> OLD.email
    SET NEW.valid_email = 0;
  END IF;
END //
DELEMITER;

