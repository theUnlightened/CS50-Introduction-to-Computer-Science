-- 4. Number of movies with a 10.0 rating
SELECT COUNT(tltle)
FROM movies
WHERE id IN (
    SELECT movie_id
    FROM ratings
    WHERE rating = '10.0'
);
