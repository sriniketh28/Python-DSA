import heapq 

min_heap1 = [5, 7, 9, 1, 3]

# using heapq.heapify(list) to convert list into heap
heapq.heapify(min_heap1)

heapq.heappush(min_heap1, 4)

heapq.heappop(min_heap1)

print(min_heap1)

min_heap2 = [5, 7, 9, 4, 3]

min_heap3 = [5, 7, 9, 4, 3]

heapq.heapify(min_heap2)
heapq.heapify(min_heap3)

# heapq.heappushpop(heap, item) and heapq.heapreplace(heap, item) are used to push and pop items simultaneously
# heapq.heapreplace(heap, item) returns the smallest value originally in heap regardless of the pushed element as opposed to heapq.heappushpop(heap, item).
heapq.heappushpop(min_heap2, 2)
# pops 2

heapq.heapreplace(min_heap3, 2)
# pops 3

print(min_heap2)
print(min_heap3)

print(heapq.nlargest(2, min_heap1))
print(heapq.nsmallest(2, min_heap1))

