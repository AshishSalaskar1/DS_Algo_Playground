def find_min_in_valley_array(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
       
        mid = (left + right) // 2
        print(left, right, mid)
        
        if arr[mid] > arr[mid + 1]:
            left = mid + 1
        elif arr[mid] < arr[mid + 1]:
            right = mid
        else:
            # Handle flat segments by moving to the right side of the flat segment
            # This ensures that we continue the search in the direction of the valley
            
            # If left and right pointers have the same value, move both pointers towards each other
            while left < right and arr[left] == arr[right]:
                # Adjust both pointers towards the middle of the flat segment
                left += 1
                right -= 1

                # Check if we have reached the end of the flat segment
                if left >= right:
                    break

    return arr[left]

# Example usage:
arr = [4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 1, 0, 2, 3, 4, 5, 5]
# arr = [4,3,2,2,2,2,2,2,2,1,1,1,1,1,0,2]
# arr = [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1]
# arr = [4,4,4,4,3,3,3,3,3,2,2,2,2,1,1,1,1,0,0,0,0,1,1,2,2,3,3,3,3,4,4,4,67,78,89]
# arr = [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
print(len(arr))
print(find_min_in_valley_array(arr))  # Output should be 0


"""
 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
"""