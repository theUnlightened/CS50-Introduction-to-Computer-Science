SELECT AVG(energy)
FROM songs
JOIN artists ON songs.artist_id = artists.id
WHERE artist_name = 'Druke';
