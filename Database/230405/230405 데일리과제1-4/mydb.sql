CREATE TABLE users(
    name TEXT NOT NULL,
    phonNumber TEXT NOT NULL,
    balance TEXT NOT NULL,
    age INTEGER,
    gender TEXT
);

--  .open db.sqlite3
--  .mode csv
--  .import users.csv users

SELECT name, age, balance FROM users ORDER BY age, balance DESC;