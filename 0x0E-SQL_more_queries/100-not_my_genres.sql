-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

SELECT gn.name FROM tv_genres gn 
WHERE gn.name NOT IN (
    SELECT gn.name FROM tv_genres gn 
    LEFT JOIN tv_show_genres shw_gn ON gn.id = shw_gn.genre_id 
    LEFT JOIN tv_shows shws ON shws.id = shw_gn.show_id 
    WHERE shws.title = "Dexter"
    ) 
    ORDER BY gn.name ASC;