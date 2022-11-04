INSERT INTO genres(name) VALUES('Pop');
INSERT INTO genres(name) VALUES('Rap');

INSERT INTO collections(name, relese_year) VALUES('Throwback Hits', 2020);
INSERT INTO collections(name, relese_year) VALUES('Halloween Pop Party', 2021);
INSERT INTO collections(name, relese_year) VALUES('2021 Mega Hits', 2021);
INSERT INTO collections(name, relese_year) VALUES('Golden Hits', 2020);
INSERT INTO collections(name, relese_year) VALUES('Best Clean Hits', 2021);
INSERT INTO collections(name, relese_year) VALUES('Rock Now', 2020);
INSERT INTO collections(name, relese_year) VALUES('Happy Pop Hits', 2021);
INSERT INTO collections(name, relese_year) VALUES('Ready2go', 2020);



INSERT INTO authors(nick) VALUES('The Weekend');
INSERT INTO authorsgenres(author, genre) VALUES(1, 1);

INSERT INTO albums(name, relese_year) VALUES('The Highlights', 2021);
INSERT INTO authorsalbums(album, author) VALUES(1, 1);

INSERT INTO tracks(name, duration, album) VALUES('Save Your Tears', 215, 1);
INSERT INTO tracks(name, duration, album) VALUES('Blinding Lights', 200, 1);
INSERT INTO tracks(name, duration, album) VALUES('In Your Eyes', 237, 1);
INSERT INTO tracks(name, duration, album) VALUES('Can`t Feel My Face', 213, 1);
INSERT INTO tracks(name, duration, album) VALUES('I Feel It Coming', 269, 1);


INSERT INTO authors(nick) VALUES('Lady Gaga');
INSERT INTO authorsgenres(author, genre) VALUES(2, 1);

INSERT INTO albums(name, relese_year) VALUES('The Fame Monster', 2009);
INSERT INTO authorsalbums(album, author) VALUES(2, 2);

INSERT INTO tracks(name, duration, album) VALUES('Bad Romance', 294, 2);
INSERT INTO trackscollections(collection, track) VALUES(1, 6);


INSERT INTO authors(nick) VALUES('Imagine Dragons');
INSERT INTO authorsgenres(author, genre) VALUES(3, 1);

INSERT INTO albums(name, relese_year) VALUES('Night Visions', 2013);
INSERT INTO authorsalbums(album, author) VALUES(3, 3);

INSERT INTO tracks(name, duration, album) VALUES('Radioactive', 188, 3);
INSERT INTO trackscollections(collection, track) VALUES(2, 7);

INSERT INTO authors(nick) VALUES('-krxt');
INSERT INTO authorsgenres(author, genre) VALUES(4, 2);

INSERT INTO albums(name, relese_year) VALUES('13 причин потерять всех', 2018);
INSERT INTO authorsalbums(album, author) VALUES(4, 4);