USE namaste;

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
emp_id, emp_age, emp_name, dept_id, salary, manager_id

==> dept
dept_id, dep_name
-----------------------------------------
==> exams
student_id, subject, exams



*/

-- 1- write a query to get region wise count of return orders
SELECT o.region, count(distinct o.order_id) as total_order_count
FROM 
	orders o JOIN oreturns r
	on o.order_id = r.order_id
GROUP BY o.region;


-- 2- write a query to get category wise sales of orders that were not returned
SELECT o.category, SUM(o.sales) as total_sales
FROM 
	orders o LEFT JOIN oreturns r
	on o.order_id = r.order_id
WHERE r.return_reason iS NULL
GROUP BY o.category;

select * from employee;

-- 3- write a query to print dep name and average salary of employees in that dep .
SELECT dep_name, AVG(salary) as dep_avg_salary
FROM 
	employee e JOIN dept d
	ON e.dept_id = d.dep_id
GROUP BY d.dep_name;
	
-- 4- write a query to print dep names where none of the emplyees have same salary.
SELECT dep_name
FROM 
	employee e JOIN dept d
	ON e.dept_id = d.dep_id
GROUP BY d.dep_name
HAVING COUNT(distinct e.salary) = COUNT(e.salary);

-- 5- write a query to print sub categories where we have all 3 kinds of returns (others,bad quality,wrong items)
SELECT o.sub_category 
FROM 
	orders o JOIN oreturns r
	on o.order_id = r.order_id
GROUP BY o.sub_category
HAVING count(distinct r.return_reason)=3;

-- 6- write a query to find cities where not even a single order was returned.
SELECT o.city
FROM 
	orders o LEFT JOIN oreturns r
	ON o.order_id = r.order_id
GROUP BY o.city
HAVING COUNT(return_reason) = 0;

-- 7- write a query to find top 3 subcategories by sales of returned orders in east region
SELECT TOP 3 o.sub_category, SUM(o.sales) as total_sales
FROM 
	orders o JOIN oreturns r
	ON o.order_id = r.order_id
WHERE o.region = 'east'
GROUP BY o.sub_category
ORDER BY total_sales DESC;

-- 8- write a query to print dep name for which there is no employee
SELECT d.dep_name
FROM
	dept d LEFT JOIN employee e
	ON e.dept_id = d.dep_id
GROUP BY d.dep_name
HAVING COUNT(e.emp_id) = 0;


-- 9- write a query to print employees name for dep id is not avaiable in dept table
SELECT distinct e.emp_name
FROM
	employee e LEFT JOIN dept d 
	ON e.dept_id = d.dep_id
WHERE d.dep_id is NULL;



