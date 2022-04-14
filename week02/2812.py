# 소스: https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-2812%EB%B2%88-%ED%81%AC%EA%B2%8C-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(map(int, input().strip()))

result = []

for x in num: 
    if not result: #result가 비어있으면
        result.append(x) #result에 x값을 더함

    while result and result[-1] < x and K != 0: #result에 값이 있고 result[-1]보다 현재 값이 더 크면 
        K -= 1
        result.pop() # pop
    result.append(x) # 반복문이 돌아갈때마다 x를 더함

while K != 0:  #K가 0 될 때까지 나머지 pop
    K -= 1
    result.pop()

print(*result, sep='')

#앞자리 수들에서 K가 0이 아닐때까지 작은 숫자들을 제거해준 후, 뒤에 숫자들을 리스트에 넣은 후 K가 0이 될대까지 다 빼버림