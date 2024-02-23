-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS org_dev_db;
CREATE USER IF NOT EXISTS 'org_dev'@'localhost' IDENTIFIED BY 'org_dev_pwd';
GRANT ALL PRIVILEGES ON `org_dev_db`.* TO 'org_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'org_dev'@'localhost';
FLUSH PRIVILEGES;
