import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
data.sort()
M = int(input())
search = list(map(int, input().split()))
print(data, search)

def binary_search(data, num):
    start = 0
    end = N-1
    while 1:#계속 돌려라 어디선가 브레이크 걸릴 때까지
        key = int((start+end)//2)
        if num == data[start] or num == data[end]: ##찾는 대상이 리스트의 앞 혹은 끝 지점에 있으면
            print(1)
            break
        if data[key] == num:
            print(1)
            break
        if key == start or key == end: ##범위를 좁히고 좁혀서 중간값이 start / end가 되었을 때 start end 사이 숫자가 없을 때
            if data[key] != num:
                print(0)
                break
        elif data[key] > num:
            end = key-1
        elif data[key] < num:
            start = key + 1

for num in search:
    binary_search(data,num)
