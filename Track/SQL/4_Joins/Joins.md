### Some tips
- `nulls` are not considered in Aggregattions functions like COUNT()
  - If you do `A` LEFT JOIN `B` and then count(*) on some column in `B`, then in case value is `null` i.e no match was found from table `A`, that wont be considered for counting
  - ```sql
    -- 6- write a query to find cities where not even a single order was returned.

    SELECT o.city
    FROM 
        orders o LEFT JOIN oreturns r
        ON o.order_id = r.order_id
    GROUP BY o.city
    HAVING COUNT(return_reason) = 0;
    ```
<br>

- While doing **JOINS doesnt check for unique** or Primary key contraints.
  -  Thereore if you join tables `A` with 5 records and `B` with 10 -> you can get max of 50 rows. This max is possible if all rows in A and B have same number (Ex: 1).
  -  Each 1 of A gets joined with each 1 of B. it wont check if its duplicate or not
  -  **if you would have added PK contstraints** on either columns which are being used to JOIN the tables, then naturally you wil get at max 5 rows as output -> No duplicates so all 5 in A will be unique and all 10 in B are unique, so at max 5 can be mapped
  
<br>

- **Cross join vs Full Outer Join** - in SQL Server
  - Cross Join: Cartesian join. Just gives you `n`X`m` rows, doest compare keys and doesnt need any `ON` clause
  - Full outer: 
    - Max rows: `m` + `n`
    - Min Rows: MAX(`m`,`n`) -> in case all elements in smaller table match with another, so matching ones + rem size left of bigger table
  - ```sql
    -- Full outer
    SELECT * 
    FROM 
        A a FULL OUTER JOIN B b
        ON a.id = b.id

    --- Cross Join
    SELECT * 
    FROM A a,B b

    ```
<br>


<hr>

### Interview Questions

1. **There are 2 tables `A` with 5 records and `B` with 10 records. How many max and min records are possible in case of all type of joins between these two tables**

   A -> 5 rows, B -> 10 rows
   1. Inner Join   
       - min: 0 
       - max: 50 (A has all 1, B has all 1 -> Each 1 of A gets joined with each 1 of B )
   2. Left Join
       - min: 5
       - max: 50
   3. Right Join
       - min: 10
       - max: 50
   4. Cross Join/Full Outer Join 
       - min: 15 - 5 rows A common with B (max common possible)
       - max: 50 - no rows with common columns