import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B, C = map(int, input().split())

try:
    X = A//(C-B) +1
    if X <0: print(-1)
    else: print(X)
except:
    print(-1)

