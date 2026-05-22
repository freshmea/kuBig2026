# chanpark-MySQL-2026

## MySQL studying repo

### 2026-04-28

```sql
SHOW DATABASES;

CREATE DATABASE iot;
USE iot;

CREATE TABLE student (
    id INT,
    name VARCHAR(20)
);

CREATE TABLE apply (
    id INT,
    stu_name VARCHAR(20)
);

SHOW TABLES;

CREATE DATABASE madang;
USE madang;

SHOW DATABASES;

CREATE TABLE Book (
    bookid INT PRIMARY KEY,
    bookname VARCHAR(40),
    publisher VARCHAR(40),
    price INT
);

DESC Book;
```

table 삭제.

```sql
-- DROP TABLE Book;
```

```sql
CREATE TABLE Customer (
    custid INT PRIMARY KEY,
    name VARCHAR(40),
    address VARCHAR(40),
    phone VARCHAR(40)
);

CREATE TABLE Orders (
    orderid INT PRIMARY KEY,
    custid INT,
    bookid INT,
    saleprice INT,
    orderdate DATE,
    FOREIGN KEY (custid) REFERENCES Customer(custid),
    FOREIGN KEY (bookid) REFERENCES Book(bookid)
);
```

조회

```sql
SELECT *
FROM Book;

INSERT INTO Book VALUES (1, '축구의 역사', '굿스포츠', 7000);
INSERT INTO Book VALUES (2, '축구 아는 여자', '나무수', 13000);
INSERT INTO Book VALUES (3, '축구의 이해', '대한미디어', 22000);
INSERT INTO Book VALUES (4, '골프 바이블', '대한미디어', 35000);
INSERT INTO Book VALUES (5, '피겨 교본', '굿스포츠', 8000);
INSERT INTO Book VALUES (6, '배구 단계별기술', '굿스포츠', 6000);
INSERT INTO Book VALUES (7, '야구의 추억', '이상미디어', 20000);
INSERT INTO Book VALUES (8, '야구를 부탁해', '이상미디어', 13000);
INSERT INTO Book VALUES (9, '올림픽 이야기', '삼성당', 7500);
INSERT INTO Book VALUES (10, 'Olympic Champions', 'Pearson', 13000);

INSERT INTO Customer VALUES (1, '박지성', '영국 맨체스타', '000-5000-0001');
INSERT INTO Customer VALUES (2, '김연아', '대한민국 서울', '000-6000-0001');
INSERT INTO Customer VALUES (3, '김연경', '대한민국 경기도', '000-7000-0001');
INSERT INTO Customer VALUES (4, '추신수', '미국 클리블랜드', '000-8000-0001');
INSERT INTO Customer VALUES (5, '박세리', '대한민국 대전', NULL);

INSERT INTO Orders VALUES (1, 1, 1, 6000, STR_TO_DATE('2024-07-01', '%Y-%m-%d'));
INSERT INTO Orders VALUES (2, 1, 3, 21000, STR_TO_DATE('2024-07-03', '%Y-%m-%d'));
INSERT INTO Orders VALUES (3, 2, 5, 8000, STR_TO_DATE('2024-07-03', '%Y-%m-%d'));
INSERT INTO Orders VALUES (4, 3, 6, 6000, STR_TO_DATE('2024-07-04', '%Y-%m-%d'));
INSERT INTO Orders VALUES (5, 4, 7, 20000, STR_TO_DATE('2024-07-05', '%Y-%m-%d'));
INSERT INTO Orders VALUES (6, 1, 2, 12000, STR_TO_DATE('2024-07-07', '%Y-%m-%d'));
INSERT INTO Orders VALUES (7, 4, 8, 13000, STR_TO_DATE('2024-07-07', '%Y-%m-%d'));
INSERT INTO Orders VALUES (8, 3, 10, 12000, STR_TO_DATE('2024-07-08', '%Y-%m-%d'));
INSERT INTO Orders VALUES (9, 2, 10, 7000, STR_TO_DATE('2024-07-09', '%Y-%m-%d'));
INSERT INTO Orders VALUES (10, 3, 8, 13000, STR_TO_DATE('2024-07-10', '%Y-%m-%d'));
```

```sql
SELECT bookname, price
FROM Book;
```

DISTINCT는 중복 제거.

```sql
SELECT DISTINCT publisher
FROM Book;
```

