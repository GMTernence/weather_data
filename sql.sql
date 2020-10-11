create database weather_data;


use weather_data;
create table if not exists city_list(
	city_id int unsigned auto_increment,
	province varchar(30) not null,
	city varchar(30) not null,
	spell varchar(30) not null,
	primary key (city_id)
)default charset=utf8;

use weather_data;
create table if not exists weather_list(
	weather_id int unsigned primary key auto_increment,
	 weather_date date not null,
	province varchar(30) not null,
	city varchar(30) not null,
	spell varchar(30) not null,
	state varchar(30) not null,
	temperature varchar(30) not null,
	wind  varchar(30) not null
)default charset=utf8;