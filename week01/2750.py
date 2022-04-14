import sys

input = sys.stdin.readline
n = int(input())
m = [ int(input().rstrip()) for _ in range(n)]

m.sort()

for i in m:
    print(i)

