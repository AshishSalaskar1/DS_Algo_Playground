"""
MAXIMUM AVERAGE PASS RATIO
Link: https://leetcode.com/problems/maximum-average-pass-ratio

SOL: GREEDY + HEAPS

Observations
- You should add to the one with least ratio ( NOT ALWAYS -> HENCE MAX GAIN IS BETTER APPROACH )
  Ex: [1,2=50%] [3,6=66%] => Here adding to first makes more sense, as you get 50% increase in gain
- Adding first new student to class, has the max gain in pass ratio. The more you increase it gets plateud ( since both pass+1 and n+1 )
- Logic:
    1. Add student one by one to the class that can get the highest gain
    2. Use PQ on <gain_in_class_by_adding_one_student>
    3. Repeat (1)->(2) until all extra students are distributed
    Note: Why repeat? After adding 1 to a class, it may turn out that again this class addition only gives max gain 
        But, this isnt gauranteed. Hence put it back in PQ rather than assigning to all

"""
from queue import PriorityQueue
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        pq = PriorityQueue()

        def get_gain(npass, n):  # gain if you assign one more passing student to this class
            return ((npass+1)/(n+1)) - (npass/n)

        for npass,n in classes:
            pq.put( (-get_gain(npass,n),npass,n) )
        
        while extraStudents>0:
            top_gain, top_passn, topn = pq.get()
            extraStudents -= 1
            pq.put( (-get_gain(top_passn+1,topn+1), top_passn+1, topn+1 ) )
        

        ratios = []
        while pq.qsize() > 0:
            _, npass, ntotal = pq.get()
            ratios.append(npass/ntotal)
        
        return sum(ratios)/len(ratios)
        