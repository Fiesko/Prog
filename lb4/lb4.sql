-- Задание 1
EXPLAIN SELECT * FROM Track WHERE genre = 'Рок';
CREATE INDEX idx_track_genre ON Track(genre);
-- Задание 2	
CREATE VIEW v_user_playlist AS
SELECT 
    User1.username,
    Playlist.playlist_name,
    Track.track_title,
    Track.duration,
    Track.genre,
    Artist.artist_name,
    Album.album_title
FROM User1
JOIN Playlist ON User1.user_id = Playlist.User1_user_id
JOIN Playlist_track ON Playlist.playslist_id = Playlist_track.Playlist_playslist_id
JOIN Track ON Playlist_track.Track_track_id = Track.track_id
JOIN Artist_track ON Track.track_id = Artist_track.Track_track_id
JOIN Artist ON Artist_track.Artist_artist_id = Artist.artist_id
JOIN Album ON Track.Album_album_id = Album.album_id;
SELECT * FROM v_user_playlist LIMIT 10;