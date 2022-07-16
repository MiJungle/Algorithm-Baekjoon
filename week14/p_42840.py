def solution(answers):
    submission = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    
    numq = len(answers)
    ans = [0,0,0]

    for i in range(numq):
        if answers[i] == submission[0][i%len(submission[0])]:
            ans[0] +=1
        if answers[i] == submission[1][i%len(submission[1])]:
            ans[1] +=1
        if answers[i] == submission[2][i%len(submission[2])]:
            ans[2] +=1
    m = ans.count(max(ans))
    
    if m == 1:
        return [ans.index(max(ans))+1]
    else:
        dd = []
        for i in range(len(ans)):
            if ans[i] == max(ans):
                dd.append(i+1)
        dd.sort()
        return dd
