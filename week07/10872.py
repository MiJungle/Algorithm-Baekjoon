import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
def recur(n):
    ans = n
    if n == 0:
        return 1
    else:
        ans = ans * recur (n-1)
        return ans

print(recur(n))