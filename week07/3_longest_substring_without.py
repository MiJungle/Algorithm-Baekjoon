s = "abcabcbb"
#글자를 배열에 담는다, 중복글자가 감지되면, count 값을 len(배열)한다.
# 중복글자부터 다시 배열에 담는다
# 중복글자가 감지되면 count값을 확인하고 그게 이전 count값보다 크면 갱신해준다. 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = {}
        max_length = start = 0
        for index, num in enumerate(s):
            if num in ans and start <= ans[num]:
                start = ans[num] + 1
            else: 
                max_length = max(max_length, index-start+1)
            ans[num] = index
        return max_length