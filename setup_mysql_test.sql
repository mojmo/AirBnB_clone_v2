-- a script that prepares a MySQL server for the project

-- Create database `hbnb_test_db` if it doesn't exist
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create user `hbnb_test` if it doesn't exist and set password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the hbnb_test_db database to the hbnb_test user
GRANT ALL PRIVILEGES 
    ON `hbnb_test_db`.*
    TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- Grant the SELECT privilege on the performance_schema database to the hbnb_test user
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
