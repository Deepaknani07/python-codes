def binary_search(arr, target):
    left, right = 0, len(arr) -1
    
    while left <= right:
        mid = (left + right)  // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Finding 7 in {arr}")
print(f"found at index: {binary_search(arr, 7)}")
print(f"Finding 10 in {arr}")
print(f"Found  at index: {binary_search(arr,10)}")
