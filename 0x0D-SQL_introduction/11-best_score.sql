-- Script that lists all records with a score >= 10 in second_table
-- Results to display both the score and the name (in this order)
-- Records to be ordered by score (top first)

SELECT score, name
FROM second_table
WHERE score >= 10 ORDER BY score DESC;
