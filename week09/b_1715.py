import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
ans = []

for _ in range(n):
    m = int(input())
    heapq.heappush(ans, m)


if len(ans) ==0:
    print(0)    
else: 
    s =0
    while len(ans) != 1:
        a = heapq.heappop(ans)
        b = heapq.heappop(ans)
        s+= a+ b
        heapq.heappush(ans, a+b)
    print(s)