import math
str1 = "E=M*C^2"
str2 = "e=m*c^2"


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

    if not st1 and not st2:
        return 65536
    ans =[]
    for i in st1:
        if i in st2:
            ans.append(i)

    
    nosame = set(ans) #공통원소 들어가있음
    count_min = []
    count_max = []
    for i in nosame:
        count_max.append(max(st1.count(i), st2.count(i)))
        count_min.append(min(st1.count(i), st2.count(i)))

    count_st1 = 0
    count_st2 = 0
    for i in nosame:
        count_st1 += st1.count(i)
        count_st2 += st2.count(i)


    len_st1 = len(st1) - count_st1
    len_st2 = len(st2) - count_st2
    together = len_st1 + len_st2 + sum(count_max)
    common = sum(count_min)


    done = (common/together) * 65536
    
    return math.trunc(done)

print(solution(str1,str2))


