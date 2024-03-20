--  lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT b.title
FROM tv_show_genres c 
INNER JOIN tv_genres a ON c.genre_id = a.id
INNER JOIN tv_shows b ON c.show_id = b.id
WHERE (a.name = "Comedy ")
ORDER BY b.title ASC;