def partition(arr, start, end):
    pivot = arr[start]
    count = 0
    for i in range(start, end+1):
        if pivot > arr[i]:
            count += 1
    pivotIndex = start + count
    arr[start], arr[pivotIndex] = arr[pivotIndex], arr[start]
    i, j = start, end
    while i<j:
        if arr[i] < pivot:
            i += 1
        elif arr[j] > pivot:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return pivotIndex

def quick_sort(arr, start, end):
    if start >= end:
        return
    # Modern compiler basically do tail call elimination to optimize the tail recursive code themselves.
    # Quick Sort Tail Call Optimization
    # We can limit the worst case auxiliary space to O(Log n)
    while start < end :
        pivotIndex = partition(arr, start, end)
        quick_sort(arr, start, pivotIndex-1)
        start = pivotIndex + 1


arr = [10, 80, 30, 90, 40, 50, 70]
quick_sort(arr,0,len(arr)-1)
print(arr)
