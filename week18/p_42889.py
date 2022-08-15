N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	

def solution(N, stages):
    answer = []

  



print(solution(N,stages))
        



# def solution(N, stages):
#     answer = []
#     failure = [0]*(N+1)
#     for i in range(1,N+1):
#         for j in range(len(stages)):
#             if stages[j] >= i:
#                 failure[i] += 1
#     for i in range(1,N+1):
#         try: 
#             answer.append([stages.count(i)/failure[i],i])

#         except:
#             answer.append([0,i])
       
#     fin = sorted(answer, key = lambda x: -x[0] )
#     real_fin = [x[1] for x in fin]
#     return(real_fin)