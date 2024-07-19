create table jul19_weather(
	w_no number (3) primary key,
	w_hour varchar2(10 char) not null,
	w_temp varchar2(10 char) not null,
	w_tmx varchar2(10 char) not null,
	w_wfKor varchar2(10 char) not null,
	w_wdKor varchar2(10 char) not null
)
create sequence jul19_weather_seq

drop table jul19_weather
drop sequence jul19_weather_seq

select * from jul19_weather

	
create table jul19_seoulair(
	s_no number(3) primary key,
	s_msrste_nm varchar2(10char) not null,
	s_pm10 varchar2(10char) not null,
	s_pm25 varchar2(10char) not null
)
create sequence jul19_seoulair_seq

drop table jul19_seoulair
select * from jul19_seoulair