import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
k = [int(input().rstrip()) for _ in range(n)]


isPrime = [True] * 10001 ## True 값을 10001 만큼 집어넣은 리스트
isPrime[1],isPrime[0] = False, False 
m = int(10000 ** 0.5) ## n의 제곱근까지 반복할거기 때문에 n의 제곱근을 계산해준다
for i in range(2, m+1): # 2부터 제곱근까지의 숫자들에 대한 배수만 제거해주면 됨
	if isPrime[i] == True: #True 값에 대해서만 판별이 들어감
		for j in range(i+i, 10001, i ): ##(i의 배수들은 다 False로 만들어줌) range(start, stop, step) step은 incrementation
			isPrime[j] = False

for i in k: 
	for j in range(i//2, 0, -1): #i의 절번에서부터 시작하면 소수 차이 가장 작은 것 출력 가능
		if isPrime[j] == True and isPrime[i-j] == True:
				print(j, i-j)
				break
