n = int(input())
ans = 0
def pibo(n):
    global ans
    i = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    ans1 = 0
    ans2 = 1
    while i != n: 
        ans3 =  ans1 + ans2
        ans1, ans2 = ans2, ans3
        i += 1  
    return ans1

print(pibo(n))

