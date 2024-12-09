# Binary Search Refresher

## 1. Base Variations - Convert to 0s and 1s
- 💡 Given any array -> **try to convert it to 0s and 1s and then it becomes searching for something in a 0,1 arrays**


### Example 1: Lower and upper bounds
- LOWER BOUND = number on the immediate left of the given Target (ot it can be target itself)
- Upper BOUND = number on the immediate right of the given Target (ot it can be target itself)

- `arr` = `[1,2,4,5,10,14,15,18,20]`, **target=6**

1. **LOWER_BOUND**
   - `[1,2,4,5,10,14,15,18,20]` convert this to 
   - `[1,1,1,1,0, 0 ,0 ,0 , 0]` ( 1 if `arr[i]`<=`target`, else 0 )
   - **Find the right most 1 in this**
3. **UPPER_BOUND**
    - `[1,2,4,5,10,14,15,18,20]` convert this to 
    - `[0,0,0,0, 1, 1, 1, 1, 1]` ( 1 if `arr[i]`>=`target`, else 0 )
    - **Find the left most 1 in this**

### Example 2: Find how many times sorted array is rotated/shifted to right
- `[4,5,1,2,3]` -> this is rotated/shifted right 2 times  <br><br>  

1. `[4,5,1,2,3]` ==> `[0,0,1,1,1]`
    - `0` if `arr[i]>=arr[0]` else `1`
2. **Find the index of the right most 1 => ANSWER**
3. **Edge Case**: init `ans=0`, in case no rotations, all will be 0. You will never see ones, in that case ans=0 
- 💡Here we consider unique elements, try solving issues when duplicate elments are allowed

### Example 3: Find peak in bitonic array
- `[1,4,5,6,7,10,6,4,2,1]` -> the peak=10

1. `[1,4,5,6,7,10,6,4,2,1]` => gets converted to<br>
   `[0,0,0,0,0, 1,1,1,1,1]`
    - `1` if `arr[i]>=arr[i+1]` else `0`
    - if `i==n-1` then `1`
2. **Find the index of the left most 1 => ANSWER**


💡**Notes**
- Since you do this directly to mid -> `convert(mid)` -> the TC remains O(logn)
- **This is what you internally do to decide whether to move left or right. Just that you are giving a 0-1 approach to this mental convesion** 
- **Dont focus on just that needed element, instead focus on pattern of numbers before and after**