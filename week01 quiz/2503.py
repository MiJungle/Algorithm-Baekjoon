import sys
input = sys.stdin.readline

n = int(input())
m = [list(map(int,input().split())) for _ in range(n)]
print(m)

