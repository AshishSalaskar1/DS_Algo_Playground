"""
Problem: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i

SOLUTION:
- First sort based on frequencies, chars having more freq must be put into min_steps

[IMPROVEMENT]
- Instead of sorting which uses O(NlogN) use Heaps to dump the freq n then keep on popping
"""
from collections import Counter
from queue import PriorityQueue
class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(list(word))
        max_heap = PriorityQueue()

        for char, freq in counter.items():
            max_heap.put( (-freq, char) )
        
        rem_keys, min_key_press = 8, 1
        res = 0
        while not max_heap.empty():
            freq, char = max_heap.get()
            if rem_keys > 0:
                res += (min_key_press*-freq)
            else:
                rem_keys = 8
                min_key_press += 1
                res += (min_key_press*-freq)
            rem_keys -= 1
        
        return res


    def minimumPushesSlow(self, word: str) -> int:
        counter = Counter(list(word))
        counter = sorted(counter.items(), key=lambda x:(x[1],x[0]), reverse=True)

        rem_keys = 8 # you have 8 keys to assign
        min_key_press = 1 # initially you havent assigned anything
        res = 0
        for char, freq in counter:
            if rem_keys > 0: # if cur_keys are remaining
                res += (min_key_press*freq)
                rem_keys -= 1
            else:
                rem_keys = 8 # reset keys to 8
                min_key_press += 1 # but now min_press also increases by 1
                res += (min_key_press*freq)
                rem_keys -= 1

        return res


