use namaste;


/* 
==> ORDERS TABLE
Row_ID | Order_ID | 
Order_Date | Ship_Date | Ship_Mode | Customer_ID | Customer_Name | Segment |
Country/Region | City | State | Postal_Code | Region | Product_ID | 
c | Sub_Category | Product_Name | 
Sales | Quantity | Discount | Profit
select count(order_id) from oreturns;

==> oreturns
order_id, return_reason

-----------------------------------------
==> employee
emp_id, emp_age, emp_name, dept_id, salary, manager_id, dob

==> dept
dept_id, dep_name
-----------------------------------------
==> exams
student_id, subject, exams

alter table  employee add dob date;
update employee set dob = dateadd(year,-1*emp_age,getdate())

*/

-- 1- write a query to print emp name , their manager name and diffrence in their age (in days) 
-- for employees whose year of birth is before their managers year of birth
SELECT
	emp.emp_name as employee_name,
	mng.emp_name as manager_name,
	DATEDIFF(day, emp.dob, mng.dob) as age_diff
FROM
	employee emp JOIN employee mng
	ON emp.manager_id = mng.emp_id
WHERE emp.dob < mng.dob;


-- 2- write a query to find subcategories who never had any return orders in the month of november (irrespective of years)
SELECT
	o.sub_category 
FROM 
	orders o LEFT JOIN oreturns r
	ON o.Order_ID = r.order_id
WHERE DATEPART(MONTH, o.order_date) = 11
GROUP BY o.sub_category
HAVING COUNT(r.return_reason) = 0;

-- 3- orders table can have multiple rows for a particular order_id when customers buys more than 1 product in an order.
-- write a query to find order ids where there is only 1 product bought by the customer.
SELECT order_id  
FROM orders
GROUP BY order_id
HAVING COUNT(product_id) = 1;

-- 4- write a query to print manager names along with the comma separated list(order by emp salary) of all employees -- directly reporting to him.
SELECT
	mng.emp_name as manager_name,
	STRING_AGG(emp.emp_name, ',') as reporting_emp
FROM
	employee emp JOIN employee mng
	ON emp.manager_id = mng.emp_id
GROUP BY mng.emp_name;

-- 5- write a query to get  number of business days between order_date and ship_date (exclude weekends). 
-- Assume that all order date and ship date are on weekdays only
--- days_diff   - 2*(week_diff) : 2 weekends per week
SELECT	
	DATEDIFF(DAY, order_date, ship_date) - 2*DATEDIFF(WEEK, Order_Date, Ship_Date) as n_business_days
FROM orders;


-- 6- write a query to print 3 columns : category, total_sales and (total sales of returned orders)
SELECT
	o.category,
	SUM(sales) as total_sales,
	SUM(
		CASE
		WHEN r.return_reason is NULL then 0
		ELSE o.sales
		END
	) as total_sales_returned_orders
FROM 
	orders o LEFT  JOIN oreturns r 
	ON o.order_id = r.order_id
GROUP BY o.category;



-- 7- write a query to print below 3 columns
-- category, total_sales_2019(sales in year 2019), total_sales_2020(sales in year 2020)
SELECT
	category,
	SUM(CASE WHEN DATEPART(YEAR,order_date)=2019 THEN sales ELSE 0 END) as sales_2019,
	SUM(CASE WHEN DATEPART(YEAR,order_date)=2020 THEN sales ELSE 0 END) as sales_2020

FROM orders
GROUP BY category;

-- 8- write a query print top 5 cities in west region by average no of days between order date and ship date.
SELECT TOP 5
	city,
	AVG(DATEDIFF(DAY, order_date, ship_date)) as order_ship_diff
FROM orders
WHERE region='WEST'
GROUP BY city
ORDER BY order_ship_diff DESC;

-- 9- write a query to print emp name, manager name and senior manager name (senior manager is manager's manager)
SELECT
	emp.emp_name as emp_name,
	mng.emp_name as manager_name,
	smng.emp_name as senior_manager_name
FROM
	employee emp
	JOIN employee mng ON emp.manager_id = mng.emp_id
	JOIN employee smng ON mng.manager_id = smng.emp_id
;
