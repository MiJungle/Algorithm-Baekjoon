# 소스: https://jjangsungwon.tistory.com/10
# https://velog.io/@grace0st/%EA%B3%B1%EC%85%88-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

A, B, C = map(int,input().split())

def power(A, B):
    if B == 1:
        return A % C
    else:
        temp = power(A, B // 2)
        if B % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * A % C
print(power(A, B))    