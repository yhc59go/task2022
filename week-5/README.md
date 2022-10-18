# 要求二
* 建立⼀個新的資料庫，取名字為 website。
```
show databases;
CREATE DATABASE website;
show databases;
```

![createDatabaseWebsite](createDatabaseWebsite.PNG)

* 在資料庫中，建立會員資料表，取名字為 member。
```
CREATE TABLE member (
    id bigint PRIMARY KEY AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    follower_count int unsigned NOT NULL DEFAULT 0,
    time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

# 要求三

* 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
```
INSERT INTO member(name,username,password)VALUES ("test", "test", "test");
INSERT INTO member(name,username,password,follower_count)VALUES ("May", "May", "abc54321",50);
INSERT INTO member(name,username,password,follower_count)VALUES ("John", "John56", "John5566",30);
INSERT INTO member(name,username,password,follower_count)VALUES ("Sally", "sally", "sallysally",30);
INSERT INTO member(name,username,password,follower_count)VALUES ("Chris", "Chris01", "12345",5);
```
![InsertMember](InsertMember.PNG)

* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
```
select * from member;
```
![Select](Select.PNG)

* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。
```
select * from member ORDER BY time DESC;
```
![Order](Order.PNG)

* 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，
由近到遠排序。 ( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
```
select * from member ORDER BY time DESC LIMIT 1,3;
```
![Limit](Limit.PNG)

* 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
```
select * from member where username="test";
```
![where](where.PNG)

* 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```
select * from member where username="test" and password="test";
```
![whereAnd](whereAnd.PNG)

* 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
```
UPDATE member SET name="test2" WHERE username="test";
```
![Update](Update.PNG)

# 要求四
* 取得 member 資料表中，總共有幾筆資料 (幾位會員)。
```
SELECT COUNT(id) FROM member;
```
![count](count.PNG)

* 取得 member 資料表中，所有會員 follower_count 欄位的總和。
```
SELECT sum(follower_count) FROM member;
```
![sum](sum.PNG)

* 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```
SELECT avg(follower_count) FROM member;
```
![avg](avg.PNG)

# 要求五
* 在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message 。
```
CREATE TABLE message (
    id bigint PRIMARY KEY AUTO_INCREMENT,
    member_id bigint NOT NULL,
    content varchar(255) NOT NULL,
    like_count int unsigned NOT NULL DEFAULT 0,
    time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(member_id) REFERENCES member(id)
);

INSERT INTO message(member_id,content)VALUES (2, "It's a rainy day!");
INSERT INTO message(member_id,content,like_count)VALUES (1, "It's hard to go to bed early~~",6000);
INSERT INTO message(member_id,content,like_count)VALUES (1, "The weather was suitable for sleep.",56);
INSERT INTO message(member_id,content,like_count)VALUES (3, "I like autumn~",66);
INSERT INTO message(member_id,content,like_count)VALUES (4, "My umbrella turned inside out!",55);
INSERT INTO message(member_id,content,like_count)VALUES (5, "I like to lie in bed and watch Japanese TV dramas.",3000);
INSERT INTO message(member_id,content,like_count)VALUES (5, "This apple is delicious.",2000);
```
![messageTable](messageTable.PNG)

* 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。
```
SELECT member.id,member.name,member.username,message.content,message.like_count,message.time FROM message INNER JOIN member ON message.member_id=member.id;
```
![innerJoin](innerJoin.PNG)

* 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有
留⾔，資料中須包含留⾔者會員的姓名。
```
SELECT member.id,member.name,member.username,message.content,message.like_count,message.time FROM message INNER JOIN member ON message.member_id=member.id where member.username="test";
```
![innerJoin2](innerJoin2.PNG)

* 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中
欄位 username 是 test 的所有留⾔平均按讚數。
```
SELECT avg(message.like_count) FROM message INNER JOIN member ON message.member_id=member.id where member.username="test";
```
![Aggregate](Aggregate.PNG)