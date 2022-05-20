s = "hello"

# 가장 뒤에 항을 앞으로 가져온다
# ans = s[-1]
# print(ans)
# for i in range(-2, -len(s)-1,-1):
#     ans += s[i]
# print(ans)

def hello(n):
    global s
    if n == -len(s):
        return
    else:
        n -= 1
        k = s[-n]
        ans = k + hello(n-1)   
    return ans
print(hello(1))