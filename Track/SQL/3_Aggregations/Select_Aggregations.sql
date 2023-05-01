/* TABLE SCHEMA
Row_ID | Order_ID | 
Order_Date | Ship_Date | Ship_Mode | Customer_ID | Customer_Name | Segment |
Country/Region | City | State | Postal_Code | Region | Product_ID | 
c | Sub_Category | Product_Name | 
Sales | Quantity | Discount | Profit
*/

use namaste;

-- 1- write a update statement to update city as null for order ids :  CA-2020-161389 , US-2021-156909
UPDATE orders SET city=null WHERE Order_ID IN ( 'CA-2020-161389' , 'US-2021-156909');

-- 2- write a query to find orders where city is null (2 rows)
SELECT * FROM orders WHERE city IS NULL;

-- 3- write a query to get total profit, first order date and latest order date for each category
SELECT 
	SUM(profit) AS total_profit,
	MIN(order_date) AS first_order_date,
	MAX(order_date) AS first_order_date
FROM orders
GROUP BY Category;

-- 4- write a query to find sub-categories where average profit is more than the half of the max profit in that sub-category
SELECT DISTINCT sub_category
FROM orders
GROUP BY sub_category 
HAVING AVG(profit) > SUM(profit)/2;

-- 5- create the exams table with below script;
create table exams (student_id int, subject varchar(20), marks int);
insert into exams values (1,'Chemistry',91),(1,'Physics',91),(1,'Maths',92),(2,'Chemistry',80),(2,'Physics',90),(3,'Chemistry',80),(3,'Maths',80),(4,'Chemistry',71),(4,'Physics',54),(5,'Chemistry',79);

-- write a query to find students who have got same marks in Physics and Chemistry.
SELECT student_id, marks FROM exams  
WHERE subject IN ('Physics','Chemistry')
GROUP BY student_id, marks
HAVING count(subject)>1;

-- 6- write a query to find total number of products in each category.
SELECT category, count(distinct product_id) as product_count
FROM orders
GROUP BY category;

-- 7- write a query to find top 5 sub categories in west region by total quantity sold
SELECT 
	TOP 5 sub_category, SUM(sales) as sub_cat_sales
FROM orders 
WHERE region='west'
GROUP BY sub_category
ORDER BY sub_cat_sales DESC;

-- 8- write a query to find total sales for each region and ship mode combination for orders in year 2020
SELECT region, ship_mode, SUM(sales) as total_sales
FROM orders
WHERE YEAR(order_date) = '2020'
GROUP BY region, ship_mode;