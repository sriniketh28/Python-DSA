import heapq

def heap_sort(arr):
    heap = arr
    heapq.heapify(heap)
    sorted_arr = []
    while(len(heap)>0):
        sorted_arr.append(heapq.heappop(heap))
    return sorted_arr

print(heap_sort([13, 21, 15, 5, 26, 4, 17, 18, 24, 2]))
