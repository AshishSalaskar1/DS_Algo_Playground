# KMP Algo

### KMP Array Definition
Given a string `S` of length `n`, we define the `kmp[i]` array such that:

- `kmp[i]` is the **length of the longest prefix** that is also a suffix for the substring `S[0:i]`.
  
For example:
```plaintext
           0  1  2  3  4  5  6  7  8
str = [    a  b  b  a  a  b  b  a  b] # 0-Based
kmp = [-1, 0, 0, 0, 1, 1, 2, 3, 4, 2] # 1-Based

```

Here, 
- kmp[0] = kmp["a"]= 0
- kmp[1] = kmp["ab"]= 0
- kmp[2] = kmp["aba"]= 1 (a|b|a)
- kmp[3] = kmp["abba"]= 0
- kmp[6] = kmp["abbaabb"]= 3 (abb| a |abb)


### Core Logic

When building the KMP array, at each position \( i \), we do the following:

1. **Use Previous Prefix Match**:
   - Assume we are at position \( i = 6 \), where \( S[6] = b \).
   - We look at `kmp[i-1]`, which tells us the length of the longest prefix-suffix for `S[0:i-1]`.

2. **Check and Extend**:
   - If \( S[i] \) matches the character after the prefix, \( S[kmp[i-1]] \), we can extend the prefix-suffix match by setting `kmp[i] = kmp[i-1] + 1`.
   - If \( S[i] \) does not match, we adjust by "falling back" to `kmp[kmp[i-1] - 1]` and repeat the check until a match is found or `kmp[i]` becomes zero.

3. **Assign Value**:
   - Once a match is found (or not), we set `kmp[i]` to the calculated longest prefix-suffix length.

### Example Walkthrough

Consider \( S = \text{"abbaabbab"} \):

- **Position 6** \( (S[6] = b) \):
  - `kmp[5]` is `2`, which suggests the longest prefix-suffix length up to `S[0:5]`.
  - If \( S[6] == S[kmp[5]] \), we increment to extend the match; otherwise, we adjust using `kmp` values.

# Use Case 1: Find occurences of Pattern in String
- Let `S` be string in which you want to mathch pattern `p`

1. Find KMP array of `P` + # + `S`
2. Now start from len(p) to end => **where you see len(p) in KMP array, thats one occurence** (the point is end)

```py
s = "sadbutsad"
p = "sad" 
res = get_kmp_array(f"{p}#{s}") 
print(res)


#       0  1  2  3  4  5  6  7  8  9  10 11 12
#       s  a  d  #  s  a  d  b  u  t  s  a  d
#  [-1, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 1, 2, 3]

class Solution: #KMP ALGO
    def strStr(self, s: str, p: str) -> int:
        ns, np = len(s), len(p)
        kmp_arr = get_kmp_array(f"{p}#{s}")


        for i in range(np, len(kmp_arr)):
            if kmp_arr[i] == np: # why -2*np-1? -2np (one np before # + # + np till i)
                return (i-2*np-1, i-np-1)

        return -1

```
