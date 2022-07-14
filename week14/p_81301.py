def solution(s):
    word = {"zero" : 0,"one" : 1,"two" : 2,"three" : 3,
    "four" : 4,"five" : 5,"six" : 6,
    "seven" : 7,"eight" : 8,"nine" : 9}
    answer = s
    for key, value in word.items():
        answer = answer.replace(key, str(value) )
    return (int(answer))
    

# s="one4seveneight"
# def solution(s):
    
#     changetonum = [[0,"zero"],[1,"one"],[2,"two"],[3,"three"],[4,"four"],[5,"five"],[6,"six"],[7,"seven"],[8,"eight"],[9,"nine"]]
#     ans = []


#     while s:
#         m = s.pop(0)
#         if m.isalpha == False:
#             ans.append(m)
#         else:

#             if i.isalpha == False:
#             ans.append(s.pop(0))
#         else:
#             alpha = []
#             while i.isalpha == True:
#                 alpha.append(s.pop(0))
#             print(alpha)
#             k = "".join(alpha)
#             print(alpha)
#             for j in changetonum:
#                 if k == j[1]:
#                     ans.append(j[0])

#     print(ans)
# print(solution(s))