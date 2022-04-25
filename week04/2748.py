import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

def fibo(n):
    val = [0,1]
    if n<2:
        return val[n]

    else:
        for i in range(2, n+1):
            val.append(val[i-1] + val[i-2])
        return val[n]
    
print(fibo(n))