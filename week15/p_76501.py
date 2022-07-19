
absolutes=[4,7,12]
signs = [True,False,True]

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == 1:
            answer += int(absolutes[i])
        elif signs[i]== 0:
            answer -= int(absolutes[i])

    return answer

print (solution(absolutes, signs))