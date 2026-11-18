def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

arr = [3, 8, 12, 17, 23, 31, 38, 45, 52, 64, 71, 86]
print(binary_search(arr, 45))   # 7
print(binary_search(arr, 50))   # -1
