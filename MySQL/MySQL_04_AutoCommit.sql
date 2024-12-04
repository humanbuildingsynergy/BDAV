USE BDAV;

SELECT * FROM Homes;

SET AUTOCOMMIT = OFF; # The transaction will not be saved automatically

DELETE FROM Homes;
SELECT * FROM Homes;

ROLLBACK;
SELECT * FROM Homes;

DELETE FROM Homes;
SELECT * FROM Homes;
COMMIT;

SELECT * FROM Homes;