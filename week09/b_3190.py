import sys
from collections import deque
sys.stdin = open('input.txt')
input =sys.stdin.readline

n = int(input())
k = int(input())
apple = [list(map(int,input().split())) for _ in range (k)]
l = int(input())
change = deque(list(map(str,input().split())) for _ in range (l))

print(apple, change)

x= [-1,1,0,0]
y = [0,0,-1,1]

head = [0,0]

while change:
    print(change(0))
    go, dir = change.popleft()
    head = [head[0]+ int(go), head[1]]
    print(head)


