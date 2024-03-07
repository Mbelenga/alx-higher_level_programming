-- A script that lists all records in the table
-- Don’t list rows without a name value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
