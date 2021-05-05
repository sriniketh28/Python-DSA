def binary_search(arr, x):
    startIndex = 0
    endIndex = len(arr)-1
    while startIndex <= endIndex:
        midIndex = (endIndex + startIndex)//2
        if arr[midIndex] == x:
            return midIndex
        elif arr[midIndex] > x:
            endIndex = midIndex - 1
        else:
            startIndex = midIndex + 1
    return -1

arr = [1,2,3,4,5,6,7]
print(binary_search(arr, 5))
