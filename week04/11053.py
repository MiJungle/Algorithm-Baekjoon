# 소스: https://www.youtube.com/watch?v=aPQY__2H3tE
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A = int(input())
Aj = list(map(int, input().split()))

def lis(A) :
    L= [1] * len(A)
    for i in range(1, len(L)):
        subproblems = [L[k] for k in range(i) if A[k]<A[i]] # i 보다 작은 index의 증가 수열 길이 
        L[i] = 1 + max(subproblems, default = 0)
    return max(L, default =0)
print(lis(Aj))