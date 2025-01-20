import sys

# def get_nearest_3sum(arr: list[int], target: int) -> int:
def get_nearest_3sum(arr, target):
    n = len(arr)
    min_abs_diff = float("inf")

    arr.sort()
    for i in range(n-2):
        lo, hi = i+1, n-1
        while lo<hi:
            csum = arr[i] + arr[lo] + arr[hi]
            diff = abs(target - csum)
            if diff < min_abs_diff:
                min_abs_diff = diff

            if diff == 0:
                return 0
            if csum > target:
                hi -= 1
            else:
                lo += 1
    
    return min_abs_diff


def main():
    for _ in range(int(input())):
        n,target = list(map(int,sys.stdin.readline().split()))
        arr = list(map(int,sys.stdin.readline().split()))
        print(get_nearest_3sum(arr, target))

main()
