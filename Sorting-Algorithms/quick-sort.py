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
    
    pivotIndex = partition(arr, start, end)
    quick_sort(arr, start, pivotIndex-1)
    quick_sort(arr, pivotIndex+1, end)


arr = [10, 80, 30, 90, 40, 50, 70]
quick_sort(arr,0,len(arr)-1)
print(arr)

