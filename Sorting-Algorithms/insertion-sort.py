def insertion_sort(arr):
    for i in range(1,len(arr)):
        anchor = arr[i]
        j = i-1
        while j>=0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = anchor
    return arr

 
arr = [10,4,5,2,1,6]
print(insertion_sort(arr))

