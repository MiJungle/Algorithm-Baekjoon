import sys
import heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline

left = []
right = []

n = int(input())

for i in range(n):
    k = int(input())

    if len(left) == len(right):  
        heapq.heappush(left,-k)
    else:
        heapq.heappush(right, k)

    if right and right[0] < -left[0]:  ##right 거를 left랑 바꾸는 작업
        f = heapq.heappop(left)
        s = heapq.heappop(right)
        heapq.heappush(left, -s)
        heapq.heappush(right, -f)

    print(-left[0])






