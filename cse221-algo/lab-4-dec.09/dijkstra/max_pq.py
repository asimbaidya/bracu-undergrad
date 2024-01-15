import heapq as heap

a = [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)]
b = a.copy()
b.reverse()

print(a)
print(b)

heap._heapify_max(a)
heap._heapify_max(b)
print(a)
print(b)
