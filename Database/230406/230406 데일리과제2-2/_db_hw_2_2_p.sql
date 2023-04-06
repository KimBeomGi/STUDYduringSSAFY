CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 어디에 입력할 것인지를 입력하지 않았기에 테이블의 컬럼 순서대로 입력된다.
--      따라서 테이블 컬럼에 맞게 입력될 수 있게 작성한다.
-- INSERT INTO zoo VALUES 
-- (5, 180, 210, 'gorilla', 'omnivore');

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 180, 210, 5);

-- 2) 각 값은 잘 주어졌으나 rowid는 한 테이블의 하나의 값만 가질 수 있는데
--      중복 되는 값을 입력했기 때문에 오류가 발생. 따라서 rowid를 다른 값으로 입력하거나,
--      rowid는 알아서 생성되므로 입력하지 않는 방법이 있다.
--     
-- INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
-- (10,'dolphin', 'carnivore', 210, 3),
-- (10, 'alligator', 'carnivore', 250, 50);

INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(11,'dolphin', 'carnivore', 210, 3),
(12,'dolphin', 'carnivore', 210, 3);

INSERT INTO zoo (name, eat, weight, age) VALUES
('dolphin', 'carnivore', 210, 3),
('alligator', 'carnivore', 250, 50);


-- 3) 테이블을 보면   name, eat, weight는 NOTNULL이어야하므로 weight 값을 추가해준다.
-- INSERT INTO zoo (name, eat, age) VALUES
-- ('dolphin', 'carnivore', 3);

INSERT INTO zoo (name, eat, age, weight) VALUES
('dolphin', 'carnivore', 3, 150);

DELETE FROM zoo;

SELECT rowid, * from zoo;