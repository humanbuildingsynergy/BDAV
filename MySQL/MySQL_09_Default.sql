CREATE TABLE offices (
	office_id INT,
    office_name VARCHAR(50),
    state_abb VARCHAR(5) DEFAULT "AZ",
	location VARCHAR(50)
);

# Assgining the default value to a column
ALTER TABLE offices ALTER state_abb SET DEFAULT "AZ";

# Add new rows
INSERT INTO offices VALUES
	(10001, "Office_01", "NV", "Las Vegas"),
    (10002, "Office_01", "AZ", "Oro Valley");
