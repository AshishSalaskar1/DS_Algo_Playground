"""
Problem: https://leetcode.com/problems/rotating-the-box/?envType=daily-question&envId=2024-11-23
Answer: https://leetcode.com/problems/rotating-the-box/solutions/1388005/two-simple-java-solutions/?envType=daily-question&envId=2024-11-23

SOLUTION - Consider only each row and add gravity to it
=> TWO POINTER KIND OF PROBLEM
- Whenever you see a stone("#") -> move to just before the first obstacle it sees (obstacle-1, untill obstacle-1 is not already occupied)

1. last_seen_obstacle -> points to the nearest right obstacle (n in case arr[-1] is free | consider right most boundary as obstacle)
   -> this means that last_seen_obstacle-1 is the first free space

2. Iterate cur=0 <- n-1
    1. if arr[cur] is obstacle -> last_seen_obstacle = cur
    2. if arr[cur] is empty -> ignore
    3. if arr[cur] is stone -> iterate cur<-last_seen_obstacle-1 -> fill the first empty slot jsut before last_seen_obstacle
       -> repalce arr[cur] with space and found index with STONE
       -> update: last_seen_obstacle
          - decrement last_seen_obstacle untill last_seen_obstacle is not a OBSTACLE or STONE


ROTATING THIS MATRIX

for i in range(nr):
    for j in range(nc):
        col = nr-1-i
        row = j
        
        res[row][col] = temp_res[i][j]

Samples to analyze
#   0 1 2 3
# 0 a b c d
# 1 e f g h


#   0 1
# 0 e a 
# 1 f b
# 2 g c
# 3 h d

# 00 -> 01
# 01 -> 11
# 02 -> 21
# 03 -> 31

# 10 -> 00
# 11 -> 10
# 12 -> 20
# 13 -> 30



"""
class Solution:
    def gravity(self, arr):
        n = len(arr)
        last_seen_obstacle = None

        if arr[-1] == ".": # considering right boundary as first obstacle
            last_seen_obstacle = n
        else:
            last_seen_obstacle = n-1
            while last_seen_obstacle>=0 and arr[last_seen_obstacle] != ".":
                last_seen_obstacle -= 1
            
            # last_seen_obstacle points to first FREE SPACE -> next to it is your OBSTACLE
            last_seen_obstacle += 1
        
        cur = n-1

        while cur>=0 and last_seen_obstacle>=0:
            if arr[cur] == "*":
                last_seen_obstacle = cur

            if arr[cur] == "#":
                # find the right-most cell before last_seen_obstacle where your stone can fall down into
                for j in reversed(range(cur,last_seen_obstacle)):
                    if arr[j] == ".":
                        arr[cur] = "."
                        arr[j] = "#"

                        # shift barrier now
                        last_seen_obstacle -= 1
                        while arr[last_seen_obstacle] != "#" and arr[last_seen_obstacle] != "*":
                            last_seen_obstacle -= 1
                        break        
                
            cur -= 1
        
        return arr

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        nr,nc = len(box), len(box[0])
        temp_res = []
        for row in box:
            # print(row)
            temp = self.gravity(row)
            # print(temp)
            temp_res.append(temp)
        
        # print(*temp_res, sep="\n")
        res = [["" for _ in range(nr)] for _ in range(nc)]

        for i in range(nr):
            for j in range(nc):
                col = nr-1-i
                row = j
                
                res[row][col] = temp_res[i][j]
        return res
        


