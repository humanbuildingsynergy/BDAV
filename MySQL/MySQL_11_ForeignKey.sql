DROP TABLE Homes;
DROP TABLE occupants;

CREATE TABLE occupants(
	occupant_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(20),
    last_name VARCHAR(20)
);

INSERT INTO occupants (first_name, last_name)
VALUES ('John','A'),
	   ('John','B'),
       ('John','C');

SELECT * FROM occupants;
       
# Let's recreate the Homes table with the foreign key from the occupants table.
#DROP TABLE Homes;

CREATE TABLE Homes (
	home_id INT PRIMARY KEY AUTO_INCREMENT,
    sqft INT,
    occupant_id INT,
    FOREIGN KEY(occupant_id) REFERENCES occupants(occupant_id)
);

# Delete the existing foreign key contraint
ALTER TABLE Homes
DROP FOREIGN KEY homes_ibfk_1;

# Add the foreign key constraint later
ALTER TABLE Homes 
ADD CONSTRAINT fk_occupant_id # this line is not necessay unless you want to name it.
FOREIGN KEY(occupant_id) REFERENCES occupants(occupant_id);

# Add rows into the Homes table.
INSERT INTO Homes (sqft, occupant_id)
VALUES (1500, 1),
	   (2000, 1),
       (2300, 2),
       (2500, 3);

SELECT * FROM Homes;

DELETE FROM occupants WHERE occupant_id = 1;