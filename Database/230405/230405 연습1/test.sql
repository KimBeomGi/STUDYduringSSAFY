CREATE TABLE users(
    name TEXT NOT NULL,
    phoneNumber TEXT NOT NULL,
    balance TEXT NOT NULL,
    age INTEGER,
    gender TEXT 
);

DROP TABLE users;
ALTER TABLE users RENAME TO contents;
ALTER TABLE contents RENAME TO users;
ALTER TABLE users RENAME COLUMN name TO first_name;
ALTER TABLE users RENAME COLUMN first_name TO users;
ALTER TABLE users RENAME COLUMN users TO first_name;
ALTER TABLE users ADD COLUMN last_name TEXT NOT NULL;
ALTER TABLE users ADD COLUMN iscan TEXT NOT NULL;
ALTER TABLE users DROP COLUMN iscan;
ALTER TABLE users RENAME TO test1;
ALTER TABLE userss RENAME TO users;

-- 실제 csv 파일과 맞추기 위해 새로 만듬
CREATE TABLE userss(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

--  .open db.sqlite3
--  .import userss.csv userss

SELECT last_name, first_name, age, balance FROM userss ORDER BY age, balance DESC;

-- 실습 이름과 나이 조회하기
SELECT last_name, first_name, age FROM users;

-- 전체 데이터 조회하기
SELECT * FROM users;

-- row id와 이름조회하기
SELECT rowid, first_name from users;

-- 이름과 나이를 나이가 어린 순서대로 조회하기
SELECT first_name, age FROM users ORDER BY age;

-- 이름과 나이를 나이가 많은 순서대로 조회하기
SELECT first_name, age FROM users ORDER BY age DESC;

-- 이름, 나이, 계좌 잔고를 나이가 어린순으로
SELECT first_name, age, balance FROM users ORDER BY age, balance DESC;\


-- 모든 지역 조회하기
SELECT country FROM users;

-- 중복 제거
SELECT DISTINCT country FROM users;

-- 지역 순으로 오름차순 정렬하여 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users ORDER BY country;

-- 이름과 지역이 중복없이 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country From users;

-- 이름과 지역 중복 없이 지역 순으로 오름차순 정렬하여 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country FROM users ORDER BY country;

-- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users WHERE age >=30;

-- 나이가 30살이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users WHERE age >= 30 AND balance >= 500000;

-- 이름에 '호'가 포함되는 사람들의 이름과 성 조회하기
SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';

-- 이름이 '준'으로 끝나는 사람들으 ㅣ이름 조회하기
SELECT first_name, last_name FROM users WHERE first_name LIKE '%준';

-- 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회하기
SELECT first_name, last_name, PHONE FROM users WHERE PHONE LIKE '02-%';

--나이가 20대인 사람들의 이름과 나이 조회하기
SELECT first_name, last_name, age FROM users WHERE age LIKE '2_';

--전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회하기
SELECT first_name, last_name, PHONE FROM users WHERE PHONE LIKE '%-51__-%';

-- 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
SELECT first_name, last_name, country FROM users WHERE country IN ('경기도', '강원도');
SELECT first_name, last_name, country FROM users WHERE country == '경기도' OR country == '강원도';

-- 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기
SELECT first_name, last_name, country FROM users WHERE country NOT IN ('경기도', '강원도');

-- 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users WHERE age BETWEEN 20 AND 30;

-- 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
-- AND 연산자를 사용하여 이전 쿼리와 동일한 결과를 반환할 수 있음
SELECT first_name, age FROM users WHERE age >=20 AND age <=30;

-- 나이가 20살 이상, 30살 이하가 아닌 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users WHERE age NOT BETWEEN 20 AND 30;
SELECT first_name, age FROM users WHERE age <20 OR age >30;


-- 첫번째부터 열번째 데이터까지 rowid와 이름 조회하기
SELECT rowid, age FROM users LIMIT 10;

-- 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회하기
SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;

-- 나이가 가장 어린 5명의 이름과 나이 조회하기
SELECT first_name, age FROM users ORDER BY age LIMIT 5;