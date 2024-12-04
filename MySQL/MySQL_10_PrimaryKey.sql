DROP TABLE occupants;

CREATE TABLE occupants(
	ssn VARCHAR(11) PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20)
);

# You can later add the PRIMARY KEY Constraint, of course.
#ALTER TABLE occupants ADD CONSTRAINT PRIMARY KEY (ssn);

INSERT INTO occupants 
VALUES ('111-11-1111','John','Doe'),
	   ('111-11-1112','John','Doe'),
       ('111-11-1113','Doe','John');

SELECT * FROM occupants;