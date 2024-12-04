DROP TABLE offices;

CREATE TABLE offices (
	office_id INT,
    office_name VARCHAR(50),
    state_abb VARCHAR(5),
	location VARCHAR(50)
    # CHECK (state_abb = "AZ")
	# CONSTRAINT chk_az CHECK (state_abb = "AZ")
);

# Adding 'CHECK' to an existing table.
ALTER TABLE offices ADD CONSTRAINT chk_az CHECK (state_abb="AZ");

# Add new rows
INSERT INTO offices VALUES
	(10001, "Office_01", "NV", "Las Vegas"),
    (10002, "Office_01", "AZ", "Oro Valley");
