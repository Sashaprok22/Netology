CREATE TABLE IF NOT EXISTS Genres(
	genre_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS Authors(
	author_id SERIAL PRIMARY KEY,
	nick VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS AuthorsGenres(
	author INTEGER NOT NULL REFERENCES Authors(author_id),
	genre INTEGER NOT NULL REFERENCES Genres(genre_id),
	CONSTRAINT ag_id PRIMARY KEY (author, genre)
);

CREATE TABLE IF NOT EXISTS Albums(
	album_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	relese_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS AuthorsAlbums(
	album INTEGER NOT NULL REFERENCES Albums(album_id),
	author INTEGER NOT NULL REFERENCES Authors(author_id),
	CONSTRAINT aa_id PRIMARY KEY (album, author)
);

CREATE TABLE IF NOT EXISTS Tracks(
	track_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	duration INTEGER NOT NULL,
	album INTEGER NOT NULL REFERENCES Albums(album_id)
);

CREATE TABLE IF NOT EXISTS Collections(
	collection_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	relese_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS TracksCollections(
	collection INTEGER NOT NULL REFERENCES Collections(collection_id),
	track INTEGER NOT NULL REFERENCES Tracks(track_id),
	CONSTRAINT tc_id PRIMARY KEY (collection, track)
);