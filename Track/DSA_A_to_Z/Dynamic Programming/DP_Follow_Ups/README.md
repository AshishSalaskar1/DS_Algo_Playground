## Standard Forms
### Form 1: Knapsack - Pick/No Pick
### Form 2: Best Ending form
- Best solution ending at `i`
- You need to iterate best paths from `0` -> `i-1` and then include `i`
- You can also reverse - best solution starting from `i` and ending at `n`

Examples:
- LIS

### Form 3: Grid Based Problems
- Extension of Form2, but here best path is 2D


Examples:
- Most profitable path from (0,0) -> (r,c)
- Number of paths from (0,0) -> (r,c)
- Longest/Shortest paths from (0,0) -> (r,c)

### Form 4: Multi Sequence - You have 2 arrays
- These are mostly string based problems
- Recursive soln always starts from end indexes - LCS(n1,n2)
Examples:
- LCS


## DP Time Complexity
- `Time Complexity` = `n_states` * (1 + Avg cost of transitions per state)
- `Time Complexity` = `n_states` * (1 + `n_transitions` per state)


## Tabulation Tips
- If your recurrence relations have +1 in them -> Fill from (n,r) to (0,0)
- If your recurrence relations have -1 in them -> Fill from (0,0) to (n,r)
