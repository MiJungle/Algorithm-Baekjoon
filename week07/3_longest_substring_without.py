s = "abcabcbb"
#글자를 배열에 담는다, 중복글자가 감지되면, count 값을 len(배열)한다.
# 중복글자부터 다시 배열에 담는다
# 중복글자가 감지되면 count값을 확인하고 그게 이전 count값보다 크면 갱신해준다. 

ans = [s[0]]
print(ans)
count = 0
right = 0
for i in s:
    while right != len(ans)-1
    if i != ans[right]:
        ans.append(i) 
        
    else:
        k = len(ans)
        ans = []
        if k > count:
            k = count
    right += 1
      
print(ans)
print(count)

