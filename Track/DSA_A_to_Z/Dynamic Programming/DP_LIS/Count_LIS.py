"""


"""


def LIS(arr):
    n = len(arr)
    dp = [0 for _ in range(n)] 
    lis_ways = [0 for _ in range(n)]

    res_lis = 0
    for i in range(n):
        cur_lis = 1 # LIS of single element = 1
        lis_ways[i] = 1

        for j in range(0,i):
            if arr[i]>arr[j]:
                possible_lis = 1+dp[j]
                if possible_lis > cur_lis:
                    cur_lis = possible_lis
                    lis_ways[i] = lis_ways[j]
                elif possible_lis == cur_lis:
                    lis_ways[i] += lis_ways[j]
        
        dp[i] = cur_lis
        res_lis = max(res_lis, cur_lis)

    res_lis_ways = 0
    for i in range(n):
        if dp[i] == res_lis:
            res_lis_ways += lis_ways[i]

    return res_lis, res_lis_ways



arr = [1,2,2,3,6] # 2
print(LIS(arr))

arr = [1,3,5,4,7] # 2
print(LIS(arr))


arr = [1,1,1,1,1,1] # 6
print(LIS(arr))
 
arr = [3,1,1,2] # 2
print(LIS(arr))
