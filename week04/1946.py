# 소스: https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%801946%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%8B%A0%EC%9E%85-%EC%82%AC%EC%9B%90
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for i in range(0,int(input())):
    Cnt = 1
    N = int(input())
    spec = [list(map(int,input().split())) for _ in range(N)]

    spec.sort() # 서류 기준 오름차순 정렬
    Max = spec[0][1] #숫자가 낮은, 즉 순위가 높은 1번뻔쨰 사람은 무조건 통과
    
    for i in range(1,N):
        if Max > spec[i][1]: #순위1 사람의 면접보다 크기만하면 그사람은 합격, 같은 방식으로 반복
            Cnt += 1
            Max = spec[i][1]

    print(Cnt)