import sys, heapq
from queue import PriorityQueue

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
leftHeap = []
rightHeap = []
for i in range(n):
    num = int(input())

    if len(leftHeap) == len(rightHeap): 
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)
    
    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, - leftValue)
    
    print(-leftHeap[0])







# 시간초과
# N = int(input())
# num = [int(input().rstrip()) for _ in range(N)]

# heap = []
# for n in num:
#     heapq.heappush(heap, n)
#     heap.sort()
#     k = len(heap)//2
#     heaplen = len(heap)

#     if heaplen == 1 or heaplen ==2 :
#         print(num[0])
#     elif heaplen > 2 and heaplen %2 == 0 :
#         if heap[k] < heap[k-1]:
#             print(heap[k])
#         else:
#             print(heap[k-1])
#     elif heaplen %2 != 0:
#         print(heap[k])

