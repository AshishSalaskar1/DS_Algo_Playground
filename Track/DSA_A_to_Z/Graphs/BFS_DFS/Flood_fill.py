"""
Link: https://www.codingninjas.com/studio/problems/flood-fill-_1082141

An 'IMAGE' is represented by the 2-D array of positive integers, where each element of 2-D represents the pixel value of the image.
The given 'IMAGE' has 'N' rows and 'M' columns. You are given the location of the pixel in the image as ('X', 'Y')(0-based indexing) and a pixel value as 'P'.
Your task is to perform a �flood fill� operation on the given coordinate (X, Y) with pixel value 'P'.

Let the current pixel value of ('X', 'Y') be equal to C. To perform the flood fill operation on the coordinate (X, Y) with pixel value 'P' you need to do the following operations in order:

1. Replace the pixel value of ('X', 'Y') with 'P'.
2. Visit all non-diagonal neighbours of ('X', 'Y') having pixel values equal to C and replace their pixel value with 'P'.
3. Non � diagonal neighbours are Up('X' - 1, 'Y'), Down('X' + 1, 'Y'), Left('X', 'Y' - 1), right('X', 'Y' + 1). Also, you cannot go out of bounds.
4. Visit all non-diagonals neighbours of coordinates visited in step 2 having pixel value equal to C and replace their pixel value with 'P'.
5. Repeat step 2, until you have visited all your neighbours

For Example:
For  'N' = 5 , 'M' = 4 , 'X' = 2 , 'Y' = 2 and 'P' = 5
[7, 1, 1, 1]
[1, 7, 7, 7]
[7, 7, 7, 0]
[7, 7, 7, 4]
[4, 4, 4, 4]

After the flood fill operation, we will replace all neighbour's 7s with 5.
So our 'IMAGE' will become:
[7, 1, 1, 1]
[1, 5, 5, 5]
[5, 5, 5, 0]
[5, 5, 5, 4]
[4, 4, 4, 4]

SOLUTION
- Simple BFS on (X,Y) and nbrs are 4 directions
- image[x][y] is ur value, n all others are same as 0 (You ignore)
- Instead of marking as visited, just replace image[x][y] with P
"""

from typing import List

def floodFill(image: List[List[int]], nr: int, nc: int, x: int, y: int, p: int) -> List[List[int]]:

    q = [(x,y)]
    curr_value = image[x][y]

    while len(q) != 0:
        x1, y1 = q.pop(0)
        image[x1][y1] = p

        # find all nbrs
        xdelta = [1,0,-1,0]
        ydelta = [0,1,0,-1]
        for xd,yd in zip(xdelta, ydelta):
            x2 = x1 + xd
            y2 = y1 + yd
            if x2>=0 and y2>=0 and x2<nr and y2<nc:
                # print(x2,y2,nr,nc)
                if image[x2][y2] == curr_value:
                    q.append((x2,y2))

    return image



arr = [
    [7, 1, 1, 1],
    [1, 7, 7, 7],
    [7, 7, 7, 0],
    [7, 7, 7, 4],
    [4, 4, 4, 4]
]

n = len(arr)
m = len(arr[0])
x,y=2,2
p=5

print(floodFill(image=arr, nr=n, nc=m, x=x,y=y,p=p))