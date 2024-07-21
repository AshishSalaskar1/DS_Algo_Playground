"""
PROBLEM:
https://leetcode.com/problems/word-ladder/

SOLUTION:
- Editorial: https://leetcode.com/problems/word-ladder/solutions/1764371/a-very-highly-detailed-explanation

INTUITION:
- Perform BFS (Earliest you reach -> the smallest path). Remove each word from vocab when visited (dont reuse words)
- "hit" -> replace each char with all possibilities (a to z - cur_char) and see if new word is in the vocab

NOTE: TCs here are for a single nextWord find operation, NOT FOR ENTIRE PROBLEM
=> Why replace all chars and not reverse? (iterate vocab and see if char_diff(newword, curword) == 1)
- looking up in vocab is O(1)
- Checking if two words have 1 char difference = O(len of largest word) # len(Counter(str1)-Counter(str2))==1
- Generating all new words = len(curword)*26 

1. Generate all pairs -> check = O(len(word)) * 26 * O(1)
2. Iterate vocab and check pairs = O(vocab) * O(len(word))

Given constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length

Summarized: Each word is of max length 10 (since all words in vocab will have same chars) and vocab_size = 5000
- So here for each step/word
1. Generate all pairs -> 10 * 26 * 1 = 260
2. Iterate vocab and check pairs = 5000 * 10 = 50k

"""
from collections import Counter
from queue import deque

class Solution:
    def ladderLength(self, begin: str, end: str, wordlist: List[str]) -> int:
       
        wordlist = set(wordlist)
        if end not in wordlist:
            return 0

        q = deque()
        q.append((begin, 1)) # <WORD, LENGTH OF ITEMS PICKED>
        if begin in wordlist: # begin may/may not be present in vocab
            wordlist.remove(begin)

        while len(q) != 0:
            curword, count = q.popleft()
            
            curword = list(curword)
            for i in range(len(curword)):
                for replace_ch in [chr(x) for x in range(ord('a'),ord('z')+1) if chr(x)!=curword[i]]:
                    nextword = "".join([*curword[:i],replace_ch,*curword[i+1:]])

                    if nextword == end:
                        return count+1

                    if nextword in wordlist:
                        wordlist.remove(nextword) # IMP : if you do this while popping (u will have same elements in q)
                        q.append((nextword, count+1))
        
        return 0


