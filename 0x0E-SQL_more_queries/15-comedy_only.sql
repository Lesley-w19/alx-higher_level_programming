--  a script that lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT shws.title FROM tv_shows shws LEFT JOIN tv_show_genres shw_gn ON shw_gn.show_id = shws.id LEFT JOIN tv_genres gn ON gn.id = shw_gn.genre_id WHERE gn.name = "Comedy" ORDER BY shws.title ASC;
