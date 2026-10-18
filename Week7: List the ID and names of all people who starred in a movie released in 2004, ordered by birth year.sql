# List the ID and names of all people who starred in a movie released in 2004, ordered by birth year
SELECT id, name 
FROM people
WHERE id IN (
  SELECT 
