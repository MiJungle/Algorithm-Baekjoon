import sys, heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
num = []

for i in range(N):
    M = int(input())
    heapq.heappush(num, M)

if len(num) == 1:
    print(0)

else:
    sum = 0
    while len(num) != 1:
        a = heapq.heappop(num)
        b = heapq.heappop(num)
        sum +=   a + b
        heapq.heappush(num, a+b)
    print(sum)

