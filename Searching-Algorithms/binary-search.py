def binary_search(arr, startIndex, endIndex, x):
    midIndex = (startIndex + endIndex)//2
    if startIndex > endIndex:
        return -1
    else:
        if arr[midIndex] == x:
            return midIndex
        elif arr[midIndex] > x:
            return binary_search(arr, startIndex, midIndex-1, x)
        else:
            return binary_search(arr, midIndex+1, endIndex, x)

arr = [1,2,3,4,5,6]
print(binary_search(arr,0,len(arr)-1,6))
arr = [ 2, 3, 4, 10, 40 ]
print(binary_search(arr,0,len(arr)-1,10))
    
 
