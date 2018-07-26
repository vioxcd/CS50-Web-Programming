-- Compound statements
SELECT origin, COUNT(*) FROM flights GROUP BY origin;

-- HAVING is similar to WHERE, but it is used to follow GROUP BY
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;

-- Compound with ()
SELECT * FROM flights WHERE id IN
    (SELECT flights_id FROM passengers
            GROUP BY flights_id
            HAVING COUNT(*) > 1);
