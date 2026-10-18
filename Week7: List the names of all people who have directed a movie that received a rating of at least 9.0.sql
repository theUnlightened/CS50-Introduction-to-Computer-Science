-- 9. Names of all people who starred in a movie released in 2004, ordered by birth yearr
SELECT id, name
FROM people
WHERE id IN (
  SELECT id
  FROM movies
  WHERE year = '2004'
)
ORDER BY year;
