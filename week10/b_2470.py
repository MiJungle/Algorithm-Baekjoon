import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
liquids= list(map(int,input().split()))
liquids.sort()
min = 2e9
left = 0
right = n-1
ans = []
def makezero():
    global min, left, right

    for _ in range(n):
        while left < right:
            if liquids[right] + liquids[left] == 0:
                ans = [liquids[left], liquids[right]]
                return ans
            elif abs(liquids[right] + liquids[left]) < min:
                min = abs(liquids[right] + liquids[left])
                ans = [liquids[left], liquids[right]]
            elif liquids[right] + liquids[left] <0:
                left += 1
            elif liquids[right] + liquids[left] >0:
                right -= 1
    return ans

print(*makezero(), end = '')

