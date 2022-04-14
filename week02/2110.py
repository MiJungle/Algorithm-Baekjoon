# https://claude-u.tistory.com/448
# https://tmdrl5779.tistory.com/119


import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

x, y = map(int, input().split())
house = [int(input().rstrip()) for _ in range (x)]
house.sort()
print(house)

def binary():
    left = 1
    right = max(house)-1 

    while left <= right:
        mid = (left + right) // 2  ##공유기간의 거리를 중간값부터 대입
        count = 1 #이미 공유기 하나는 설치했다고 가정
        wifi = min(house) + mid #리스트 첫항으로부터 mid 거리만큼에 공유기를 설치

        for i in house:
            if wifi <= i: # 공유기 설치한 곳과 인접한 거리에 집이 위치해있으면 공유기 설치 가능하다는 뜻
                count += 1  # 그러면 카운트 숫자 높임
                wifi = i + mid # 공유기 설치한 곳 위치를 재설정 

        if count >= y:
            left = mid + 1
        elif count < y:
            right = mid - 1
    return right
print(binary())
