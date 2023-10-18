-- Lists all the cities in California in the database
SELECT id, name FROM cities
WHERE state_id = 1
GROUP BY id ASC;
