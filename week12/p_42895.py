n = 5
num = 12
answer = -1
dp = [[] for _ in range(9)]
for i in range(1, 9) :
    dp[i].append(int(str(n) * i))
    for j in range(1, i) :
            for num1 in dp[j] :
                for num2 in dp[i-j] :
print(dp)