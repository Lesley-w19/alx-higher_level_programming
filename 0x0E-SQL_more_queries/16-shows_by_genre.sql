-- a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

 SELECT shws.title, gn.name FROM tv_shows shws LEFT JOIN tv_show_genres shw_gn ON shw_gn.show_id = shws.id LEFT JOIN tv_genres
 gn ON gn.id = shw_gn.genre_id  ORDER BY shws.title ASC, gn.name ASC;
