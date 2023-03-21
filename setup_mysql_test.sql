-- CREATES a new MYSQL server database hbnb_test_db
-- CREATES a new user hbnb_test
-- SETS user password to hbnb_test_pwd
-- USER should have all the priviledges only on this database
-- USER should have SELECT priviledge on databasee performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE  USER 
	IF NOT EXISTS 'hbnb_test'@'localhost' 
	IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES
	ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
