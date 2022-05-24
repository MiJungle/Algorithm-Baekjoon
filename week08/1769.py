# 숫자를 리스트로 만들어서
# 해당 숫자를 더한게 Sum 값
# 또 그 sum값 각각의 숫자를 리스트로 만듬
# 그 숫자가 10보다 작아질 때까지 

n = input()
count = 1
def recur(n):
    global count
    if int(n) < 10:
        count = 0 
    k = sum(list(map(int,str(n))))
    if k <10:
        print(count)
        if k % 3 == 0:
            print('YES')
        else:
            print('NO')
    else:
        count += 1
        recur(k)

recur(n)