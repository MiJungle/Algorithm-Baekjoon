import sys
sys.stdin =open('input.txt')
input = sys.stdin.readline

n,m= map(int,input().split())
trees = list(map(int, input().split()))
trees.sort()
left = 1
right = max(trees)

def tree():
    global left, right
    while left <= right:
        print(left,right)
        ans = 0
        mid = (left + right)//2
        for i in range(n):
            if trees[i]> mid:
                ans += trees[i] - mid 
        if ans >= m:
            left = mid+ 1
            print("#2",left,right)
        else:
            right = mid- 1
            print("#3",left,right)
    return right
print(tree())