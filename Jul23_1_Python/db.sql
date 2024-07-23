create table Jul23_map(
	m_place_name varchar2(20char) primary key,
	m_phone varchar2(20char),
	m_x number(9,6) not null,
	m_y number(9,6) not null
)
select * from Jul23_map
drop table Jul23_map


