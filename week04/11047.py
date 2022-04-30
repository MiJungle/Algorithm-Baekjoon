import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())

m = [int(input().strip()) for _ in range(n)]
m.sort(reverse = True)

def greedy(k):
    coincount = 0
    for i in m:
        if i <= k:
            num = k//i
            coincount += num
            k = k % i 
        if k == 0:
            return coincount

print(greedy(k))

    