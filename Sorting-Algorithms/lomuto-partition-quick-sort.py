def lomutoPartition(arr,start,end):
    i = start - 1
    pivot = arr[end]
    for j in range(start,end+1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    pivotIndex = i+1
    return pivotIndex

def quick_sort(arr,start,end):
    if start >= end:
        return
    pivotIndex = lomutoPartition(arr,start,end)
    quick_sort(arr,start,pivotIndex-1)
    quick_sort(arr,pivotIndex+1,end)


arr = [5,3,8,4,2,7,1,10]
quick_sort(arr,0,len(arr)-1)
print(arr)

arr = [10,80,30,90,40,50,70]
quick_sort(arr,0,len(arr)-1)
print(arr)
