## Prefix Sums
- Given any array, you build a `prefix array`. Where `prefix[i]` = sum(`arr[0]`+..+`arr[i]`)
- **SUM(L,R)** = `prefix[r]` - `prefix[l-1]` 


## Partial Sums
- You have `Q` queries where you add a certain number to range [`start`, `end`]
- Now answer the same query as prefix sum -> SUM(L,R)
### Solution:
1. For each query (`start`,`end`,`add_val`) ->  `prefix[start] += add_val`, `prefix[end+1] -= add_val`
2. SUM(L,R) -> **RECALCULATE PREFIX SUM -> GET SUM(L,R)**

- Why `arr[start] += add_val`? All numbers after `start` will have the additional value added to it
- Why `arr[end+1] -= add_val`? Till end, you want the `add_val` to be added to each item till `end` ( this is already done). But after this val, you dont want this val to be added


### 💡 **Note**: 
  1. This method is fine, in case you have `Q` range add/sub queries and then a final sum(l,r) query
  2. If you multiple queries of both types (range add/sub and range_sum) then use SEGMENT TREES



## Prefix Sums - 2D
#### Problem: Given 2D matrix, you need to return the sum bounded by `L`,`R`,`U`,`D` -> These represent the 4 boundaries of the square

### Generating Prefix Sum Matrix
1. `prefix[i][j]` = SUM from `arr[0][0]` to `arr[i][j]`
2. Traverse the matrix in **ROW_WISE** traversal
   - **`prefix[i][j]` = `arr[i][j]` + `prefix[i-1][j]` + `prefix[i][j-1]` - `prefix[i-1][j-1]`**
    1. ADD `arr[i][j]` -> add curr value
    2. ADD `prefix[i-1][j]`, `prefix[i][j-1]` -> add sum from top and left row
    3. SUB `prefix[i-1][j-1]` -> since in `2` this part got added twice

### SUM (L, R, U, D)
- SUM(L,R,U,D) = `prefix[D][R]` - `prefix[U-1][R]` - `prefix[D][L-1]` + `prefix[U-1][L-1]`

![Imgur](https://i.imgur.com/bsynfgC.png)
- Ref Video: https://www.youtube.com/watch?v=gRqAbKHNp6M


## Partial Sums - 2D
#### Problem: Given 2D matrix, you need to return the sum bounded by `L`,`R`,`U`,`D` -> These represent the 4 boundaries of the square. In between you have queries Q(L,R,U,D,val) where val is added to each cell in the rectangle formed by `L`,`R`,`U`,`D`


### 1. Updating Vals for each Query
1. ADD: arr[U][L] += val
2. SUB: arr[U][R+1] -= val
3. SUB: arr[D+1][L] -= val
4. ADD: arr[D+1][R+1] += val ( this got subtracted twice by `2`,`3`)

### 3. Generate the 2D prefix sum matrix again and use for SUM queries

![Imgur](https://i.imgur.com/1wrjbjS.png)
- Ref Video: https://www.youtube.com/watch?v=bprsWuagVlU