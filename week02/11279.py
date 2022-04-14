# 소스: https://kjhoon0330.tistory.com/entry/Python-heapq-%EB%AA%A8%EB%93%88
# https://yunaaaas.tistory.com/36

import sys, heapq
from queue import PriorityQueue

sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

li = []
for i in range(N):
    M = int(input())
    if M == 0 and len(li) == 0:
        print("0")
    elif M != 0:
        # heapq.heappush(li, (-M,M)) #음수를 붙이면 큰 숫자가 앞에 오게됨
        heapq.heappush(li, -M)
    elif M == 0 and len(li)!= 0:
        print(-heapq.heappop(li)) 
        # print(heapq.heappop(li)[1]) #그 중 index 1 (M) 만 출력
