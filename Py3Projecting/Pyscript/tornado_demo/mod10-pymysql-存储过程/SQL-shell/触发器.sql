插入前的触发器
DELIMITER $$
CREATE TRIGGER tri_before_insert_color2 BEFORE INSERT ON color FOR EACH ROW
BEGIN
  INSERT INTO person(NAME,email,part_id) VALUES('ttt','ttt.com',1);
END $$
DELIMITER ;

INSERT INTO color(title) VALUE('222'),('333')

插入前的触发器2
DELIMITER $$
DROP TRIGGER IF EXISTS tri_before_insert_color $$	
CREATE TRIGGER tri_before_insert_color BEFORE INSERT ON color FOR EACH ROW
BEGIN
  INSERT INTO person(NAME,email,part_id) VALUES('ttt','ttt.com',1);
END $$
DELIMITER ;

INSERT INTO color(title) VALUE('222'),('333')

删除前的触发器
DELIMITER $$
DROP TRIGGER IF EXISTS tri_befor_insert_color $$
CREATE TRIGGER tri_before_insert_color BEFORE DELETE ON color FOR EACH ROW
BEGIN
  INSERT INTO person(NAME,email) VALUES(old.title,old.title);
END $$
DELIMITER ;

delete from color where nid = 7



函数
select  left('kevin',2),right('kevin',2),insert('kevin',2,2,'666'),char_length('kevin'),length('kevin'),concat('aa','bb','cc'),concat_ws('-','aa','bb','cc')

自定义行数
delimiter $$
drop function if exists f1 $$
create function f1(
	i1 int,
	i2 int)
returns int
begin
	declare num int;
	set num = i1 + i2;
	return(num);
end $$
delimiter ;

select f1(11,nid),nid from person

事物-- 支持事务的存储过程
delimiter $$
create PROCEDURE p1(
    OUT p_return_code tinyint
)
BEGIN 
  DECLARE exit handler for sqlexception 
  BEGIN 
    -- ERROR 
    set p_return_code = 1; 
    rollback; 		-- 回滚
  END; 
 
  DECLARE exit handler for sqlwarning 
  BEGIN 
    -- WARNING 
    set p_return_code = 2; 
    rollback; 
  END; 
 
  START TRANSACTION; 	-- 开始事物
    update person set email='qq.com' where nid=6;
    UPDATE person SET email='qq.com' WHERE nid=11;
  COMMIT; 		-- 提交
 
  -- SUCCESS 
  set p_return_code = 0; 
 
END$$
delimiter ;

call p1(@n);
select @n;