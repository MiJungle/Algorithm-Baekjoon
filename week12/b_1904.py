import sys
input = sys.stdin.readline

n = int(input())

def fibo(n):
    val = [0,1,2]
    if n <3:
        return val[n]
    else:
        for i in range(3, n+1):
            val.append((val[i-2]+val[i-1])%15746)
        return val[n]


print(fibo(n))