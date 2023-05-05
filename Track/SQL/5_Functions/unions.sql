use namaste;

/*
create table icc_world_cup
(Team_1 Varchar(20),Team_2 Varchar(20),Winner Varchar(20)
);
INSERT INTO icc_world_cup values('India','SL','India');
INSERT INTO icc_world_cup values('SL','Aus','Aus');
INSERT INTO icc_world_cup values('SA','Eng','Eng');
INSERT INTO icc_world_cup values('Eng','NZ','NZ');
INSERT INTO icc_world_cup values('Aus','India','India');

Run below script to create drivers table:

create table drivers(id varchar(10), start_time time, end_time time, start_loc varchar(10), end_loc varchar(10));
insert into drivers values('dri_1', '09:00', '09:30', 'a','b'),('dri_1', '09:30', '10:30', 'b','c'),('dri_1','11:00','11:30', 'd','e');
insert into drivers values('dri_1', '12:00', '12:30', 'f','g'),('dri_1', '13:30', '14:30', 'c','h');
insert into drivers values('dri_2', '12:15', '12:30', 'f','g'),('dri_2', '13:30', '14:30', 'c','h');
*/


--1- write a query to produce below output from icc_world_cup table.
--team_name, no_of_matches_played , no_of_wins , no_of_losses
WITH points_table AS (
	(
		SELECT team_1 as team, SUM(CASE WHEN team_1 = winner THEN 1 ELSE 0 END) as wins
		FROM icc_world_cup GROUP BY team_1
	)
	UNION ALL
	(
		SELECT team_2 as team, SUM(CASE WHEN team_2 = winner THEN 1 ELSE 0 END) as wins
		FROM icc_world_cup GROUP BY team_2
	)
)
SELECT 
	team, 
	COUNT(*) as total_played,
	SUM(wins) as wins,
	COUNT(*)-SUM(wins)  as losses
FROM points_table GROUP BY team;

--2- write a query to print first name and last name of a customer using orders table(everything after first space can be considered as last name)
--customer_name, first_name,last_name

--3- write a query to print below output using drivers table. Profit rides are the no of rides where end location of a ride is same as start location of immediate next ride for a driver
--id, total_rides , profit_rides
--dri_1,5,1
--dri_2,2,0

--4- write a query to print customer name and no of occurence of character 'n' in the customer name.
--customer_name , count_of_occurence_of_n

--5-write a query to print below output from orders data. example output
--hierarchy type,hierarchy name ,total_sales_in_west_region,total_sales_in_east_region
--category , Technology, ,
--category, Furniture, ,
--category, Office Supplies, ,
--sub_category, Art , ,
--sub_category, Furnishings, ,
----and so on all the category ,subcategory and ship_mode hierarchies 

--6- the first 2 characters of order_id represents the country of order placed . write a query to print total no of orders placed in each country
--(an order can have 2 rows in the data when more than 1 item was purchased in the order but it should be considered as 1 order)