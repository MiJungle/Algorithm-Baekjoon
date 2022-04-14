import sys
input = sys.stdin.readline

x,y,w,h = map(int,input().split())

a= h-y
b = w-x

l = [a,b,x,y]

print(min(l))
