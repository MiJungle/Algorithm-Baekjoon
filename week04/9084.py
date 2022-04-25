#동전

# 소스: https://pacific-ocean.tistory.com/217
# 비슷한 문제 풀어볼것 : https://www.acmicpc.net/problem/2293
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    m = int(input())
    dp = [0 for i in range(m + 1)]
    dp[0] = 1
    for i in c: #동전의 각 금액들
        for j in range(1, m + 1): #1 ~ M 액수
            if j - i >= 0: # M을 j-i만큼 채워야하는 경우
                dp[j] += dp[j - i] #j-i 액수를 만드는 방법수만큼 더해줌
    print(dp[m])


