-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT b.title, a.name
FROM tv_show_genres c
RIGHT JOIN tv_shows b ON c.show_id = b.id
LEFT JOIN tv_genres a ON c.genre_id = a.id
ORDER BY b.title, a.name;