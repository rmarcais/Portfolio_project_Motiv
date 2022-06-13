-- This script prepares a MySQL server for the project.
-- Create the database hbnb_dev_db.
CREATE DATABASE IF NOT EXISTS motiv_dev_db;
-- Create a user
CREATE USER IF NOT EXISTS 'motiv_dev'@'localhost' IDENTIFIED BY 'motiv';
-- Set all privileges.
GRANT ALL PRIVILEGES ON motiv_dev_db.* TO 'motiv_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'motiv_dev'@'localhost';
