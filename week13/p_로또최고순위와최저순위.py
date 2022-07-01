lottos= [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]	

def solution(lottos, win_nums):

    m = lottos.count(0)

    k = set(win_nums) -set(lottos) 
    ans = len(k)
    highest = 6- ans + m
    lowest = 6-ans 
    fin = []
    if highest == 6:
        fin.append(1)
    elif highest == 5:
        fin.append(2) 
    elif highest == 4:
        fin.append(3) 
    elif highest == 3:
        fin.append(4) 
    elif highest == 2:
        fin.append(5) 
    else:
        fin.append(6) 

    if lowest == 6:
        fin.append(1)
    elif lowest == 5:
        fin.append(2) 
    elif lowest == 4:
        fin.append(3) 
    elif lowest == 3:
        fin.append(4) 
    elif lowest == 2:
        fin.append(5) 
    else:
        fin.append(6) 
    return fin
print(solution(lottos, win_nums))