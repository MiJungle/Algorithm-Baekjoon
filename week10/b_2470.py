import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
liquids= list(map(int,input().split()))
liquids.sort()
ans = []
min = 2e9
def makezero():
    global min
    left = 0
    right = left+1
    while left < right:
        for i in range(n):
            if liquids[left] + liquids[right] == 0:
                ans = [liquids[left], liquids[right]]
                return ans
            if abs(liquids[left] +liquids [left])< min:
                min = liquids[right] + liquids[left]
                ans = [liquids[left], liquids[right]]
                left += 1
            else:
                right -= 1
        return ans
print(*makezero(),"")
        

