import heapq
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

n = 5

def solution(n, arr1, arr2):
    ar1 = []
    for i in arr1:
        n = format(i, 'b')
        ar1.append(n)

    ar2 = []
    for i in arr2:
        m = format(i, 'b')
        ar2.append(m)
    ans = []
    
    for i in range(len(ar2)):
        ans.append(str(int(ar1[i])+int(ar2[i])))

    for i in ans:
        print("\"", end='')
        for j in i:
            if int(j) >= 1:
                print("#",end='')
            else:
                print(" ", end="")
        print("\",",end='')        
    
print(solution(5,arr1,arr2))