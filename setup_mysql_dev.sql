-- CREATES a new MYSQL server database hbnb_dev_db
-- CREATES a new user hbnb_dev
-- SETS user password to hbnb_dev_pwd
-- USER should have all the priviledges only on this database
-- USER should have SELECT priviledge on databasee performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE  USER 
	IF NOT EXISTS 'hbnb_dev'@'localhost' 
	IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES
	ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
