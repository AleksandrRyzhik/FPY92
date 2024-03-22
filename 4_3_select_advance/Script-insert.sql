
delete from collections_tracks; 
delete from collection_songs;
delete from albums_artists ;
delete from genres_artists ;
delete from artists ;
delete from genres ;
delete from tracks ;
delete from albums ;

insert into artists(artist_name)
values('deftones'), ('the strokes')
, ('rage against the machine')
, ('red hot chilli peppers');

insert into genres(genre_name)
values('nu metal'), ('indie rock')
, ('funk metal'), ('funk');

insert into albums(album_name, album_year)
values('around the fur', 1997)
, ('the new abnormal', 2020)
, ('rage against the machine', 1992)
, ('stadium arcadium', 2006);

insert into tracks(track_name, duration_min, album_id)
values ('killing in the name', 5, 19)
, ('bombtrack', 4, 19)
, ('my own summer (shove it)', 3.5, 17)
, ('be quiet and drive (far away)', 5, 17)
, ('the adults are talking', 5, 18)
, ('brooklyn bridge to chorus', 4, 18)
, ('snow (hey oh)', 5.5, 20)
, ('stadium arcadium', 5, 20);

insert into collection_songs (collection_name
, collection_year, album_id)
values ('metals', 1998, 17)
, ('indierock', 2020, 18)
, ('metal', 1993, 19), ('funks', 2008, 20);

insert into albums_artists 
values(17, 14), (18, 15), (19, 16), (20, 17);

insert into collections_tracks
values (17, 51), (18, 53), (19, 49), (20, 56);

insert into genres_artists 
values (13, 14), (14, 15), (15, 16), (16, 17)







 