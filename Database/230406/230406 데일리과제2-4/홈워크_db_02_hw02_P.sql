-- BEGIN; ROLLBACK; COMMIT; 관련 내용이다.
-- BEIGIN;을 실행후 그 이후의 내용을 설정하면 임시로 값을 가지고 있다가
-- ROLLBACK;을 실행하게 되면 임시의 내용을 모두 취소하고 기존의 값으로 돌아간다.
-- 만약 BEIGIN;을 실행후 그 이후의 내용을 설정하면 임시로 값을 가지고 있다가
-- COMMIT;을 실행하면 임시의 값이 저장되어 기존의 값을 대체하게 된다.


CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

SELECT * FROM zoo;

BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;

DELETE FROM zoo;

BEGIN;
INSERT INTO zoo VALUES ('NAYONG', 'herbivore', 10, 100, 10);
ROLLBACK;

BEGIN;
INSERT INTO zoo VALUES ('KONG', 'herbivore', 10, 100, 10);
ROLLBACK;