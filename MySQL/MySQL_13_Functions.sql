SELECT * FROM Homes;

# COUNT
SELECT COUNT(sqft) FROM Homes;
SELECT COUNT(sqft) AS Num_sqft FROM Homes;

# MAX
SELECT MAX(sqft) FROM Homes;
SELECT MAX(sqft) AS "Maximum" FROM Homes;

# MIN
SELECT MIN(sqft) FROM Homes;
SELECT MIN(sqft) AS "SQFT Min" FROM Homes;

# AVG
SELECT AVG(sqft) FROM Homes;
SELECT AVG(sqft) AS "SQFT AVG" FROM Homes;

# SUM
SELECT SUM(sqft) FROM Homes;
SELECT SUM(sqft) AS "SUM" FROM Homes;

# CONCAT
SELECT CONCAT(first_name, " ", last_name) AS full_name
FROM occupants;