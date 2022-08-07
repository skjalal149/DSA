arr = [4, 7, 1, 9, 6, 8, 3, 5, 2]


def bubbleSort(arr):
    n = len(arr)
    if n <= 0:
        return 0
    for i in range(n):
        for j in range(1, n):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


def selectionSort(arr):
    n = len(arr)
    if n <= 0:
        return 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


import math


def bucket(arr):
    n = len(arr)
    bucket_size = round(math.sqrt(n))
    buckets = []
    max_value = max(arr)
    for i in range(bucket_size):
        buckets.append([])
    for i in range(n):
        val = math.ceil(arr[i] * bucket_size / max_value)
        buckets[val - 1].append(arr[i])
    for i in range(len(buckets)):
        buckets[i] = insertionSort(buckets[i])
    k = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
    return arr


def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    end = n - mid
    la = mergeSort(arr[:mid])
    ra = mergeSort(arr[mid:])

    i = j = 0
    sorted_array = []
    while i < mid and j < end:
        if la[i] < ra[j]:
            sorted_array.append(la[i])
            i += 1
        else:
            sorted_array.append(ra[j])
            j += 1

    while i < mid:
        sorted_array.append(la[i])
        i += 1
    while j < end:
        sorted_array.append(ra[j])
        j += 1
    return sorted_array


def QuickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr[0]
    i = 0
    j = n-1
    print(arr[n-1])

    while(i < n):
        while(arr[i] <= pivot):
            i+=1
        while(arr[j] < pivot):
            j+=1
        if (i<j):
            arr[i], arr[j] = arr[j], arr[i]
        i+=1
    arr[j], arr[0] = arr[0], arr[j]
    return arr

arr = [-4,-1,0,3,10]

for i in range(len(arr)):
    arr[i] *= arr[i]

print(insertionSort(arr))
