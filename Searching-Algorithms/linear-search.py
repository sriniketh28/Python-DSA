def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print(linear_search([1,2,7,4,5], 7))
print(linear_search([3,4,2,5,6], 1))
