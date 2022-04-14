import sys
input = sys.stdin.readline

count = 0
num = int(input())
if num < 100:
    count += num
    print(count)
else:
    for i in range(100, num+1) :
        numList = str(i)
        if int(numList[0]) - int(numList[1]) == int(numList[1]) - int(numList[2]):
            count +=1
    count += 99
    print(count)


