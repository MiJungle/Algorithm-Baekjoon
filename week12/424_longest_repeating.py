# 참고: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/discuss/1827576/python-easy-to-read-and-understand-leetcode-424

class Solution(object):
    def characterReplacement(self, s, k):
        d = {}
        ans, i = 0, 0
        for j in range(len(s)):
            d[s[j]] = d.get(s[j], 0) + 1 #s[j] 값이 없을 때 0을 넣겠다.
            cnt = (j - i + 1) - max(d.values()) #j-i+1 지금까지 dic에 넣은 숫자에 dic멕스를 빼면 바꿔야하는 글자수
            while cnt > k: #바꾸는 글자수가 k보다 크게 되면
                d[s[i]] -= 1 #그 i값에 해당하는 글자를 dict 에서 뺌
                i = i + 1 #i pointer를 옮기면서 갱신
                cnt = (j - i + 1) - max(d.values()) # cnt 는 계속 바꿔야하는 글자수를 저장하고 있고
            ans = max(ans, j - i + 1) # ans는 최대값을 계속 비교하면서 갖고 잇음
        return ans #반복문이 끝난 경우, 최대 글자값을 담고 있음 

s = "AABABBA"
k = 2
print(Solution().characterReplacement(s,k))