#LCS
# 소스:https://pacific-ocean.tistory.com/160
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

m = list(input().rstrip()) #sys.stdin.readline 때문에 그냥 input만 넣으면 오류남
n = list(input().rstrip())
li = [[0]*(len(n)+1) for _ in range(len(m)+1) ]

for i in range(len(m)):
    for j in range(len(n)):
        if m[i] == n[j]:
            li[i+1][j+1] = li[i][j] + 1
        else:
            li[i+1][j+1] = max(li[i][j+1], li[i+1][j], )

print(li[len(m)][len(n)])



#초기 접근방법 
# 1) 배열 요소마다 for문을 돌려서 카운트 해준다 -> 문제: 중복 문자 처리 못함
# 2) Dictionary 이용 -> order를 처리 못함
# 결론: 같으면 대각선에서 +1더해주고 아니면 위 왼 값중 큰 값