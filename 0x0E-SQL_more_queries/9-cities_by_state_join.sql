-- a script that lists all cities contained in the database hbtn_0d_usa.

-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement

 SELECT cty.id, cty.name, st.name from hbtn_0d_usa.cities cty INNER JOIN hbtn_0d_usa.states st ON cty.state_id = st.id ORDER BY cty.id ASC;
