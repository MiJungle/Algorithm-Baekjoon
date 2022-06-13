import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left = 0
right = n-1
min = 2e9
def zero():
    global left,right, min
    ans = []
    while left < right:
        for _ in range(n):
            if liquid[left] + liquid[right] ==0:
                ans = [liquid[left], liquid[right]]
                return ans
            elif abs(liquid[left]+ liquid[right]) < min:
                min = liquid[left] + liquid[right]
                ans = [liquid[left], liquid[right]]
            elif liquid[left] + liquid[right] > 0:
                right -= 1
            else:
                left += 1
    return ans

print(*zero(),end ='')

