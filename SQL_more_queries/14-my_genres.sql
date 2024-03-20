-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT a.name
FROM tv_show_genres c 
INNER JOIN tv_genres a ON c.genre_id = a.id
INNER JOIN tv_shows b ON c.show_id = b.id
WHERE (b.title = "Dexter")
ORDER BY a.name ASC;
