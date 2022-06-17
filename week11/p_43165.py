import sys
# sys.stdin = open('iput.txt')
from collections import deque 
input = sys.stdin.readline

numbers = [4, 1, 2, 1]
zero = [0]
numbers = zero+ numbers
target = 4

graph= [[]for _ in range((len(numbers)+1)*2)]
visited= [[0]*((len(numbers)+1)*2)]

for i in range(0,len(numbers)-1):
    graph[numbers[i]].append([numbers[i+1],-numbers[i+1]])
    graph[numbers[-i]].append([numbers[i+1],-numbers[i+1]])


print(graph)
# def bfs(n):
#     visited[n] == 1
#     q = deque(n)
#     while q:
#         k = q.pop(0)
#         print(k)
#         for i in graph[k][0]:
#             if visited[i] == 0:

# bfs(0)

    
