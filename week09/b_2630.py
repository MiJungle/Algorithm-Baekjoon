import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

white,blue= 0,0

def papercut(x,y,n):
    global white,blue
    for i in range(x, x+n):
        for j in range(y, y+n):
            if m[x][y] != m[i][j]:
                papercut(x,y,n//2)
                papercut(x+n//2,y,n//2)
                papercut(x, y+n//2, n//2)
                papercut(x+n//2,y+n//2,n//2)
                return

    if m[x][y] ==0:
        white += 1
    else:
        blue += 1

papercut(0,0,n)
print(white)
print(blue)