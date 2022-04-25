#아주 평범한 배낭
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())

bag = [[0,0]]
thing = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    bag.append(list(map(int, input().split())))

for i in range(1, n+1): #세로
    for j in range(1, k+1): #가로
        w = bag[i][0]
        v = bag[i][1]

        if j < w: # 그 해당 아이템의 무게가 j무게 보다 큰 경우 - 못넣는 경우
            thing[i][j] = thing[i-1][j] #그 전좌표 (다른 물건의) 무게의 가치를 넣어줌 
        else:
            thing[i][j] = max(thing[i-1][j], thing[i-1][j-w]+v) #그 전좌표 무게 가치(최대value보장) vs 남은 무게 만큼의 최대 v 더하기 지금 무게 v

print(thing[n][k])