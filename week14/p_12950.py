def solution(arr1, arr2):
    k = []
    for i in range(len(arr1)):
        m = []
        for j in range(len(arr1[i])):
            m.append(arr1[i][j] + arr2[i][j])
        k.append(m)
    return k