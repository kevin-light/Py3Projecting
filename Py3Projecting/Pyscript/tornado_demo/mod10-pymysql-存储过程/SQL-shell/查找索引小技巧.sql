小技巧：
http://www.cnblogs.com/wupeiqi/articles/5716963.html
用limit查询比较快
SELECT * FROM person WHERE nid = 6 LIMIT 1;

 %号在后面-走索引-查找快
SELECT * FROM person WHERE NAME LIKE 'aa%'  --  查找快
SELECT * FROM person WHERE NAME LIKE '%aa'  --  查找慢

 reverse号在后面-走索引-查找快
SELECT * FROM person WHERE REVERSE(NAME) = 'aa'  --  查找快
SELECT * FROM person WHERE NAME = REVERSE('aa')  --  查找慢

查找类型不一致不走索引
 > <> 不走索引

- ORDER BY -- 
    SELECT email FROM tb1 ORDER BY NAME DESC;  - 不走索引
    当根据索引排序时候，选择的映射如果不是索引，则不走索引
    特别的：如果对主键排序，则还是走索引：
     SELECT * FROM tb1 ORDER BY nid DESC;    - 走索引
     SELECT NAME FROM tb1 ORDER BY NAME DESC;   - 走name索引

- 组合索引最左前缀
    如果组合索引为：(NAME,email)
    NAME AND email       -- 使用索引
    NAME                 -- 使用索引
    email                -- 不使用索引
    
 组合索引 - 效率高
 覆盖索引
 索引合并
 
 6、其他注意事项
 - 避免使用select *
- COUNT(1)或count(列) 代替 COUNT(*)
- 创建表时尽量时 CHAR 代替 VARCHAR
- 表的字段顺序固定长度的字段优先 - 放前面
- 组合索引代替多个单列索引（经常使用多个条件查询时）
- 尽量使用短索引
- 使用连接（JOIN）来代替子查询(Sub-Queries)
- 连表时注意条件类型需一致
- 索引散列值（重复少）不适合建索引，例：性别不适合


SELECT * FROM tb LIMIT 2000000,5;
每页10条数据，显示上一页，下一页 的优化方案：
SELECT nid,NAME,email FROM tb WHERE ORDER BY nid LIMIT 10;
SELECT nid,NAME,email FROM tb WHERE ORDER BY nid DESC LIMIT 10;
动态最小ID: 
SELECT nid FROM (SELECT nid FROM tb1 WHERE nid <9989 ORDER BY nid DESC LIMIT 30) AS A ORDER BY nid ASC LIMIT 1
SELECT nid NAME,email FROM tb WHERE nid < 动态最小ID ORDER BY nid DESC LIMIT 10;

总结：

