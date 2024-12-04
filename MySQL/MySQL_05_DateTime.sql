CREATE TABLE date_time(
	my_date DATE,
    my_time TIME,
    my_datetime DATETIME
);

INSERT INTO date_time VALUES(
	CURRENT_DATE(),
    CURRENT_TIME(),
    NOW()
);

SELECT * FROM date_time