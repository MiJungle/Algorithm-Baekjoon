import sys
input = sys.stdin.readline

a,b = list(map(str,input().split()))

aReverse = a[::-1]
bReverse = b[::-1]

if aReverse > bReverse: 
    print(aReverse)
else:
    print(bReverse)