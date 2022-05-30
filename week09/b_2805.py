import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
ans = []

def cut_tree():
    left = 0
    right = n-1
    mid = (left+right)//2
    length = trees[mid]

 #최대 길이는 마지막 나무 높이만큼 
    num = 0
    idx = 0
    while length <= trees[-1] or length >= 0:
        if trees[idx] > length:
            num += trees[idx]- length
        print("first:",length, num)
    if num == m: #m 값 목표 도달 
        return length
    elif num > m:
        length = length + 1
    else: 
        length = length - 1
    print(length, num)
    return length
print(cut_tree())