# In this Bucket sort we are going to sort the numbers in interval [0, 1)
def insertion_sort(arr):
    for i in range(1,len(arr)):
        anchor = arr[i]
        j = i-1
        while j>=0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = anchor

    return arr

def bucket_sort(arr):
    bucket = []
    
    for i in range(10):
        bucket.append([])

    for j in arr:
        index = int(j*10)
        bucket[index].append(j)

    for i in range(10):
        bucket[i] = insertion_sort(bucket[i])
        
    k = 0
    for i in range(10):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1

    return arr


arr = [0, 0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print(bucket_sort(arr))
