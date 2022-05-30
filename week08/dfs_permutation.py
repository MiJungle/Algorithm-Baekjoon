# def DFS(L):
#     if L == r:
#         print(result)
#     else: 
#         for i in range(len(arr)):
#             if checklist[i] == 0:
#                 result[L] = arr[i]
#                 checklist[i] = 1
#                 DFS(L+1)
#                 checklist[i] = 0

# arr = [1,2,3]
# r = 2
# result = [0] *r
# checklist = [0] *len(arr)
# DFS(0)


#combination 

def DFS(L, BeginWith):
    if L == r:
        print(result)
    else:
        for i in range(BeginWith, len(n)):
            result[L] = [i]
            DFS(L+1, i+1)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

n = [1,2,3]
r = 2

result = [0]* r

DFS(0, 0) #(0level, 0 beginwith)