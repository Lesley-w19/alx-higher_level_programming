--  a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)
SELECT score, name  FROM second_table GROUP BY score, name ORDER BY score DESC;
