create table jul18_coffee(
	c_no number(3) primary key,
	c_name varchar2 (10 char )not null,
	c_price number(5) not null,
	c_bean varchar2(10 char) not null
)
create sequence jul18_coffee_seq
select * from jul18_coffee
select COUNT(c_bean), AVG(c_price) from jul18_coffee where c_bean in

select avg(c_price) from jul18_coffee where c_no >= 2 and c_no <= 6

select c_name  ,c_price, c_bean from jul18_coffee

delete  from jul18_coffee where c_no = 2

select * from jul18_coffee order by c_no