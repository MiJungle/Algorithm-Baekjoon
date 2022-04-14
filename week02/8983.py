# 소스: https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-8983%EB%B2%88-%EC%82%AC%EB%83%A5%EA%BE%BC-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 사냥꾼의 위치 정렬
# 동물의 위치 완전 탐색
# - 해당 동물의 위치에서 가장 가까운 사냥꾼이 위치를 이분탐색
# - 사냥꾼의 위치, 사냥꾼의 왼쪽 위치, 사냥꾼의 오른쪽 위치와 동물 사이의 거리가 L이하이면 
# anser +=1

# 각 동물의 위치에서 가장 가까운 사냥꾼의 위치를 찾고 사정거리 내인지 확인
# 사냥꾼의 위치는 정렬을 하여 이분탐색 가능
# 각 동물의 위치에서 가장 가까운 사냥꾼의 위치: a좌표가 같을 경우
# a좌표가 다르면서 이분탐색이 끝날 경우가 있으니 현재 사냥꾼의 위치 전후로 L과 비교해주어야한다.


import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

M, N, L = map(int,input().split())
X = list(map(int, input().split())) #L의 X좌표 
X.sort()
print(X)
animals = [ list(map(int, input().split())) for _ in range(N)]

answer = 0
for a, b in animals:
    start = 0
    end = len(X)-1
    mid = 0
    while start < end:
        mid = (start+end)//2
        if X[mid] < a:
            start = mid + 1
        elif X[mid] > a:
            end = mid -1
        else:
            start = mid
            break
    if abs(X[start]-a)+b <= L:
        answer += 1
    elif start+1 < len(X) and abs(X[start+1]-a) + b <= L:
        answer += 1
    elif start > 0 and abs(X[start-1]-a)+b <= L:
        answer += 1
print(answer)