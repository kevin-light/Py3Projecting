mysql创建索引-提高查询效率
http://www.cnblogs.com/wupeiqi/articles/5716963.html
http://www.cnblogs.com/wupeiqi/articles/5713323.html

创建索引：

1、普通索引
普通索引仅有一个功能：加速查询
CREATE TABLE in1(
    nid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(32) NOT NULL,
    email VARCHAR(64) NOT NULL,
    extra TEXT,
    INDEX ix_name (NAME)
)
创建表 + 索引

CREATE INDEX person ON ix_index(NAME)  -- 添加索引

DROP index_name ON table_name;				-- 删除索引

SHOW INDEX FROM person;				-- 查看表的索引

DESC person
SHOW CREATE TABLE person

CREATE INDEX ix_index ON person(NAME)

EXPLAIN SELECT * FROM person WHERE email = 'q'   - TYPE=ALL 全表扫描
EXPLAIN SELECT NAME FROM person WHERE NAME = 'aaa'   - TYPE=ref 普通索引

2、唯一索引
唯一索引有两个功能：加速查询 和 唯一约束（可含null）
CREATE TABLE person2(
  nid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  NAME VARCHAR(32) NOT NULL,
  email VARCHAR(32),
  extra TEXT,
  UNIQUE(NAME)
  )ENGINE=INNODB DEFAULT CHARSET=utf8;
  
 INSERT INTO person2(nid,NAME,email) VALUES(1,'kevin','kevin.com'),(2,'alvin','alvin.com')
 
 
 EXPLAIN SELECT * FROM person2 WHERE email='k'       -- type=all   全表扫描 效率低   
  EXPLAIN SELECT * FROM person2 WHERE NAME='kevin'   -- type=const 查找效率最高
 
  
3、主键索引

主键有两个功能：加速查询 和 唯一约束（不可含null）
  -- 通过主键查找
  
 4、组合索引
组合索引是将n个列组合成一个索引
其应用场景为：频繁的同时使用n列来进行查询，如：where n1 = 'alex' AND n2 = 666。
  创建索引 创建表时：unique（name,email)，给表添加索引
  
CREATE TABLE person2(
  nid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  NAME VARCHAR(32) NOT NULL,
  email VARCHAR(32),
  extra TEXT,
  UNIQUE(NAME，email)
  )ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE INDEX ix_index ON person2(NAME,email)
SELECT * FROM person2 NAME = 'name' 			  - 走索引
SELECT * FROM person2 NAME = 'name' AND email = 'email'   - 走索引
SELECT * FROM person2 email = 'email'			  - 不走索引 （最左前缀）
