-- a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
SELECT shws.title, shw_gn.genre_id FROM tv_shows shws LEFT JOIN tv_show_genres shw_gn ON shws.id = shw_gn.show_id WHERE shw_gn.genre_id IS NULL ORDER BY shws.title ASC, shw_gn.genre_id ASC;