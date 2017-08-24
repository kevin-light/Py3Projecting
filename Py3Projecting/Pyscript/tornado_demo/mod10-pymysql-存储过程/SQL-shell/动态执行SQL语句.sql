动态执行SQL语句 ： 防止SQL注入
DELIMITER $$
DROP PROCEDURE IF EXISTS proc_sql $$
CREATE PROCEDURE proc_sql()
BEGIN
  DECLARE p1 INT;
  SET p1 = 6;
  SET @p1 = p1;
  
  PREPARE prod FROM 'select * from person where nid > ?';
  EXECUTE prod USING @p1;
  DEALLOCATE PREPARE prod;
END $$
DELIMITER ;

CALL proc_sql()


DELIMITER $$
DROP PROCEDURE IF EXISTS proc_sql $$
CREATE PROCEDURE proc_sql(
  IN strSQL VARCHAR(128),
  IN nid INT
)
BEGIN
  SET @p1 = nid;
  SET @sqll = strSQL;
  
  PREPARE prod FROM @sqll;
  EXECUTE prod USING @p1;
  DEALLOCATE PREPARE prod;
END $$
DELIMITER ;

CALL proc_sql('select * from person where nid > ?',6)