price가 20000보다 작은 책 조회.

```sql
SELECT *
FROM Book
WHERE price < 20000;
```

price가 10000과 20000 사이인 책 조회.

```sql
SELECT *
FROM Book
WHERE price BETWEEN 10000 AND 20000;
```

publisher가 굿스포츠 또는 대한미디어인 책 조회.

```sql
SELECT *
FROM Book
WHERE publisher IN ('굿스포츠', '대한미디어');
```

price가 NULL인 책 조회. IS NOT NULL은 NULL이 아닌 값 조회.

```sql
SELECT *
FROM Book
WHERE price IS NULL;
```

publisher가 굿스포츠 또는 대한미디어인 책 조회.

```sql
SELECT *
FROM Book
WHERE publisher = '굿스포츠'
   OR publisher = '대한미디어';
```

LIKE와 IN의 차이점은 LIKE는 패턴 매칭을 사용하여 문자열을 검색하는 반면, IN은 특정 값 목록에서 일치하는 값을 검색합니다. LIKE는 와일드카드 문자(%, _)를 사용하여 패턴을 정의할 수 있지만, IN은 단순히 값 목록을 나열합니다.

```sql
SELECT bookname, publisher
FROM Book
WHERE bookname LIKE '축구의 역사';
```

bookid가 3인 책의 이름 조회.

```sql
SELECT bookname
FROM Book
WHERE bookid = 3;
```

도서를 이름순으로 정렬할때

```sql
SELECT *
FROM Book
ORDER BY bookname;
```

가격순으로 검색하고 가격이 같으면 이름순으로 정렬할 때

```sql
SELECT *
FROM Book
ORDER BY price, bookname;
```

도서의 가격을 내림차순으로 검색하고 가격이 같다면 출판사를 오름차순으로 정렬할 때

```sql
SELECT *
FROM Book
ORDER BY price DESC, publisher ASC;
```

### 집계함수와 group by

SUM, AVG, MAX, MIN, COUNT 등이 집계함수이다.

주문의 총 판매 가격 조회.

```sql
SELECT SUM(saleprice)
FROM Orders;
```

```sql
SELECT SUM(saleprice) AS 총매출
FROM Orders;
```

2번 고객이 주문한 도서의 총판매액 조회.

```sql
SELECT SUM(saleprice) AS 총매출
FROM Orders
WHERE custid = 2;
```

고객이 주문한 도서의 총판매액, 평균값, 최저가, 최고가 조회.

```sql
SELECT SUM(saleprice) AS Total,
       AVG(saleprice) AS Average,
       MIN(saleprice) AS Minimum,
       MAX(saleprice) AS Maximum
FROM Orders;
```

마당 서점의 도서 판매 건수 조회. (*)는 모든 컬럼을 의미한다.

```sql
SELECT COUNT(*)
FROM Orders;
```

고객별로 주문한 도서의 총수량과 총판매액 조회.

```sql
SELECT custid,
       COUNT(*) AS 도서수량,
       SUM(saleprice) AS 총액
FROM Orders
GROUP BY custid;
```

group by는 특정 컬럼을 기준으로 데이터를 그룹화하여 집계함수를 적용할 때 사용한다. group by 뒤에는 그룹화할 컬럼이 오며, 집계함수는 그룹화된 데이터에 대해 계산된다. group by를 사용하면 각 그룹별로 집계된 결과를 얻을 수 있다.

가격이 8000원 이상인 도서를 구매한 고객에 대해 고객별 주문 도서의 총수량을 조회하고 총수량이 2이상인 고객만 조회.

```sql
SELECT custid,
       COUNT(*) AS 도서수량
FROM Orders
WHERE saleprice >= 8000
GROUP BY custid
HAVING COUNT(*) >= 2;
```

having 절은 group by 절과 함께 사용

#### join 조인

조건없이 작성하면 모든 경우의 수 가 나온다.

```sql
SELECT *
FROM Customer, Orders;
```

조건을 추가한 쿼리. custid가 같은 경우에만 조인된다.

```sql
SELECT *
FROM Customer, Orders
WHERE Customer.custid = Orders.custid;
```

order by 를 사용해 고객별로 정렬.

```sql
SELECT *
FROM Customer, Orders
WHERE Customer.custid = Orders.custid
ORDER BY Customer.custid;
```

