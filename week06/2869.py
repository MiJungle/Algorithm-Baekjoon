import sys
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B, V = map(int,input().split())
x = (V-A)/(A-B)
ans = x+1

print(math.ceil(ans))