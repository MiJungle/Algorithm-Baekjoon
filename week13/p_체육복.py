def solution(n, lost, reserve):
    
    n_lost = set(lost) - set(reserve)
    n_reserve = set(reserve) - set(lost)

    for i in n_reserve:
        if i-1 in n_lost:
            n_lost.remove(i-1)
        elif i+ 1 in n_lost:
            n_lost.remove(i+1)

    return n - len(n_lost)

#초기 풀이: pop을 쓰게 돼서 index 오류가 너무 많이 나옴. whil룹을 했을 때는 또 while이 끝나지 않은 문제가 발생 
# def solution(n, lost, reserve):

#     count = 0
#     reserve.sort()
#     for i in range(len(lost)):
#         try:
#             if lost[i] in reserve:
#                 reserve.pop(i)
#                 lost.pop(i)
#         except:
#             pass

#     k = n - len(lost) 
#     while reserve and count!=len(lost):
#         num = reserve.pop()
#         try:
#             if (num -1 in lost) or (num+1 in lost):
#                 count += 1
#         except:
#             pass

#     return count + k 
