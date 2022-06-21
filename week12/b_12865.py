import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

arr= sorted(arr, key =lambda x: x[1])

max = 0
left = 0
right = len(arr)-1
for i in range(len(arr)-1, 0, -1):
    if k >= arr[i][0]:
        max += arr[i][1]
        k = k- arr[i][1]
        print(arr[i][0])
print(max)