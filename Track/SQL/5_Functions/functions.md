## Important Fuctions
## STRING_AGG()
- Also called STRING_CONCAT in some databases
- Aggregate all row-values in group after performing group_by
- Syntax: `STRING_AGG(col_name, separator) WITHIN GROUP(order by col_name_to_order)`
- ```sql
    SELECT dept_id, STRING_AGG(emp_name,',')
    FROM department
    GROUP BY dept_id
    /*
    dept1 |  name1,name2,name3
    dept2 | name3,name 5,name6
    */
  ```

## Other String functions
- LEFT(col_name, n)
- RIGHT(col_name, n)
- SUBSTRING(col_name, start_index, n) -> selects col_name[start_index, start_index+n]
- CONCAT(col1, '_', col2)
- CHARINDEX(char, col_name) -> returns first occurence index of char in col_name
- LEN(col_name)
- REPLACE(col_name, s1, s2) -> replace s1 with s2 in col_name
  ## Date Functions
- `DATEPART(year, order_date)`
- `DATEADD(day, 5, order_date)` -> `(what_to_add, how_much_to_add, where_to_add)`
- `DATEDIFF(day, date_col_1, date_col2)` ->  `(measure_of_diff, date1, date2)`

## Null check functions
- ISNULL(col_name, default)
- COALESCE(col1, col2, col3, default) -> if col1=null pick col2, if that also is null pick col2 and so on

## CASE
- Always executed from top to bottom in order -> If matched will stop execution
- You can also use case within aggregration like `SUM(CASE ....)`
- ```sql
    SELECT 
    col1,
        CASE
        WHEN col1>2 and col1<3 THEN 'GOOD'
        WHEN col1>1 THEN 'FINE'
        ELSE 'BAD'
        END
    as case_op
    FROM employee;
  ```

## UNION, INTERSECT and EXCEPT
- Col(name,datatype) should have same number of columns for UNION
- ```sql
    -- removes any duplicates rows
    select * from table1
    UNION
    select * from table2

    -- keep duplicate rows
    select * from table1
    UNION ALL
    select * from table2

    -- Give rows common in table1 and 2
    select * from table1
    INTERSECT
    select * from table2

    -- Give rows present in table1 but not in table2
    -- EXCEPT === MINUS
    select * from table1
    EXCEPT
    select * from table2
  ```