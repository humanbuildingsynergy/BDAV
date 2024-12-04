/*
GRUOP BY = aggregate all rows by a specific column
		   often used with aggregate functions
           e.g., SUM(), MAX(), MIN(), AVG(), COUNT(), ...
*/
SELECT * FROM Homes;

# GROUP BY
SELECT AVG(sqft), floor_number
FROM Homes
GROUP BY floor_number;

# HAVING
SELECT AVG(sqft), floor_number
FROM Homes
GROUP BY floor_number
HAVING floor_number > 1;