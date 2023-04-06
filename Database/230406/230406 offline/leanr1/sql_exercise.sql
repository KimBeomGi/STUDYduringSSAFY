--CRUD
--INSERT, SELECT, UPDATE, DELETE
-- INSERT INTO table_name(column, column2, column3,..))
--      VALUES (value1, value2, value3,.....) : 하나의 레코드 생성

INSERT INTO emp (ename, job, sal)
    VALUES('KIMSSAFY', 'PROGRAMMER', '6000');

INSERT INTO emp
    VALUES('7777', 'KIMSSAFY', 'PROGRAMMER', 7566, '6/4/2023', 6000, NULL, 20);

DELETE FROM EMP;

DELETE FROM EMP WHERE ename='SCOTT';

-- UPDATE table_name
--      SET column_name = value, 
--          column_name = value, 
--          column_name = value, 
--          column_name = value
--      WHERE 조건문....;
UPDATE emp
    SET DEPTNO = 50
    WHERE mgr = 7698;

UPDATE emp
    SET DEPTNO = 30
    WHERE mgr = 7698;


-- 전직원의 급여의 총합을 구하라


SELECT rowid, sum(sal) as "급여 총합"
    FROM emp;

-- 전 사원의 수를 구하라
SELECT count(*) as "사원수"
    FROM emp;

-- 부서별 급여의 합
-- SELECT sum(sal)
--     FROM emp
--     WHERE deptno = 10;

-- SELECT sum(sal)
--     FROM emp
--     WHERE deptno = 20;

-- SELECT sum(sal)
--     FROM emp
--     WHERE deptno = 30;

-- GROUP BY
--  부서별 급여의 총합
SELECT sum(sal) as "부서별 총합", deptno
    FROM emp
    GROUP BY deptno;

--  업무별 급여의 총합
SELECT sum(sal) as "부서별 총합", job
    FROM emp
    GROUP BY job;

-- 업무별 급여의 총합 에서 NULL값이 있으면 IFNULL 사용
SELECT sum(sal+IFNULL(comm,0)) as "부서별 총합", job
    FROM emp
    GROUP BY job;

-- 부서별 업무별 급여의 총합을알고 싶도다!
SELECT sum(sal+IFNULL(comm,0)) as "부서별 업무별 총합", deptno AS "부서", job AS "업무"
    FROM emp
    GROUP BY deptno, job;

-- 자신의 업무별 급여의 평균보다 많이 받는 직원을 조회
SELECT e1.empno, e1.ename, e1.job, e1.sal
    FROM emp e1
    WHERE e1.sal >= (SELECT AVG(e2.sal+IFNULL(e2.comm,0))
                    FROM emp e2
                    WHERE e2.job = e1.job
                    GROUP BY e2.job);

SELECT AVG(sal+IFNULL(comm,0)), job
    FROM emp
--    WHERE job = 'SALESMAN'
    GROUP BY job;


-- 모든 직원의 직원의 사번, 이름, 부서번호, 부서 이름, 업무를 조회
SELECT empno, ename deptno, job
    FROM emp;

SELECT deptno, DNAME
    FROM dept;


-- 동등 조인, INNER JOIN
SELECT empno, ename, e.deptno, d.deptno, dname
    FROM emp e, dept d
    where e.deptno = d.deptno;

SELECT empno, ename, e.deptno, d.deptno, dname
    FROM emp e INNER JOIN dept d
    ON e.deptno = d.deptno;

-- 각 직원의 사번, 이름, 부서번호, 매니저 이름, 업무를 조회
SELECT * FROM emp;


-- 셀프 조인
SELECT e1.empno, e1.ename, e1.deptno, e1.mgr, e2.ename AS "매니저", e1.job
    FROM emp e1, emp e2
    WHERE e1.mgr = e2.empno;


-- 부서에 직원이 없는 부서도 조회
-- OUTER JOIN
-- 보통 조인 할 때 왼쪽 테이블을 기준으로 주고, 그 테이블에 다가 끼워서 조인을 주로함.
-- 따라서 OUTER 조인시 RIGHT나 FULL을 주로 사용하진 않음.
SELECT empno, ename, e.deptno, d.deptno, dname
    FROM emp e LEFT OUTER JOIN dept d
    ON e.deptno = d.deptno;

SELECT empno, ename, e.deptno, d.deptno, dname
    FROM emp e RIGHT OUTER JOIN dept d
    ON e.deptno = d.deptno;


SELECT empno, ename, e.deptno, d.deptno, dname
    FROM emp e FULL OUTER JOIN dept d
    ON e.deptno = d.deptno;


INSERT INTO emp
    VALUES('7777', 'KIMSSAFY', 'PROGRAMMER', 7566, '6/4/2023', 6000, NULL, 50);

SELECT e1.empno, e1.ename, e1.deptno, e1.mgr, e2.ename AS "매니저", e1.job
    FROM emp e1 LEFT OUTER JOIN emp e2
    ON e1.mgr = e2.empno;