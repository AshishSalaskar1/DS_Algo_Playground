## CLOCKWISE

def rotateMatrixClockwise(arr, nr, nc):
    # flip horizontally
    for i in range(nr//2):
        for j in range(nc):
            # print(f"replace {i}{j} with {nr-i-1}{j}")
            arr[i][j], arr[nr-i-1][j] = arr[nr-i-1][j], arr[i][j]
    print(arr, sep="\n")
    
    # flip diagonally: top-left --> bottom-right
    for i in range(nr):
        for j in range(i+1,nc):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    print(arr, sep="\n")
    print()
    
    return arr
    
# INPUT
# 1 2 3
# 4 5 6
# 7 8 9

# OUTPUT
# 7 4 1
# 8 5 2
# 9 6 3

# output: [[7,4,1],[8,5,2],[9,6,3]]
arr = [[1,2,3],[4,5,6],[7,8,9]]
rotateMatrixClockwise(arr, len(arr), len(arr))

# output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
arr = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotateMatrixClockwise(arr, len(arr), len(arr))