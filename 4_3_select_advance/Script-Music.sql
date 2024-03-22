create database music_shop;

CREATE TABLE IF NOT EXISTS genres (
	id serial primary key,
	genre_name varchar(60) not null
	);

CREATE TABLE IF NOT EXISTS artists (
	id serial primary key,
	artist_name varchar(160) not null
	);

CREATE TABLE IF NOT EXISTS genres_artists (
	genre_id int not null references genres(id),
	artist_id int not null references artists(id),
	constraint pk primary key (genre_id, artist_id)
	);

CREATE TABLE IF NOT EXISTS albums (
	id serial primary key,
	album_name varchar(260) not null,
	album_year int
	);

CREATE TABLE IF NOT EXISTS albums_artists (
	album_id int not null references albums(id),
	artist_id int not null references artists(id)
	constraint pk_albums_artists primary key (album_id, artist_id)
	);

CREATE TABLE IF NOT EXISTS tracks (
	id serial primary key,
	track_name varchar(260) not null,
	duration_min decimal(5,2),
	album_id int references albums(id)
	);

CREATE TABLE IF NOT EXISTS collection_songs (
	id serial primary key,
	collection_name varchar(260) not null,
	collection_year int,
	album_id int references albums(id)
	);

CREATE TABLE IF NOT EXISTS collections_tracks (
	collection_id int not null references collection_songs(id),
	track_id int not null references tracks(id),
	constraint pk_collection_tracks primary key (collection_id, track_id)
	);



