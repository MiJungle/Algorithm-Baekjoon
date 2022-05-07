import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for i in range(int(input())):
    M,N,K = map(int, input().split())
    li= [[0]*(M+1) for _ in range(N+1)]
    for _ in range(K):
        x, y = map(int, input().split())
        li[x][y] = 1
    print(li)
    x= [-1,1,0,0]
    y = [0,0,-1,1]
