-- Indexes are used to retrieve data faster than normal search queries
-- The downside of using indexes is, it takes more time updating the table when it needed an update

-- duplicate allowed
CREATE INDEX index_name
    ON table_name(column1, column2);

-- no duplicate allowed
CREATE UNIQUE INDEX index_name
    ON table_name(column1, column2);
