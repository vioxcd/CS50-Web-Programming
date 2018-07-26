-- Update entry and set new values
UPDATE flights
    SET duration = 430
    WHERE origin = 'New York'
    AND destination = 'London';
