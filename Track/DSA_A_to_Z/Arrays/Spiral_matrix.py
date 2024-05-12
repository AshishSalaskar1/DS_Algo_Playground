def spiral(arr):
    nr = len(arr) - 1
    nc = len(arr[0]) - 1

    rStart, rEnd = 0, nr
    cStart, cEnd = 0, nc

    res = []
    
    while rStart<=rEnd and cStart<=cEnd:
        for i in range(cStart, cEnd+1):
            res.append(arr[rStart][i])
        rStart += 1
        
        for i in range(rStart, rEnd+1):
            res.append(arr[i][cEnd])
        cEnd -= 1
        
        if rStart <= rEnd:
            for i in reversed(range(cStart, cEnd+1)):
                res.append(arr[rEnd][i])
            rEnd -= 1
        
        if cStart <= cEnd:
            for i in reversed(range(rStart, rEnd+1)):
                res.append(arr[i][cStart])
            
            cStart += 1
    return res