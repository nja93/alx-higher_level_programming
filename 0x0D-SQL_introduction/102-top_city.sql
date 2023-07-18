-- Script that displays the top 3 of cities temperature during July and Ausgut, decending order of temp

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
