-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.

 SELECT gn.name, 
 SUM(shw_rting.rate) AS rating 
 FROM tv_genres gn 
 LEFT JOIN tv_show_genres shw_gn ON gn.id = shw_gn.genre_id 
 LEFT JOIN tv_show_ratings shw_rting ON shw_gn.show_id = shw_rting.show_id 
 GROUP BY gn.name 
 ORDER BY rating DESC;