where 절을 사용하여 정렬.

```sql
SELECT name, saleprice
FROM Customer, Orders
WHERE Customer.custid = Orders.custid;
```

고객별로 주문한 모든 도서의 총판매액을 구하고, 고객별로 정렬.

```sql
SELECT name,
       SUM(saleprice)
FROM Customer, Orders
WHERE Customer.custid = Orders.custid
GROUP BY Customer.name
ORDER BY Customer.name;
```

self join은 자기 자신과 조인하는 경우에 사용한다.

셀프 조인 예시. Orders 테이블을 두 번 조인하여 고객명과 도서명을 조회한다. Orders 테이블을 a와 b로 각각 조인하여 고객명과 도서명을 가져온다.

```sql
SELECT a.name AS 고객명,
       b.bookname AS 도서명
FROM Orders
JOIN Customer a ON Orders.custid = a.custid
JOIN Book b ON Orders.bookid = b.bookid;
```

### 2026-04-29

demo_scott.sql 예제

가격이 20000원인 도서를 구매한 고객의 이름과 주문한 도서의 이름을 조회.

```sql
SELECT Customer.name,
       Book.bookname
FROM Customer, Orders, Book
WHERE Customer.custid = Orders.custid
  AND Orders.bookid = Book.bookid
  AND Book.price = 20000;
```

inner join을 사용하여 같은 결과를 얻는 쿼리.

```sql
SELECT Customer.name,
       Book.bookname
FROM Orders
INNER JOIN Customer ON Orders.custid = Customer.custid
INNER JOIN Book ON Orders.bookid = Book.bookid
WHERE Book.price = 20000;
```

도서를 구매하지 않은 고객을 포함해 고객의 이름과 고객이 주문한 도서의 판매가격 조회

```sql
SELECT Customer.name, saleprice
FROM customer left outer join orders
ON Customer.custid = Orders.custid;
```

회원별 실적

```sql
select name, sum(saleprice)
from customer left join orders
on customer.custid = orders.custid
group by name;
```

#### subquery 서브쿼리

가장 비싼 도서의 이름 조회

```sql
SELECT bookname
FROM Book
WHERE price = (SELECT MAX(price) FROM Book);
```

join과 subquery의 차이점은 join은 여러 테이블을 연결하여 데이터를 조회하는 방식이고, subquery는 하나의 쿼리 안에 또 다른 쿼리를 포함하여 데이터를 조회하는 방식이다. join은 테이블 간의 관계를 기반으로 데이터를 결합하는 반면, subquery는 특정 조건을 만족하는 데이터를 조회하기 위해 내부 쿼리를 사용한다. join은 일반적으로 성능이 더 좋지만, subquery는 복잡한 조건을 처리할 때 유용할 수 있다.

도서를 구매한 적이 있는 고객의 이름을 검색하시오

```sql
select name
from customer
where custid in (select distinct custid from orders);
```

대한 미디어에서 출판한 도서를 구매한 고객의 이름을 조회.

```sql
select bookid
from book
where publisher = '대한미디어';

select custid
from orders
where bookid in (3,4);

select name
from customer
where custid = 1;
```

subquerry 를 사용하면 위의 querry 를 이렇게 작성 할 수 있다.

```sql
select name
from customer
where custid in (select custid
                 from orders
                 where bookid IN (select bookid
                                  from book
                                  where publisher = '대한미디어'));
```

#### 집합 연산

union 연산은 두 개 이상의 SELECT 문에서 반환된 결과 집합을 결합하여 하나의 결과 집합으로 만드는 연산이다. union은 중복된 행을 제거하고, union all은 중복된 행을 포함하여 모든 행을 반환한다. union은 각 SELECT 문의 컬럼 수와 데이터 타입이 일치해야 하며, 컬럼 이름은 첫 번째 SELECT 문의 컬럼 이름이 사용된다. union은 여러 테이블에서 데이터를 결합할 때 유용하게 사용된다.

김연아 고객이 주문한 도서의 총 판매액

```sql
select sum(saleprice) as 총판매액
from orders
where custid = (select custid from customer where name ='김연아');
```

```sql
select sum(saleprice) as 총판매액
from orders join customer
on orders.custid = customer.custid
where customer.name = '김연아';
```

정가가 20000원인 도서를 주문한 고객의 이름과 도시를 조회.

