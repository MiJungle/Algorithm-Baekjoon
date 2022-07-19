participant= ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

from collections import defaultdict
def solution(participant, completion):
    
    m = defaultdict(int)
    for i in participant:
        m[i] += 1
    
    for j in completion:
        m[j]-= 1
    
    ans = []
    for j in m:
        if m[j] != 0:
            ans.append(j)
    return ",".join(ans)
print(solution(participant, completion))