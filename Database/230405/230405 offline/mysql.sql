CREATE TABLE contacts(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);


CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

CRUD
CREATE: INSERT
READ : SELECT 

SELECT {필드} FROM {테이블이름} [WHERE {조건문}];

SELECT rowid, first_name, age, balance FROM users
ORDER BY age DESC, balance ASC;

SELECT DISTINCT country, first_name FROM users;
SELECT DISTINCT country from users ORDER BY country;

--나이가 20 이상 35이하인 사람의 이름과 나이를 나이순(오름차순) 조회
SELECT first_name, age
    FROM users
    WHERE age BETWEEN 20 and 35
    ORDER BY age ASC;

-- 이름이 '진호'인 사람의 이름과 나이 조회
SELECT first_name, age
    FROM users
    WHERE first_name = '진호';

-- 이름에 '호'를 포함하는 사람의 이름과 나이 모두 조회
SELECT first_name, age
    FROM users
    WHERE first_name LIKE '%민%';

-- 지역 이름이 ;__남도; 인 지역을 중복제거 하고 지역 이름 조회
SELECT DISTINCT country
    FROM users
    WHERE country LIKE '__남도';

-- IN 연산자는 여러개의 조건중에 하나를 만족하면 조회

-- 사는지역이 충청북도, 충청남도인 사람의 이름과 나이, 지역을 조회
SELECT first_name, age, country
    FROM users
    WHERE country IN('충청북도', '충청남도');

SELECT first_name, age, country
    FROM users
    WHERE country = '충청북도'
    OR country = '충청남도';

SELECT *
    FROM users
    WHERE country LIKE ('충청%');

SELECT rowid, first_name, age, balance
    FROM users
    WHERE age >= 35
    AND balance >= 500000
    LIMIT 11, 15;

SELECT FIRST_name, age, balance FROM users ORDER BY age, balance DESC;

UPDATE : UPDATE
DELETE : DELETE