```sql
select name, address
from customer
where custid in (select custid
                from orders
                where bookid in (select bookid
                                from book
                                where price = 20000));
```

```sql
select name, address
from customer c join orders o join book b
on c.custid = o.custid and o.bookid = b.bookid
where price = 20000;
```

```sql
select orderid as 주문번호, (b.price - o.saleprice) as 차이
from orders o join book b
on o.bookid = b.bookid
where (b.price - o.saleprice) = (select max(b2.price - o2.saleprice) from orders o2 join book b2 on b2.bookid = o2.bookid);
```

### 2026-04-30

#### 삽입

insert into book (bookid, bookname, publisher)
        values(14, '스포츠의학', '한솔의학서적');

insert into book (bookid, bookname, publisher)
        values(15, '스포츠의학3', '한솔의학서적'),
        values(16, '스포츠의학4', '한솔의학서적');

#### 수정

customer 테이블에서 고객번호가 5인 고객의 주소를 대한민국 대전으로 변경.

```sql
SET SQL_SAFE_UPDATES = 0; --safe updates 옵션 미 해제시 실행.
UPDATE customer
SET address = '대한민국 대전'
WHERE custid = 5;


박세리의 주소를 세종으로 변경.
        update customer
    -> set address = '세종특별자치시'
    -> where custid =5;
```

#### 삭제

```sql
delete from book
where bookid = 11;
```

cascade 옵션이 설정된 경우, 부모 테이블에서 행이 삭제되면 해당 행과 관련된 자식 테이블의 행도 자동으로 삭제된다. 예를 들어, Orders 테이블에서 특정 고객의 주문이 삭제되면, 해당 고객과 관련된 모든 주문도 함께 삭제된다. cascade 옵션은 데이터 무결성을 유지하는 데 도움이 되며, 부모-자식 관계가 있는 테이블에서 유용하게 사용된다.

```sql
create table NewBook (
    bookid int primary key,
    bookname varchar(40),
    publisher varchar(40),
    price int
);
```

```sql
create table NewOrders (
    orderid int primary key,
    custid int ,
    bookid int ,
    saleprice int,
    orderdate date,
    foreign key (custid) references customer(custid) on delete cascade,
    foreign key (bookid) references book(bookid) on delete cascade
);
```

```sql

alter table new book add isbn varchar(13); -- alter table은 테이블 구조를 변경하는 명령어로, 컬럼 추가, 삭제, 수정 등을 수행할 수 있다. 위의 예시에서는 new book 테이블에 isbn이라는 새로운 컬럼을 추가하는 쿼리이다.
alter table newbook modify isbn int;

alter table newbook drop column isbn;

alter table newbook modify isbn interger not null;

alter table newbook add primary key (bookid);
```

#### 뷰
뷰는 하나 이상의 테이블에서 데이터를 조회하여 가상의 테이블을 생성하는 데이터베이스 객체이다. 뷰는 실제 데이터를 저장하지 않고, 정의된 쿼리를 실행하여 결과를 반환한다. 뷰는 복잡한 쿼리를 단순화하고, 보안을 강화하며, 데이터의 일관성을 유지하는 데 사용된다. 뷰를 사용하면 사용자에게 필요한 데이터만 제공할 수 있으며, 원본 테이블의 구조를 변경하지 않고도 데이터를 조회할 수 있다.

```sql
create view V_orders
as select orderid, O.custid, name, O.bookid, bookname, saleprice, orderdate
from orders O, customer C, book B
where O.custid = C.custid and O.bookid = B.bookid;


select * from v_orders;
```

### 아나콘다

conda env list : 현재 설치된 가상환경 목록을 보여준다.

conda create -n iot1 python=3.12 : iot1이라는 이름의 가상환경을 생성하고, 해당 환경에 Python 3.12 버전을 설치한다.

conda activate iot1 : iot1이라는 가상환경을 활성화한다.

conda install jupyter notebook : 현재 활성화된 가상환경에 Jupyter Notebook을 설치한다. pip 에서설치해도됨.

주피터 노트북 코드 폴더 설정.
cd 파일경로.
>jupyter notebook

실행후 브라우저가 열리지않으면 수동으로 복사해서 브라우저에 붙여넣기.

파이썬 프로그램 단독 실행
python 파일명.py
