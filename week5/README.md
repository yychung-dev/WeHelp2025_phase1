# Week 5 Assignment (Task 2 - Task 5)

## Task 2
1.
SHOW DATABASES;
CREATE DATABASE website;

2.
USE website;
CREATE TABLE member(
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
    name VARCHAR(255) NOT NULL COMMENT 'Name',
    username VARCHAR(255) NOT NULL COMMENT 'Username',
    password VARCHAR(255) NOT NULL COMMENT 'Password',
    follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time'
);

## Task 3
1.
INSERT INTO member(name, username, password) VALUES('test', 'test', 'test');
INSERT INTO member(name, username, password, follower_count) VALUES('andy', 'andya', '12', 1);
INSERT INTO member(name, username, password, follower_count) VALUES('bill', 'billb', '34', 2);
INSERT INTO member(name, username, password, follower_count) VALUES('calvin', 'calvinc', '56', 3);
INSERT INTO member(name, username, password, follower_count) VALUES('dan', 'dand', '78', 4);

2.
SELECT * FROM member;

## Task 4
## Task 5
