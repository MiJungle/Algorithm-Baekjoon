import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

queue = deque()

for _ in range(int(input())):
    m = list(map(str, input().split()))
    if m[0] =="push":
        queue.append(m[1])
    elif m[0] == "back":
        if len(queue)!= 0: 
            print(queue[-1])
        else:
            print(-1)           
    elif m[0] == "empty":  
        if len(queue)!= 0: 
            print(0) 
        else:
            print(1)      
    elif m[0] == "pop": 
        if len(queue)!= 0: 
            print(queue.popleft())      
        else:
            print(-1)
    elif m[0] == "front": 
        if len(queue)!= 0: 
            print(queue[0])
        else:
            print(-1)
    elif m[0] == "size":
        print(len(queue))     