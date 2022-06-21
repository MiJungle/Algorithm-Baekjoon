import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

min = 2e9
ans= []

def zero():
    global n, min
    left = 0
    right = n-1
    for i in range(n):
        while left <right:
            if arr[left] + arr[right] == 0:
                return [arr[left], arr[right]]
            
            elif abs(arr[left] + arr[right]) < min:
                min = abs(arr[left] + arr[right])
                ans = [arr[left], arr[right]]
            elif arr[left] + arr[right] < 0:
                left += 1
            
            elif arr[left] + arr[right] > 0:
                right -= 1
        return ans

print(*zero(), end ='')