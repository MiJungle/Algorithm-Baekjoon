#첫번쨰 원소 넣고 target에서 뺀다음, 그 뺀만큼의 숫자가 있는지 for문 돌리면서 확인
candidates = [2,3,6,7]
target = 7

ans = []
fin = []
def dfs(candidates, target):
    if target < 0:
        return 
    for i in candidates:
        fin.append(i)
        target = target-i
        if target !=0:
            dfs(candidates, target)
    ans.append(fin)
    return ans

print(dfs(candidates, target))