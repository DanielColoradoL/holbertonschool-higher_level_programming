-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT a.title, b.genre_id 
FROM tv_shows a LEFT JOIN tv_show_genres b
ON b.show_id = a.id
ORDER BY a.title, b.genre_id;