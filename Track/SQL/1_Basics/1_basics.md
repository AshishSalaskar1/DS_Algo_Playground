## Alter Table
1. Change data type of a existing column
    - new and old datatype should be compatible<br>
    ```sql
    ALTER TABLE table_name ALTER COLUMN column_name new_data_type;
    ```

2. Add new column
    - This new column always gets added at last
    - Value for `new_col` will be NULL for already present values
    
    ```sql
    ALTER TABLE table_name add column_name col_data_type;
    ```

3. Drop a column
    ```sql
    ALTER TABLE table_name DROP column_name;
    ```

4. Delete rows with condition
   ```sql
   DELETE FROM table_name WHERE col_name=col_value;
   ```

5. Update Values
   ```sql
   UPDATE table_name SET col_name=val;
   UPDATE table_name SET col_name=val WHERE col_name=col_condition_value;
   ```




    

