CREATE TABLE apartments (
	apartment_id INT,
    apartment_name VARCHAR(50) NOT NULL,
    city VARCHAR(25)
);

# Apply the NULL NULL contraint to the column
ALTER TABLE apartments MODIFY city VARCHAR(25) NOT NULL;

# You'll get an error as NULL is provided in the 'apartment_name' column.
INSERT INTO apartments
VALUES (100001, NULL, "Tucson");
