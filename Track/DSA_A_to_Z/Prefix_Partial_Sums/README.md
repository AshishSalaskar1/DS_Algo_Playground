## Overall Patterns
1. **Classic find prefix-sum** = `sum_till_i`
2. Classic find prefix-sum **with Updates**
3. **FreqSeenBefore, FreqSeenAfter pattern:** [Leetcode Discussion - Count Triplets](https://leetcode.com/problems/count-special-triplets/solutions/7401382/solve-all-prefix-suffix-problems-instant-2v3l)
Ref: `Freq_Before_After_Pattern.py`


## Prefix Sums
- Given any array, you build a `prefix array`. Where `prefix[i]` = sum(`arr[0]`+..+`arr[i]`)
- **SUM(L,R)** = `prefix[r]` - `prefix[l-1]` 

💡**IMP NOTE**: Use 1-based indexing in prefix sums ( So that you dont have to deal with l=0 case )

## Partial Sums
- You have `Q` queries where you add a certain number to range [`start`, `end`]
- Now answer the same query as prefix sum -> SUM(L,R)
### Solution:
1. For each query (`start`,`end`,`add_val`) ->  `prefix[start] += add_val`, `prefix[end+1] -= add_val`
2. SUM(L,R) -> **RECALCULATE PREFIX SUM -> GET SUM(L,R)**

- Why `arr[start] += add_val`? All numbers after `start` will have the additional value added to it
- Why `arr[end+1] -= add_val`? Till end, you want the `add_val` to be added to each item till `end` ( this is already done). But after this val, you dont want this val to be added

#### IMP TO REMEMBER
- 💡 IMP: If initially all the elements are `0` then after performing UDPATE + PREFIX SUM -> `prefix[i]` = num times the index `i` was incremented (Refer `2_Good_Nums_Partial_N_Prefix.py`)
- But in case initially array wasnt `0` then to get count ele you need to do `prefix[i]`-`prefix[i-1]` ( this is doing SUM(L,L))

### 💡 **Note**: 
  1. This method is fine, in case you have `Q` range add/sub queries and then a final sum(l,r) query
  2. If you multiple queries of both types (range add/sub and range_sum) then use SEGMENT TREES

### Interesting Examples
- `Maximize_Min_Powered_Cities.py` -> here you use partial sums but without recomputing `prefix` arr since its not needed in this particular problem


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

### Notes
- Since you do `index`+1 and `index`-1. just using 1-based indexing work. 
  1. Either handle edge cases in if condition
  2. 1-Based indexing but `arr` size = `[nr+2]``[nc+2]` ( so that 1 padding is done before and after )
- 💡Problem solved using this: `3_Max_Value_in_Rectangle_after_updates.py`


## AP on Prefix Sums ( Any series types )
- Given `arr` and `q` queries `<L,R>` 
- `query(l,r)`= `arr[l]` + `arr[l+1]x`2 + `arr[l+2]`x3 + .... + `arr[r]`x(r-l+1) 

![Imgur](https://i.imgur.com/Cbxe38R.png)

### Solution: `4_AP_on_prefix_sum.py`

## GP on Prefix Sums ( Any series types )
- Given `arr` and `q` queries `<L,R>` 
- `query(l,r)`= `arr[l]` + `arr[l+1]`x`k`<sup>`1`</sup> + `arr[l+2]`x`k`<sup>`2`</sup> + .... + `arr[r]`x`k`<sup>`(r-l+1)`</sup> 

![Imgur](https://i.imgur.com/bc7TVtv.png)

### Note:
- You need to handle mod inverse specially in this solution (NOT DONE)
### Solution: `5_GP_on_prefix_sum.py`


### References
- https://leetcode.com/problem-list/prefix-sum/
- [x] https://leetcode.com/problems/range-sum-query-2d-immutable/description/
- [ ] https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/?envType=problem-list-v2&envId=prefix-sum


