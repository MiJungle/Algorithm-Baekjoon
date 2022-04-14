import sys
input = sys.stdin.readline

N = int(input())

def Moo(N):
    if N == 0:
        return
    else:
        print("m" + "o" * (N+1))
        Moo(N-1)
print(Moo(N))