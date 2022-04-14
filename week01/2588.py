import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int,input()))

numone = a*b[-1]
numtwo = a*b[-2]
numthree = a*b[-3]

ans = numone + 10*numtwo + 100*numthree
print(numone)
print(numtwo)
print(numthree)
print(ans)