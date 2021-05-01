def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


print(selectionSort([64, 25, 12, 22, 11]))

