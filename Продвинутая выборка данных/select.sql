SELECT name, COUNT(author) FROM genres
JOIN authorsgenres a on genres.genre_id = a.genre
GROUP BY name;

SELECT COUNT(*) FROM tracks
WHERE (SELECT relese_year FROM albums WHERE album_id = album) BETWEEN 2019 AND 2020;

SELECT albums.name, AVG(duration) FROM albums
JOIN tracks ON albums.album_id = tracks.album
GROUP BY albums.name;

SELECT nick FROM authors
WHERE 2020 NOT IN (
    SELECT relese_year FROM albums
    JOIN authorsalbums a on albums.album_id = a.album
    WHERE author = authors.author_id
);

SELECT a.name FROM authorsalbums aa
JOIN (
    SELECT b.name, albums.album_id FROM albums
    JOIN (
        SELECT d.name, album FROM tracks
        JOIN (
            SELECT c.name, collection, track FROM trackscollections
            JOIN collections c ON c.collection_id = collection
        ) d ON d.track = track_id
    ) b ON b.album = albums.album_id
) a ON a.album_id = aa.album
WHERE aa.author = 2;

SELECT a.name FROM genres
JOIN (
    SELECT b.name, genre FROM authorsgenres
    JOIN (
        SELECT c.name, author_id FROM authors
        JOIN (
            SELECT name, author FROM authorsalbums
            JOIN albums ON album_id = album
        ) c ON c.author = author_id
    ) b ON b.author_id = author
) a ON a.genre = genre_id
GROUP BY a.name
HAVING COUNT(genre) > 1;

SELECT name FROM tracks
WHERE (
    SELECT COUNT(*) FROM trackscollections
    WHERE track = tracks.track_id
) < 1;

SELECT a.nick FROM tracks
JOIN (
    SELECT b.nick, album_id FROM albums
    JOIN (
        SELECT nick, album FROM authorsalbums
        JOIN authors ON author_id = author
    ) b ON b.album = album_id
) a ON a.album_id = album
WHERE duration = (SELECT MIN(duration) FROM tracks);

SELECT name FROM albums
WHERE album_id IN (
    SELECT album FROM (
        SELECT album, COUNT(*) FROM tracks
        GROUP BY album
    ) a
    WHERE a.count = (
        SELECT MIN(a.count) FROM (
            SELECT album, COUNT(*) FROM tracks
            GROUP BY album
        ) a
));



