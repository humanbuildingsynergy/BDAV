# adding a new column
ALTER TABLE Homes 
ADD COLUMN floor_number INT AFTER sqft;

SELECT * FROM Homes;

# Updating the value in the table (try this query multiple times to fill out the column) 
UPDATE homes SET floor_number = 3
WHERE home_id = 5;

SELECT * FROM Homes;

# AND
SELECT * FROM Homes WHERE sqft > 2000 AND floor_number < 3;

# OR
SELECT * FROM Homes WHERE sqft > 2000 OR floor_number > 3;

# NOT
SELECT * FROM Homes WHERE NOT sqft > 2000;

# IN
SELECT * FROM Homes WHERE floor_number in (1, 2);