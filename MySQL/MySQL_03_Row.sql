# Comments

# Single-line comments
-- SELECT * FROM Homes; 
# SELECT * FROM Homes;

/* Multi-line comments
You can use multiple line comments with /* and */


USE BDAV;

INSERT INTO Homes 
VALUES (100001, "2024-09-30", "4B", 4, 73942.18);

SELECT * FROM Homes;

INSERT INTO Homes 
VALUES (100002, "2024-09-30", "4A", 1, 123456.23),
	   (100003, "2024-08-14", "4B", 1, 6293.72),
       (100004, "2024-08-01", "3A", 5, 16993.72),
       (100005, "2023-07-03", "4A", 1, 42812.12);
INSERT INTO Homes (building_id, climate_zone, num_windows)
VALUES (100006, "2A", 4);

SELECT * FROM Homes;
SELECT climate_zone, num_windows FROM Homes;
SELECT * FROM Homes WHERE num_windows = 1;
SELECT * FROM Homes WHERE TOTBTUSPH IS NULL;

SET SQL_SAFE_UPDATES = 0; # (turn off the safe update mode)

UPDATE Homes SET TOTBTUSPH = 8818.47 WHERE building_id = 100006;

UPDATE Homes SET TOTBTUSPH = 8818.47,
				 num_windows = 3
			 WHERE building_id = 100006;

DELETE FROM Homes WHERE building_id = 100006;

SELECT * FROM Homes;
