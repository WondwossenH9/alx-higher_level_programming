-- Lists all records of the second_table with a name value in MySQL server.
-- Records are in descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
