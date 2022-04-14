import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
operator = list(map(int,input().split()))

maximum = -1e9
minimum = 1e9 #1000000000

def dfs(depth, total, add, sub, mul, div): #(1, 5, 0, 0, 1, 0)
    global maximum, minimum
    if depth == n: #마지막 숫자 항에 도달하면 / n과 일치하면 멈추도록 
        maximum = max(total, maximum) #total 과 maximum 중에 큰애가 maximum이다 
        minimum = min(total, minimum)
        return
    else:
        if add:
            dfs(depth+1, total +nums[depth],add-1, sub, mul, div) #depth를 높임으로써 다음 숫자와 연산을 하게끔 
        if sub:
            dfs(depth+1, total-nums[depth], add, sub-1, mul, div)
        if mul:
            dfs(depth+1, total*nums[depth], add, sub, mul-1, div) #(2, 5* nums[1], 0, 0,0 ,0 )
        if div:
            dfs(depth+1, int(total/nums[depth]), add, sub,mul, div-1)
dfs(1, nums[0], operator[0], operator[1], operator[2], operator[3])
print(maximum)
print(minimum)