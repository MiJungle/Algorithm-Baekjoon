# 소스: https://claude-u.tistory.com/446
# Pypy로만 됨

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
Tree = list(map(int, input().split()))
#sort 하면 시간초과남, 그리고 max값 구해서 빼는 거라서 sort 필요없음
start, end = 1, max(Tree)

while start <= end:
    mid = (start+end) //2 #중간값을 구해준 후

    log = 0 #log 값 0으로 다시 세팅해줌 
    for i in Tree:
        if i >= mid:
            log += i - mid  # 중간값보다 같거나 큰경우 그만큼 빼서 (나무를 잘라서) log에 더해줌
            
    if log >= M: #M이랑 비교헀을 때 더 크면 다시 mid 를 조정
        start = mid + 1
    else:
        end = mid - 1
print(end)