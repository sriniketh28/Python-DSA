def hoarePartition(arr,start,end):
    pivot = arr[start]
    i = start - 1
    j = end + 1
    while True:

        while True:
            i += 1
            if arr[i] >= pivot:
                break
        
        while True:
            j -= 1
            if arr[j] <= pivot:
                break

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr,start,end):
    if start >= end:
        return
    partitionIndex = hoarePartition(arr,start,end)
    quick_sort(arr,start,partitionIndex)
    quick_sort(arr,partitionIndex+1,end)


arr = [5,3,8,4,2,7,1,10]
quick_sort(arr,0,len(arr)-1)
print(arr)
