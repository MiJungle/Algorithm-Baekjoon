import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
M = deque(range(1, N+1))

while len(M) != 1:
    M.popleft()
    k = M[0]
    M.append(k)
    M.popleft()
print(M[0])
