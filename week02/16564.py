import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int,input().split())
Level = [int(input().rstrip()) for _ in range(N)]


def levelup():
    first = 1
    end = max(Level)

    while first <= end:
        mid = (first + end)//2
        count = 0
        for i in Level:
            if i<= mid:
                count += mid - i
        
        if count == K: # 바로 mid 값 출력
            return mid
        elif count > K: 
            if first == end: 
                return mid - 1  
            else:
                end = mid - 1 #first = end 아니면 end 값 계속 쫍히기
        else:
            if first == end:
                return first
            else:
                first = mid + 1

print(levelup())