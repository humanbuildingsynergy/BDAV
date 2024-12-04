CREATE TABLE offices (
	building_id INT,
    building_name VARCHAR(50) UNIQUE,
    state VARCHAR(10)
);

# Add a Unique constraint after creating a table.
ALTER TABLE offices ADD CONSTRAINT UNIQUE(building_name);

# Add four rows.
INSERT INTO offices
VALUES (100001, "UA_MainLibrary", "AZ"),
	   (100002, "UA_CivilBldg", "AZ"),
       (100003, "UA_CAPLA", "AZ"),
       (100004, "UA_CivilBldg", "AZ");