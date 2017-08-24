创建数据库utf8  CREATE DATABASE testdb DEFAULT CHARSET utf8 COLLATE utf8_general_ci

SELECT * 
FROM person LEFT JOIN part ON person.`part_id` = part.`id`
LEFT JOIN color ON person.`nid` = color.`nid`

SELECT person.`nid`,person.`name`,part.`caption` 
FROM person RIGHT JOIN part ON person.`part_id` = part.`id`

SELECT person.`nid`,person.`name`,part.`caption` 
FROM person INNER JOIN part ON person.`part_id` = part.`id`

 不带参数存储过程
DELIMITER $$
CREATE PROCEDURE proc_p2()
BEGIN
    SELECT * FROM color;
END $$
DELIMITER ;

DROP PROCEDURE IF EXISTS proc_p1;
CREATE PROCEDURE proc_p1()
BEGIN
    SELECT * FROM color;
END
调用存储过程
CALL proc_p1();
删除
DROP PROCEDURE proc_p1;


带 IN 函数的存储过程
DELIMITER $$		-- 设置SQL语句结束符号为 $$
DROP PROCEDURE IF EXISTS proc_p1 $$   -- 如果proc_p1存在先删除
CREATE PROCEDURE proc_p1(
  IN i1 INT  			-- 定义传入 i1 为整形 参数
)
BEGIN
  DECLARE d1 INT;		-- 定义变量 d1
  DECLARE d2 INT DEFAULT 3; 	-- 定义变量 d3 默认值为3
  SET d1 = i1 + d2;
  SELECT * FROM person WHERE nid > d1;
END $$
DELIMITER ;     -- 设置SQL语句结束符号为默认的 ;
调用查询 i1 = 1 的结果
CALL proc_p1(1)


带 IN,INOUT,OUT 函数的存储过程

DELIMITER $$
DROP PROCEDURE IF EXISTS proc_p5 $$
CREATE PROCEDURE proc_p5(
  IN i1 INT,
  INOUT ii INT,
  OUT i2 INT
)
BEGIN
  DECLARE d2 INT DEFAULT 3;
  SET ii = ii + 1;
  SELECT * FROM person;
  
  IF i1 = 1 THEN
    SET i2 = 100 + d2;
  ELSEIF i1 = 2 THEN
    SET i2 = 200 + d2;
  ELSE
    SET i2 = 300 + d2;
  END IF;
END $$  
DELIMITER ;

SET @o = 5;
CALL proc_p5(2,@o,@u);
SELECT @o,@u;




