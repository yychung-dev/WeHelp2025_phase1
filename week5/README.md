# Week 5 Assignment (Task 2 - Task 5)

## Task 2
1. CREATE DATABASE website;    

<img src="screenshots/2-1.png" width="600" height="600" />

2. USE website;
 
CREATE TABLE member(  
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',  
    name VARCHAR(255) NOT NULL COMMENT 'Name',  
    username VARCHAR(255) NOT NULL COMMENT 'Username',  
    password VARCHAR(255) NOT NULL COMMENT 'Password',  
    follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',  
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time'  
);  

![2-2](screenshots/2-2.png)   

## Task 3
1.
INSERT INTO member(name, username, password) VALUES('test', 'test', 'test');  
INSERT INTO member(name, username, password, follower_count) VALUES('andy', 'andya', '12', 1);  
INSERT INTO member(name, username, password, follower_count) VALUES('bill', 'billb', '34', 2);  
INSERT INTO member(name, username, password, follower_count) VALUES('calvin', 'calvinc', '56', 3);  
INSERT INTO member(name, username, password, follower_count) VALUES('dan', 'dand', '78', 4);  

![3-1](screenshots/3-1.png)   


2. SELECT * FROM member;  

![3-2](screenshots/3-2.png)   

3. SELECT * FROM member ORDER BY time DESC;  

![3-3](screenshots/3-3.png)   

4. SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;  

![3-4](screenshots/3-4.png)   

5. SELECT * FROM member WHERE username= 'test';  

![3-5](screenshots/3-5.png)   

6. SELECT * FROM member WHERE name LIKE '%es%';  

![3-6](screenshots/3-6.png)   

7. SELECT * FROM member WHERE username= binary 'test' and password= binary 'test';  

![3-7](screenshots/3-7.png)   

8. UPDATE member SET name= 'test2' WHERE username= 'test';  

![3-8](screenshots/3-8.png)   




## Task 4
1. SELECT COUNT(*) FROM member;  

![4-1](screenshots/4-1.png)  

2. SELECT SUM(follower_count) FROM member;  

![4-2](screenshots/4-2.png)  

3. SELECT AVG(follower_count) FROM member;  

![4-3](screenshots/4-3.png)  

4. SELECT AVG(follower_count) FROM (SELECT follower_count FROM member ORDER BY follower_count DESC LIMIT 2) AS member_first2;  

![4-4](screenshots/4-4.png)  




## Task 5
1. USE website;  

CREATE TABLE message(  
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',  
    member_id BIGINT NOT NULL COMMENT 'Member ID for Message Sender',  
    content VARCHAR(255) NOT NULL COMMENT 'Content',  
    like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Like Count',  
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',  
    FOREIGN KEY(member_id) REFERENCES member(id)  
);  

![5-1](screenshots/5-1.png)   


![5-1-2](screenshots/5-1-2.png)   


2. SELECT message.*, member.name FROM member INNER JOIN message ON member.id=message.member_id;  

![5-2](screenshots/5-2.png)   

3. SELECT message.*, member.name FROM member INNER JOIN message ON member.id=message.member_id WHERE member.username='test';  

![5-3](screenshots/5-3.png)   

4. SELECT AVG(message.like_count) FROM message INNER JOIN member ON message.member_id=member.id WHERE member.username='test';  

![5-4](screenshots/5-4.png)   

5. SELECT member.username, AVG(message.like_count) FROM message INNER JOIN member ON message.member_id=member.id GROUP BY member.username;  

![5-5](screenshots/5-5.png)   






