
## DP Time Complexity
- `Time Complexity` = `n_states` * (1 + Avg cost of transitions per state)

---

## Tabulation Tips
- If your recurrence relations have +1 in them -> Fill from (n,r) to (0,0)
- If your recurrence relations have -1 in them -> Fill from (0,0) to (n,r)

---

## Memoization -> Tabulation

### Straight Tabulation
- In case your recursive function **depends on outputs of past function calls**
- DP size is most times - `dp[nr+1][nc+1] `
  - This `0`th index acts like out of bounds condition (`i`,`j`<0)
  - Consider `i`==0 as no char present in `i`
  - 💡 `i<0` in recursive now becomes `i==0`
- Iterations:   
    - `i`: `1`->`nr+1`
    - `j`: `1`->`nc+1`
    - Array access = `arr[i-1][j-1]` (since you start from 1->nr+1)
- Result: `dp[nr][nc]`

### Reverse Tabulation
- In case your recursive function **depends on outputs of further future function calls**
- DP size is most times - `dp[nr+1][nc+1] `
    - This `nr`th index acts like out of bounds condition (`i`>=`nr`, `j`>=`nc`)
    - This doesnt push your indexes by 1 -> hence no -1 needed for accessing array elements
    - 💡 `i>n` in recursive now becomes `i==n`
  - Consider `i`==0 as no char present in `i`
- Iterations:   
    - `i`: `0`<-`nr-1`
    - `j`: `0`<-`nc-1`
    - Array access = `arr[i][j]` ( since you iterate from `nr-1` -> 0)
- Result: `dp[nr][nc]`

### Example
- **Problem**: 
  - https://leetcode.com/problems/distinct-subsequences/
  - Given 2 strings `s` and `t`. Count number of distinct subsequences you can form out of `s` which are equal to `t`

-** Recursive Solution**
  ```py
    def solve(self, i, j):
        # reached end of second string (total match)
        if j==len(self.t):
            return 1

        # first string exhausted
        if i==len(self.s):
            return 0

        # cur chars are same -> (1) pick (2) dont pick, hoping you have same char somewhere ahead
        if self.s[i] == self.t[j]:
            return self.solve(i+1, j+1) + self.solve(i+1,j)
        else: # move ahead, hoping you have needed char somewhere ahead
            return self.solve(i+1,j)
  ```

- **Reverse Tabulation Solution**
  ```py
    def tabular_dp_reverse(self, s, t) -> int:
        ns, nt = len(s), len(t)
        dp = [[0 for _ in range(nt + 1)] for _ in range(ns + 1)]

        # Base case: If t is empty, there's exactly one way to match it (by choosing nothing)
        for i in range(ns + 1):
            dp[i][nt] = 1

        # Fill the DP table bottom-up
        for i in range(ns - 1, -1, -1):
            for j in range(nt - 1, -1, -1):
                if s[i] == t[j]:
                    # Either match the current character or skip it
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    # Skip the current character in `s`
                    dp[i][j] = dp[i + 1][j]

        # The result is stored in dp[0][0]
        return dp[0][0]
  ```

- **Forward Solution**
  - Recursive funtions got changes acc to forward
  ```py
    def tabular_dp_incr(self, s, t) -> int:
        ns, nt = len(s), len(t)
        dp = [[0 for _ in range(nt + 1)] for _ in range(ns + 1)]

        # Base case: If t is empty, there's exactly one way to match it (by choosing nothing)
        for i in range(ns + 1):
            dp[i][0] = 1

        # Fill the DP table bottom-up
        for i in range(1, ns+1):
            for j in range(1, nt+1):
                if s[i-1] == t[j-1]:
                    # Either match the current character or skip it
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # Skip the current character in `s`
                    dp[i][j] = dp[i - 1][j]

        # The result is stored in dp[0][0]
        return dp[ns][nt]
  ```


