SELECT name, COUNT(author) FROM genres
JOIN authorsgenres a on genres.genre_id = a.genre
GROUP BY name;

SELECT COUNT(*) FROM tracks
JOIN albums ON albums.album_id = tracks.album
WHERE relese_year BETWEEN 2019 AND 2020;

SELECT albums.name, AVG(duration) FROM albums
JOIN tracks ON albums.album_id = tracks.album
GROUP BY albums.name;

SELECT nick FROM authors
WHERE 2020 NOT IN (
    SELECT relese_year FROM albums
    JOIN authorsalbums a on albums.album_id = a.album
    WHERE author = authors.author_id
);

SELECT collections.name FROM authorsalbums aa
JOIN albums ON aa.album = albums.album_id
JOIN tracks ON albums.album_id = tracks.album
JOIN trackscollections tc ON tracks.track_id = tc.track
JOIN collections ON tc.collection = collections.collection_id
WHERE aa.author = 2;

SELECT albums.name FROM genres
JOIN authorsgenres ag ON genres.genre_id = ag.genre
JOIN authorsalbums aa ON ag.author = aa.author
JOIN albums on aa.album = albums.album_id
GROUP BY albums.name
HAVING COUNT(genre) > 1;

SELECT name FROM tracks
LEFT JOIN trackscollections tc ON tracks.track_id = tc.track
WHERE collection IS NULL;

SELECT nick FROM tracks
JOIN albums ON tracks.album = albums.album_id
JOIN authorsalbums aa on albums.album_id = aa.album
JOIN authors on aa.author = authors.author_id
WHERE duration = (SELECT MIN(duration) FROM tracks);

SELECT albums.name FROM albums
JOIN tracks ON albums.album_id = tracks.album
GROUP BY albums.name
HAVING COUNT(*) = (SELECT MIN(a.count) FROM (
    SELECT album, COUNT(*) FROM tracks
    GROUP BY album
) a
);
