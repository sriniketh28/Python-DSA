import heapq

max_heap = []

heapq.heapify(max_heap)

# We use heapq module to implement Heaps in Python. 
# By default Min Heap is implemented by heapq module. 
# So we multiply each value by -1 so that we can use it as MaxHeap.
heapq.heappush(max_heap, -1 * 10)
heapq.heappush(max_heap, -1 * 30)
heapq.heappush(max_heap, -1 * 20)
heapq.heappush(max_heap, -1 * 400)

def printMaxHeap(max_heap):
    print(list(map(lambda a:a*-1, max_heap)))

printMaxHeap(max_heap)

heapq.heappop(max_heap)

printMaxHeap(max_heap)
