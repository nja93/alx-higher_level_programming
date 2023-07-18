-- Script to create the table first_table
-- Shoulf not fail if the table exists
-- attributes include name and id

CREATE TABLE IF NOT EXISTS first_table(
    id INT,
    name VARCHAR(256)
);
