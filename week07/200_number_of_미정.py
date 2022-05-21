grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
m = len(grid)
for i in grid:
    n = len(i)
visited = [[0]*(n) for _ in range(m)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
count = 0
def sol():
    global count
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and visited[i][j] == 0:
                count += 1
                bfs(i,j)
    return count

def bfs(i,j):

    q = [[i,j]] 
    visited[i][j] = 1
    while q:
        s = q.pop(0)
        for i in range(4):
            nx = s[0] + dx[i]
            ny = s[1] + dy[i]
            if (nx <0 and nx >=m) and (ny<0 and ny >=n):
                continue
            if visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                q.append([nx,ny])

print(sol())
print(visited)