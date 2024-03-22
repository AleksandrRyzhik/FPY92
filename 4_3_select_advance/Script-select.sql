
-- самый длинныйтрек
select track_name , duration_min 
from tracks t
order by duration_min desc limit 1;

-- Название треков, продолжительность которых 
--не менее 3,5 минут
select track_name , duration_min 
from tracks t
where duration_min >= 3.5;

--Названия сборников, вышедших в период 
--с 2018 по 2020 год включительно.
SELECT *
FROM collection_songs cs 
where cs.collection_year between 2018 and 2020;

--Исполнители, чьё имя состоит из одного слова.
select *
from artists a2
where artist_name  not like '% %'

--Название треков
--, которые содержат слово «мой» или «my».
select t.track_name  from tracks t 
where t.track_name like '%my%' 
or t.track_name like '%мой%' 

--ЗАДАНИЕ 3

--количество исполнителей в каждом жанре
select g.genre_name 
, count(*) as num_artists
from genres_artists ga 
join genres g on ga.genre_id = g.id 
group by g.genre_name 

--Количество треков, вошедших в альбомы 2019–2020 годов.
select count(*) num_tracks
from tracks t 
join albums a 
on t.album_id = a.id 
where album_year between 2019 and 2020

--Средняя продолжительность треков по каждому альбому.
select a.album_name 
, avg(t.duration_min) avg_duration 
from tracks t 
join albums a 
on t.album_id = a.id 
group by a.album_name 

--Все исполнители, которые не выпустили альбомы в 2020 году.
select distinct a.artist_name 
from artists a 
join albums_artists aa on a.id = aa.artist_id 
join albums a2 on aa.album_id = a2.id 
where a2.album_year != 2020

--Названия сборников, в которых присутствует конкретный исполнитель Deftones.
select cs.collection_name 
from collection_songs cs
join albums a on cs.album_id = a.id 
join albums_artists aa on a.id = aa.album_id 
join artists a2 on aa.artist_id = a2.id 
where a2.artist_name = 'deftones'
