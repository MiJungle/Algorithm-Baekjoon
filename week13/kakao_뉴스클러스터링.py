import math
str1 = "FRANCE"
str2 = "french"


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    st1 = []
    for i in range(0, len(str1)-1):
        k = str1[i:i+2]
        if k[0].isalpha()== 0 or k[1].isalpha()==0:
            continue
        else:
            st1.append(k)
    st2 = []
    for i in range(0, len(str2)-1):
        k = str2[i:i+2]
        if k[0].isalpha()== 0 or k[1].isalpha()==0:
            continue
        else:
            st2.append(k)
    ans = []
    for i in st1:
        for j in st2:
            if i == j:
                ans.append(i)
    fin = []
    ans = set(ans) #공통원소 들어가있음

    for i in ans:
        fin.append(max(st1.count(i), st2.count(i)))
        fin.append(min(st1.count(i), st2.count(i)))
    kyo = fin[0] 
    hp = fin[1]

    for i in ans:
        st1.remove(i)
        st2.remove(i)
    mm = len(st1) + len(st2) + kyo 
    done = (hp/mm) * 65536
    return math.trunc(done)

print(solution(str1,str2))