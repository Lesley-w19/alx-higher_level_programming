-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download

-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- USE hbtn_0d_tvshows;

SELECT shws.title, shw_g.genre_id FROM tv_shows shws INNER JOIN tv_show_genres shw_g ON shw_g.show_id = shws.id ORDER BY shws.title ASC, shw_g.genre_id ASC;
