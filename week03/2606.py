import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
m = int(input())
virus = [0 for _ in range(n+1)]
s = [[0]*(n+1) for _ in range(n+1)]
for _ in range(0,m):
    x, y = map(int,input().split())
    s[x][y] = s[y][x] = 1

##dfs 로 풀기 
def dfs(v):
    virus[v] = 1
    for i in range(n+1):
        if virus[i] == 0 and s[v][i] == 1:
            dfs(i)
dfs(1)    
count = virus.count(1)

print(count-1) #자기 자신 제외

#bfs 로 풀기

def bfs(v):
    queue = [v]
    virus[v] = 1
    while queue:
        v = queue.pop(0)
        for i in range(n+1):
            if virus[i] == 0 and s[v][i] == 1:
                queue.append(i)
                virus[i] = 1
bfs(1)
count = virus.count(1)
print(count-1) 