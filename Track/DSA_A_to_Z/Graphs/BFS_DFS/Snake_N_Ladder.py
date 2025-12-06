"""
PROBLEM: https://leetcode.com/problems/snakes-and-ladders/?envType=study-plan-v2&envId=top-interview-150

SOLUTION: Simple BFS

- Representation
7 8 9
6 5 4
1 2 3

=> first row (from bottom is normal) -> second is reversed -> third is normal .....
"""

from collections import deque

class Solution:
    def snakesAndLadders(self, matrix: List[List[int]]) -> int:
        board = [0] # to use 1-based indexing
        n = len(matrix)
        reverse = False  # last row is normal
        for line_arr in matrix[::-1]:
            if reverse:
                board.extend(line_arr[::-1])
            else:
                board.extend(line_arr)

            reverse = not reverse # flip reverse <-> normal
        
        # print(board)
        q = deque([(1, 0)])
        vis = set(list[1])

        while len(q) != 0:
            cur_node, cur_steps = q.popleft()
            # print(f"At node {cur_node}")
            for dice_roll in range(1,7):
                next_node = cur_node +  dice_roll
                if next_node > n*n:
                    break

                next_node = next_node if board[next_node]==-1 else board[next_node]
                # if next node is visited -> means you have already visited this node
                # since we use BFS, already visisted = it had shorter number of steps
                if next_node in vis:
                    continue
                
                if next_node == (n**2):
                    return cur_steps + 1

                q.append( (next_node, cur_steps+1) )
                vis.add(next_node)
        
        return -1
    


"""
[-1,-1,-1],
[-1,9,8],
[-1,8,9]
"""