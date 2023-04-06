-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT COUNT(*) FROM users;
SELECT AVG(balance) FROM users;

SELECT country, AVG(balance) FROM users where country='전라북도';

SELECT country, AVG(balance) FROM users GROUP BY country;
SELECT country, AVG(balance) FROM users GROUP BY country ORDER BY AVG(balance) DESC;

SELECT AVG(age) FROM users WHERE age>=30;

SELECT country, COUNT(*) FROM users GROUP BY country

SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;
SELECT last_name, COUNT(*) FROM users GROUP BY last_name ORDER BY COUNT(*) DESC;



CREATE TABLE classmates(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);


INSERT INTO classmates (name, age, address)
VALUES('홍길동', 23, '서울');

INSERT INTO classmates
VALUES ('김철수', 30, '경기'),
    ('이영미', 31, '강원'),
    ('박진성', 26, '전라'),
    ('최지수', 12, '충청'),
    ('정요한', 28, '경상');

UPDATE classmates SET name='김철수한무두루미', address='제주도' WHERE rowid=2;