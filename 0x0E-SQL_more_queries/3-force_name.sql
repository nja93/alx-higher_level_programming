-- create table force_name on my MySQL server
-- description id(INT) name(VARCHAR(256)) cannot be NULL
-- If the table force_name already exists, your script should not fail

CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
);
