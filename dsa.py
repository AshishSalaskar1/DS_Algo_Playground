def isArraySpecial(arr, queries):
    n = len(arr)
    bads = []

    for x in range(n):
        if (arr[x]%2==1 and arr[x-1]%2==1) or (arr[x]%2==0 and arr[x-1]%2==0):
            # print(arr[x-1], arr[x])
            bads.append([x-1,x])

    res = []
    # print(bads)
    for [u,v] in queries:
        curres = None
        for x,y in bads:
            if x>=u and y<=v:
                curres = False
                break
        if curres is None:
            curres = True
        
        res.append(curres)

    return res

print(isArraySpecial( [4,3,1,6],  [[0,2],[2,3]]))
print(isArraySpecial( [1,4],  [[0,1]]))



