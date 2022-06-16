import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int,input().split())
trees = list(map(int, input().split()))
trees.sort()
left = 1
right = max(trees)

def cut():
    global left, right
    while left <= right:
        ans = 0
        mid = (left + right)//2
        for tree in trees:
            if tree > mid:
                ans += tree-mid
        if ans >= m:
            left = mid +1
        else:
            right = mid -1
    return right
print(cut())