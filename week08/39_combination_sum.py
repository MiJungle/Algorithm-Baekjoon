#첫번쨰 원소 넣고 target에서 뺀다음, 그 뺀만큼의 숫자가 있는지 for문 돌리면서 확인
candidates = [2,3,6,7]
target = 7

ans = []
fin = []
def dfs(candidates, target):
    for i in candidates:
        ans.append(i)
        target2 = target-i
        if target2 !=0:
            for i in candidates:
                ans.append(i)
                dfs(candidates, target2)
    fin.append(ans)
    return fin

print(dfs(candidates, target))