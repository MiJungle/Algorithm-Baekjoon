import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
blue =0
white = 0
def papercut(x,y,n):
    global blue, white
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[x][y] != paper[i][j]:
                papercut(x,y, n//2)
                papercut(x+n//2,y,n//2)
                papercut(x, y+n//2,n//2)
                papercut(x+n//2,y+n//2,n//2)
                return
    if paper[x][y] == 1:
        blue +=1
    else:
        white += 1
papercut(0,0,n)
print(white)
print(blue)
