dartResult = "1D2S#10S"

def solution(dartResult):
    dartResult = list(map(str, dartResult))
    op= ["S","D","T","*", "#"]
    num = [dartResult[0]]
    for i in range(1,len(dartResult)):
        if dartResult[i] in op:
            k = num.pop()
            if dartResult[i] == "S":
                k = int(k)**1
            elif dartResult[i] =="D":
                k = int(k)** 2
            elif dartResult[i] =="T":
                k = int(k)** 3
            elif dartResult[i] =="*":
                if len(num)!= 0:
                    n2 = num.pop()
                    num.append(int(n2)*2)
                k = int(k) * 2
            elif dartResult[i] =="#":
                k = int(k) * (-1)
            num.append(k)
        else:
            if dartResult[i] == '0' and num[-1]=='1':
                num.pop()
                num.append(10)
            else:
                num.append(dartResult[i])
    return sum(num)