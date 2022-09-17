-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- USE hbtn_0d_tvshows_rate;
SELECT shws.title, 
SUM(shw_rting.rate) AS rating 
FROM tv_shows shws 
LEFT JOIN tv_show_ratings shw_rting ON shw_rting.show_id = shws.id 
GROUP BY shws.title 
ORDER BY rating DESC;
