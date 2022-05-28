# https://miin-z.tistory.com/25?category=872727
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

#이분탐색 - 정렬하고, 반으로나눠서 그걸 기준으로 대조해가면서 범위를 좁힘 
#투포인터느낌인데 ..
#가운데서부터 0이랑 대조하면서 right값 줄이거나 left값 늘림
#더해서 최소값을 계속 갱신해나감, 0이면 바로 return
#right left 값을 어떻게 처음에 정하고 값을 +- 하는지 잘 모르겠음 
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
low = 2e9
ans = []

def liquid():
    global low,ans
    left = 0
    right = n-1
    mid = (left+right)//2
    while left < right:
        k = arr[left] + arr[right]
        if abs(k) < low:
            low = abs(k)
            ans= [arr[left], arr[right]]
        if k < 0:
            left = mid +1
        else:
            right = mid -1
        mid = (left+right)//2  
    return ans
print(*liquid(), end=' ')
