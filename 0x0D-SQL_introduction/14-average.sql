-- A script that computes the score average of all records in the second_table
-- Result column name should be average
-- The database name will be passed as an argument of the mysql command

SELECT AVG(score)
AS Average
FROM second_table;
