import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
objects = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]

bag = [[0]* (k+1) for _ in range(n+1)]

def baggy():
    for i in range(1,n+1):
        for j in range(1,k+1):
            w = objects[i][0]
            v = objects[i][1]
            if w > j:
                bag[i][j] = bag[i-1][j]
            else:
                bag[i][j] = max(bag[i-1][j], bag[i-1][j-w] + v)
    return bag[n][k]
print(baggy())