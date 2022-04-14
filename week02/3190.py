# 소스: https://my-coding-notes.tistory.com/153

import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
applecount = int(input())
applespot = [list(map(int, input().split())) for _ in range(applecount)]
snakemove = int(input())
q = deque()
for i in range(snakemove):
    x, y = input().split()
    x = int(x)
    q.append((x,y))


(c, d) = (0, 0)
(a, b) = q.popleft()
print(a,b,c,d)
time = 0
if b == "D":
    for i in range(a):
        (c,d) = (c, d + i)
        if c == 0 or c == N-1 or d == 0 or d == N-1:
            break
        time += i
elif b == "L":
    for i in range(a):
        (c,d) = (c+i, d) 
        if c == 0 or c == N-1 or d == 0 or d == N-1:
            break
        time += i
print(time)

