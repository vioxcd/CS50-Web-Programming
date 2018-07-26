-- Average
SELECT AVG(duration) FROM flights;

SELECT AVG(duration) FROM flights WHERE origin = 'New York';

-- Count entry with property
SELECT COUNT(*) FROM flights;

-- Min / Max
SELECT MIN(duration) FROM flights;

-- In - several selector
SELECT * FROM flights WHERE origin IN ('New York', 'Lima');

-- String Matching | LIKE
SELECT * FROM flights WHERE origin LIKE '%a%'
