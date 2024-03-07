-- A script that lists all records of the second_table
-- Results should display both the score and the name
-- Records should be ordered by score(top first)
-- The database name will be passed as an argument of the mysql command

SELECT score, name
FROM second_table ORDER BY score DESC;
