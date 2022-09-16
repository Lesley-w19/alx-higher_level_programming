-- a script that creates the table unique_id on your MySQL server.

-- unique_id description:
-- id INT with the default value 1 and must be unique
-- name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1, name VARCHAR(256) NOT NULL);
ALTER TABLE unique_id ADD CONSTRAINT unique_id_constraint UNIQUE KEY(id);