arr = [6, 3, 5, 9, 1, 0, 3, 4]


def linearSearch(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return "not found"


def binarySearch(arr, val):
    arr.sort()
    print(arr)
    n = len(arr)
    n = n//2
    if arr[n] == val:
        return n
    elif arr[n] > val:
        return binarySearch(arr[:n], val)
    else:
        return binarySearch(arr[n:], val)

print(binarySearch(arr, 6))
