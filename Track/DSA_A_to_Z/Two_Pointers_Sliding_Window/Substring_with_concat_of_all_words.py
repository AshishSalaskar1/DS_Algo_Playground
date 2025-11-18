"""
Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

IDEAS:
1. Simple sliding windows to create substrings

2. Main? how do u check if substring is valid?
- Can you just compare the char count? NOOOO
  EX: words = ["ab","ab","ab"], s="bababa"
  - If you see this, counts of both are same: but words are not exactly same as `words`

  💡 SOLUTION: 
  - can you break down given string to words? YESSS -> LEN OF ALL WORDS ARE SAME
  - cur_words = ["ba","ba","ba"] :-> just split the curword every wordlen times
  - cur_words == org_words

"""

from collections import Counter
class Solution:
    def findSubstring(self, arr: str, words: List[str]) -> List[int]:
        n = len(arr)

        wmap = Counter(words)
        wordlen = len(words[0]) # all words of same length
        total_len = wordlen * len(words)

        l,r = 0,0
        res = []

        def check(curs: str, wmap: dict) -> bool:
            cur_words = Counter([curs[i:i+wordlen] for i in range(0,len(curs),wordlen)])
            return cur_words == wmap


        while r<n:
            wsize = r-l+1
            if wsize == total_len:
                if check(arr[l:r+1], wmap):
                    res.append(l)
                l += 1
       
            r += 1
        return res


"""
    def findSubstring(self, arr: str, words: List[str]) -> List[int]:
        n = len(arr)
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        wmap = Counter(words)
        res = []

        l,r = 0,0

        def check(curs, wmap):
            cur_words = Counter([curs[i:i+word_len] for i in range(0, len(curs), word_len)])
            return cur_words == wmap

        while r + word_len <= n:
            window = arr[r:r + total_len]   # full substring of required length

            if len(window) == total_len:   # window fully fits
                if check(window, wmap):
                    res.append(r)

            r += 1  # slide by 1 char (your style, not optimized)

        return res
"""
        