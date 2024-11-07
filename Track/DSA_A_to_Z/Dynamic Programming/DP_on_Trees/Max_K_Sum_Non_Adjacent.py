"""
PROBLEM
You are given a n-ary tree rooted at 1 and each node has some val.

1. If you pick a Node then you cant pick its child
2. You can at max pick `k` elements

GOAL: Maximise the sum of such `k` elements
 
We need to find the max sum you can make?

INTUITION
- This is similar to House robber. You cant rob adjcaent houses. 
- You solve that using DP

SOLUTION HERE: SIMILAR, but on Trees


            3(1)
          /   \
         4(2)  5(3)
       /   \     \
      1(4)  3(5)  1(6)

BEST HERE: Pick (2) and (3) = 9

"""



class Tree:
    def __init__(self) -> None:
        pass