## **row_number()**
- It adds an extra col
- It requires `OVER` and `ORDER BY`. `PARTITION BY` is optional
- It just assigns running numbers, 2 rows cant have same row_number()
- - **Important**: **If two rows have same col_value used to order than it will assign continous ranks.**
  - There are 5 employees out of which 2 have same top salary. So E1=1, E2=2, E3=3, E4=4, E5=5

- ```sql
    -- Assign rank to each employee based on salary
    SELECT 
       *,
       row_number() over (order by salary desc) as sal_rank
    FROM employees;

    -- Assign rank to each employee in each dept based on salary
    SELECT 
       *,
       row_number() over (PARTITION BY dept order by salary desc) as sal_rank
    FROM employees;
    ```
 - **You cant use col generated using row_number() in where clause**. 
   - Because ideally SELECT runs only after WHERE is run and row_number() is mentioned in SELECT clause
   - **Solution:** use the result as subquery or use CTE
   - ```sql
     -- find top `n`(3 for ex) salary earners in each dept
     SELECT * FROM 
        (
            SELECT 
                *,
                row_number() over (PARTITION BY dept order by salary desc) as sal_rank
              FROM employees
        ) table_name
     WHERE sal_rank <=3;

     -- Same with CTE
     WITH rank_table AS  (
            SELECT 
                *,
                row_number() over (PARTITION BY dept order by salary desc) as sal_rank
              FROM employees
     )
     SELECT * FROM rank_table WHERE sal_rank <=3; 
     ```

<hr>

## **rank()**
- Syntax is same as `row_number()` . But here 2 rows can have same rank
- **Important**: **If two rows have same col_value used to order than it will assign same rank to both rows and skip 1 rank.**
  - There are 5 employees out of which 2 have same top salary. So E1,E2 rank=1, E3=3, E4=4, E5=5
  - There are 5 employees out of which 3 have same top salary. So E1,E2,E3 rank=1, E4=4, E5=5
  - `Last rank == num of elements`

<hr>

## **dense_rank()**
- Same as `rank()` which assigns same rank if equal, but doest skip ranks like `rank()` does
- **Important**:
  - There are 5 employees out of which 3 have same top salary. So E1,E2,E3 rank=1, E4=2, E5=3
  - `Last rank == num of distinct elements`

<hr>

## **lead()**
- **LEAD(`col_name`, `lead_num`, `default_value`) OVER ()**
  - Fetch value of `col_name` which is `lead_num` rows ahead of current row
  - **This fetching happens on the data after `order_by` has been applied**
  - If in case there are no rows after `lead_num` from current row, it will be NULL OR filled with `lead_num`.
  - `lead_num` can be value or you can mention `col_name` which will replace null with value of `col_name` of current row
- ```sql
    SELECT *,
        LEAD(emp_id, 1) OVER (ORDER BY salary DESC) as lead_num
    FROM employee;

    RESULT
    /*
        emp_id | salary | lead_num
        3231   | 89k    | 1212
        1212   | 60k    | 0909
        0909   | 20K    | 1010
        1010   | 10k    | NULL
    */

    SELECT *,
        LEAD(emp_id, 2) OVER (ORDER BY salary DESC) as lead_num
    FROM employee;

    RESULT
    /*
        emp_id | salary | lead_num
        3231   | 89k    | 0909
        1212   | 60k    | 1010
        0909   | 20K    | NULL
        1010   | 10k    | NULL
    */
  ```

<hr>

## **lag()**
- Same as `lead` but picks up rows before instead of ahead in case of lead
- Use Case
  - Calculate year on year growth
    - Get sales for each year
    - Using lag get last_year sales and then calculate percentage growth


<hr>

## **Aggregations on Window Function**
- `OVER` is called window function. Here instead of using rank(), row_num() etc you can also use Aggregation functions with `OVER` clause
- With aggregation+window its not mandatory to give `ORDER BY`
- ```sql
    -- calculate avg sal of each dept and add it as new col against each employee
    SELECT 
       *,
       AVG(salary) over (PARTITION BY dept) as dep_avg_salary
    FROM employees;
    -- this first partitions -> apply aggregation on that partition -> assign value to each row in that partition
  ```
- **RUNNING SUM/AVG/COUNT**
  - If you need running_sum give order in `ORDER BY` clause. 
  - **It will partition using `PARTITION BY` and then within that will calculate running SUM/COUNT/MAX/MIN based on order given in `ORDER BY`**
  - ```sql
    -- calculate running sum  based on emp_id
    SELECT 
       *,
       SUM(salary) over (ORDER BY emp_id) as dep_avg_salary
    FROM employees;
    -- sort based on emp_id -> calculate rolling sum in that partition


    -- calculate running sum each dept wise based on emp_id
    SELECT 
       *,
       SUM(salary) over (PARTITION BY dept ORDER BY emp_id) as dep_avg_salary
    FROM employees;
    -- this first partitions on dept -> sort based on emp_id -> calculate rolling sum in that partition
  ```
- **Rolling SUM with `BETWEEN`**
  - For each row, get sum of salaries 2 previous rows (include current row also) taking emp_id as order
    ```sql
    SELECT 
        SUM(salary) OVER (ORDER BY emp_id ROWS BETWEEN 2 PRECEEDING AND CURRENT ROW) as 3_roll_sum
    FROM EMPLOYEE
    ```
  - For each row, get sum of salaries of 2 previous + current + 2 next ahead rows 
      ```sql
      SELECT 
          SUM(salary) OVER (ORDER BY emp_id ROWS BETWEEN 2 PRECEEDING AND 2 PROCEEDING) as 5_roll_sum
      FROM EMPLOYEE
      ```
 - **ROWS BETWEEN `[start_range]` AND `[end_range]`** (`start_range` and `end_range` are alsos included)
   - It will be `null` if both `start_range` and `end_range` are out of bounds
   - If only `end_range` is out of bounds then take from `start_range` to `last_row` present
- **UNBOUNDED**
  - Get rolling sum from `start` till `cur_row`
      ```sql
      SELECT 
          SUM(salary) OVER (ORDER BY emp_id ROWS BETWEEN UNBOUNDED PRECEEDING AND CUURENT ROW) as 5roll_sum
      FROM EMPLOYEE
      ```
  - Get rolling sum from `cur_row` till `end_row`
    ```sql
    SELECT 
        SUM(salary) OVER (ORDER BY emp_id ROWS BETWEEN CUURENT ROW AND UNBOUNDED PROCEEDING) as 5roll_sum
    FROM