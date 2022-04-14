import sys
sys.stdin = open('input.txt')

# print(sys.stdin.readline())

N, r, c = map(int, sys.stdin.readline().split())
ans = 0

def rec(x, y, n):   #N=2 r=3 c=1 / x=0 y=0 n=2 # x+mid = 2 y=0 n=1
    global ans  #함수 내부에서 전역 변수를 사용하기 위해서는 반드시 global 키워드를 사용하여 해당 전역 변수를 재선언
    if x == r and y == c: 
        return
    if n == 0:
        return

    mid = 2**(n-1) # 2 / 1
    if 0 <= r-x < mid and 0 <= c-y < mid:
        rec(x, y, n-1) 
    elif 0 <= r-x < mid and mid <= c-y < 2*mid:
        ans += mid**2 
        rec(x, y+mid, n-1) 
    elif mid <= r-x < 2*mid and 0 <= c-y < mid:
        ans += (mid**2)*2 #8 
        rec(x+mid, y, n-1) #(2 0 1)  r-x = 1 c-y = 0
    elif mid <= r-x < 2*mid and mid <= c-y < 2*mid:
        ans += (mid**2)*3 #3  r-x = 1 c-y = 1 mid =1
        rec(x+mid, y+mid, n-1)#( 3, 1, 0)

rec(0,0,N)
print(ans)

#다른 사람이 적은 4줄만에 끝나는 식
# def sol(N, r, c):
#     if N == 0:
#         return 0
#     return 2*(r % 2) + (c % 2) + 4*sol(N-1, int(r/2), int(c/2))