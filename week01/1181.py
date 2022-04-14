import sys

input = sys.stdin.readline

N = int(input())
M = [ input().rstrip() for _ in range(N) ]

M = list(set(M))
M.sort() 
M.sort(key=lambda x:len(x) )

for i in M:
    print(i)