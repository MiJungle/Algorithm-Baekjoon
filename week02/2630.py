# 소스: https://developmentdiary.tistory.com/334
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
color_paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def cut(x,y,n):
    global blue, white
    check = color_paper[x][y]
    for i in range(x, x+n): 
        for j in range(y, y+n):
            if check != color_paper[i][j]: #같지 않으면 자름 
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return
    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return 

cut(0, 0, n)
print(white)
print(blue)