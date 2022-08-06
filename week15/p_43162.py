
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	
n = 3
visited = [0]*n
def solution(n):
    count = 0
    for i in range(n):
        if visited[i] != 1:
            bfs(i)
            count += 1
    return count


def bfs(i):
    q = [i]
    visited[i] = 1
    while q:
        t = q.pop(0)
        for i in range(len(computers[t])):
            if computers[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1
        
print(island(n))