-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

SELECT shws.title FROM tv_shows shws 
WHERE shws.title NOT IN 
(
    SELECT shws.title FROM tv_shows shws 
    LEFT JOIN tv_show_genres shw_gn ON shws.id = shw_gn.show_id
    LEFT JOIN tv_genres gn ON gn.id = shw_gn.genre_id 
    WHERE gn.name = "Comedy"
    )
     ORDER BY shws.title ASC;
