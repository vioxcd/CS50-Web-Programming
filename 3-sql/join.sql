-- JOIN ON keywords
-- and primary-foreign key matching

-- This one is called INNER JOIN
SELECT origin, destination, name
    FROM flights JOIN passengers
    ON passengers.flights_id = flights.id;

SELECT origin, destination, name
    FROM flights JOIN passengers
    ON passengers.flights_id = flights.id
    WHERE name = 'Alice';

-- this one is LEFT JOIN
-- return all entries from LEFT-side table
-- equivalent to RIGHT JOIN
SELECT origin, destination, name
    FROM flights LEFT JOIN passengers
    ON passengers.flights_id = flights.id;
