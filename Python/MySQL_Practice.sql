-- MySQL Monitor --

-- START: open cmd
cd C:\Bitnami\wampstack-x.x.x-x\mysql\bin;
mysql -uroot -p (-hxxxx)
Enter password: ***********

-- CHANGE PW of User
SET PASSWORD = PASSWORD('xxxxxx')
-- OFF
exit

-- CREATE DATABASE
CREATE DATABASE opentutorials;
SHOW DATABASES;
USE opentutorials;
-- CREATE TABLE
CREATE TABLE topic;
SHOW TABLES;
DROP TABLE topic;

-- EXAMPLE:
CREATE TABLE topic(
  id INT(11) NOT NULL AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  description TEXT NULL,
  created DATETIME NOT NULL,
  profile VARCHAR(200) NULL,
  PRIMARY KEY(id)
 );
-- DESCRIBE TABLE: CHECK STRUCTURE of TABLE before INSERT DATA
DESC topic;
-- INSERT
INSERT INTO topic (title,description,created,author,profile) VALUES('MySQL', 'MySQL is...,NOW(),'egoing','developer');
-- SELECT
SELECT id,title,created,author FROM topic;
-- UPDATE
UPDATE topic SET description = 'MySQL is...', title='MySQL' WHERE id=1;
SELECT * FROM topic;
-- DELETE
DELETE FROM topic WHERE id=1;

-- JOIN
SELECT * FROM topic LEFT JOIN author ON topic.author_id = author.id;


-- MySQL Workbench --

-- STORED PROCEDURE
DELIMITER //
CREATE PROCEDURE myProc()
BEGIN
	SELECT * FROM memberTBL WHERE memberName = '당탕이';
  SELECT * FROM productTBL WHERE productName = '냉장고';
END //
DELIMITER ;

CALL myProc() ;
