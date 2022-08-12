gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	


def solution(gems):
    answer = [2e9]
    left = 0
    right = 1
    jewel = set(gems)
    num = len(jewel)
    arr = dict()
    arr[gems[0]] = 1
    while left < right:
        if len(arr) < num:
            if right >= len(gems):
                break
            else:
                arr[gems[right]] = arr.get(gems[right],0) +1 
            right += 1
        else:
            answer = min(answer,[right-left+1, left, right])
            arr[gems[left]] -= 1
            if arr[gems[left]] == 0:
                del arr[gems[left]]
            left += 1
            
    return [answer[1]+1, answer[2]]



print(solution(gems))   







def solution(gems):
    answer = [2e9]
    arr = dict()
    # right 이 len(gems) 가 되면서, len(arr)는 3인 경우가 존재, 즉 len(arr)가 4가 아님에도 break함
    #right 이 len(gems) 5가 되면서, len(arr)는 4가 되어버리니까, answer은 갱신됨
    arr[gems[0]] = 1 
    jewel = set(gems)
    num = len(jewel)
    left = 0
    right = 1
    while left < right:
        if len(arr) < num:
            if right >= len(gems):
                break
            else: 
                arr[gems[right]] = arr.get(gems[right],0) + 1
            right += 1
        elif len(arr) >= num:
            answer= (min(answer, [right-left+1, left, right]))
            arr[gems[left]]-= 1
            if arr[gems[left]] == 0:
                del arr[gems[left]]
            left += 1
    
    return [answer[1]+1, answer[2]]
            