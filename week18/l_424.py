
s = "ABAB"
k = 2

class Solution(object):
    def characterReplacement(self, s, k):
        m = dict()
        i = 0
        answer = 0
        for j in range(len(s)):
            m[s[j]] = m.get(s[j],0) +1
            maxlen = j-i+1 -max(m.values())
            while maxlen > k:
                m[s[i]] -= 1
                i += 1
                maxlen = j-i+1 -max(m.values())
            answer = max(answer, j-i+1)
        
        return(answer)
                
print(Solution().characterReplacement(s,k))