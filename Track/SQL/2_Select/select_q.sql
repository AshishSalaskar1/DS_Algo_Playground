use namaste;

/* TABLE SCHEMA
Row_ID | Order_ID | 
Order_Date | Ship_Date | Ship_Mode | Customer_ID | Customer_Name | Segment |
Country/Region | City | State | Postal_Code | Region | Product_ID | 
Category | Sub_Category | Product_Name | 
Sales | Quantity | Discount | Profit
*/

-- 1- write a sql to get all the orders where customers name has "a" as second character and "d" as fourth character (58 rows)
SELECT * FROM orders where Customer_Name LIKE '_[aA]_[dD]%';

-- 2- write a sql to get all the orders placed in the month of dec 2020 (352 rows) 
SELECT * FROM orders WHERE Order_Date BETWEEN '2020-12-01' and '2020-12-31';
SELECT * FROM orders WHERE YEAR(Order_Date)=2022 AND MONTH(Order_Date)=12;

-- 3- write a query to get all the orders where ship_mode is neither in 'Standard Class' nor in 'First Class' and ship_date is after nov 2020 (944 rows)
SELECT * FROM orders
WHERE 
	Ship_Mode NOT IN ('Standard Class','First Class')	
	AND Ship_Date > '2020-11-30';

-- 4- write a query to get all the orders where customer name neither start with "A" and nor ends with "n" (9815 rows)
select * from orders where customer_name not like 'A%n';

-- 5- write a query to get all the orders where profit is negative (1871 rows)
SELECT * FROM orders where Profit < 0;

-- 6- write a query to get all the orders where either quantity is less than 3 or profit is 0 (3348)
SELECT * FROM orders where Quantity<3 OR Profit=0;

-- 7- your manager handles the sales for South region and
-- he wants you to create a report of all the orders in his region where some discount is provided to the customers (815 rows)
SELECT * FROM Orders WHERE Region='South' AND Discount>0;

-- 8- write a query to find top 5 orders with highest sales in furniture category 
SELECT TOP 5 * FROM orders
WHERE  Category='Furniture'
ORDER BY sales DESC;

-- 9- write a query to find all the records in technology and furniture category for the orders placed in the year 2020 only (1021 rows)

-- 0-write a query to find all the orders where order date is in year 2020 but ship date is in 2021 (33 rows)