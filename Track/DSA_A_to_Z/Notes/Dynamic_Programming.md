### LCS Related Problems
**Variations**
- **Longest Palindromic Subsequence** -> `LCS(str, reverse(str)`
- **Min num of insertions or deletion to make string s1=s2**
    1. l = LCS(s1,s2)
    2. Min Deletions -> len(s1)-l
    3. Min Insertions -> len(s2)-l
- **Shortest Common Subsequence**
  1. Given 2 strings, create another string such that it has both the strings as subsequence and is as short as possible
  2. LCS = LCS(str1,str2)
  3. res = LCS + Add missing chars from str1 and str2 in res in order (Such that str1/2 subs