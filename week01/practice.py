import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N,r,c = map(int, input().split())
ans = 0

def rec(x, y, n):
    global ans
    if x == r and y == c:
        return
    if n == 0:
        return

    mid = 2**(n-1)

    if 0 <= r-x < mid and 0<= c-y < mid:
        rec(x,y, n-1)
    elif 0<= r-x < mid and mid <= c-y < 2*mid:
        ans += mid**2
        rec(x,y+mid,n-1)
    elif r-x < mid  and 0 <= c-y < mid:
        ans += (mid**2)*2
        rec(x+mid, y, n-1)
    elif mid <= r-x < 2*mid and mid <= c-y <2*mid:
        ans += (mid ** 2)*3
        rec(x+mid, y+mid, n-1)

rec(0,0,N)
print(ans)