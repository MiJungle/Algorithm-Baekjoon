import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline


n,m = map(int, input().split())
blue = list(map(int, input().split()))

total = sum(blue)
left = 1
right = total
aver = (left+right)//2

blue.sort()
addnum = 0
count =1



while count != m:
    count = 1
    addnum = 0
    for i in range(len(blue)):
        if addnum + blue[i]<=aver:
            addnum += blue[i]
            
        else:
            count += 1
            addnum = blue[i]
    left = aver + 1
    aver = (right+left)//2
print(aver-1)

