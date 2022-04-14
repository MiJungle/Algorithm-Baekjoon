import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int,input().split())
result = []
q = deque(range(1,N+1))

while q:
    for _ in range(K-1):
        q.append(q.popleft()) #K-1 번째까지 항을 다 빼고 뒤로 더함
    result.append(q.popleft()) # 가장 앞에거를 result에 더함 

print("<", end="")
print(*result, sep=", ",end="")
print(">")


