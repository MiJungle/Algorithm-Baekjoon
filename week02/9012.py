import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())
M = [input().rstrip() for _ in range(T)]

for i in M:
    openbracket = []
    closebracket = []
    for j in range(len(i)):
        if i[j] == "(":
            closebracket.append(")") #close bracket이 필요함을 의미
            openbracket.append("(") #닫혀야할 open bracket있음을 의미
        if i[j] ==")":
            if len(closebracket) != 0 and len(openbracket) != 0:
                closebracket.pop(-1) #있어야할 close bracket이 출력됬음을 의미
                openbracket.pop(-1) #open bracket이 닫혔음을 의미
            else:
                closebracket.append(")") #아닌 경우 불필요한 close bracket임을 의미 
        
    if len(openbracket) == 0 and len(closebracket) ==0:
        print("YES")
    else:
        print("NO")

##open bracket 이 입력되면, openbracket 과 close bracket 리스트에 각각 넣어준다.
#close bracket이 나오면 기존에 입력된 openbracket 과 close bracket에서 pop
#open bracket 리스트에 아무것도 없거나 closebracket에 아무것도 없으면 불필요한 close bracket임을 의미

##2번쨰 풀이 
#소스 : https://pacific-ocean.tistory.com/70
# import sys
# sys.stdin = open("input.txt")
# input = sys.stdin.readline

# T = int(input())
# M = [input().rstrip() for _ in range(T)]

# for i in M:
#     sum = 0
#     for j in i:
#         if j == "(":
#             sum += 1
#         elif j == ")":
#             sum -= 1
#         if sum < 0:
#             print("NO")
#             break
#     if sum > 0:
#         print("NO")
#     elif sum == 0:
#         print("YES")
