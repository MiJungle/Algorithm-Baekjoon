#동전
# https://d-cron.tistory.com/23
# https://sangminlog.tistory.com/m/289?category=870205
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split())) 
    M = int(input())
    li = [[0] * (M+1) for _ in range(N+1)] 
    for i in range(N+1):
        for j in range(M+1):
            if  coins[i] < j:
                print(coins[i], j )
                li[i][j] = max(li[i-1][j], li[i][j-coins[i]])+1
            else:
                li[i][j] = li[i-1][j]
    print(li[N][M])
    

