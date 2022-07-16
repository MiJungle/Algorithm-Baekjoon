import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

blue = 0
white = 0
def cut(x,y,n):
    global blue, white
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[x][y] != paper[i][j]:
                cut(x,y,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                cut(x,y+n//2,n//2)
                return
            
    if paper[i][j]== 0:
        white += 1
    else:
        blue +=1
cut(0,0,n)
print(white)
print(blue)

# ______________________________-

import sys

N = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white, blue = 0, 0
def rec(x, y, n):
    global white, blue
    
    if n == 0:
        return
        
    total_sum = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            total_sum += grid[i][j]
    if total_sum == 0:
        white += 1
        return
    if total_sum == n**2:
        blue += 1
        return

    mid = n//2
    rec(x, y, mid)
    rec(x, y+mid, mid)
    rec(x+mid, y, mid)
    rec(x+mid, y+mid, mid)

rec(0, 0, N)
print(white)
print(blue)