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

CREATE TABLE Homes (
	home_id INT PRIMARY KEY AUTO_INCREMENT,
    sqft INT,
    occupant_id INT,
    FOREIGN KEY(occupant_id) REFERENCES occupants(occupant_id)
);

INSERT INTO Homes (sqft, occupant_id)
VALUES (1500, 1),
	   (2000, 1),
       (2300, 2),
       (2500, 3),
       (1850, NULL);

SELECT * FROM Homes;

## INNER JOIN
# All columns
SELECT  *
FROM Homes INNER JOIN occupants
ON Homes.occupant_id = occupants.occupant_id;

# Selected columns
SELECT  home_id, sqft, first_name, last_name
FROM Homes INNER JOIN occupants
ON Homes.occupant_id = occupants.occupant_id;

## LEFT JOIN
SELECT  home_id, sqft, first_name, last_name
FROM Homes LEFT JOIN occupants
ON Homes.occupant_id = occupants.occupant_id;