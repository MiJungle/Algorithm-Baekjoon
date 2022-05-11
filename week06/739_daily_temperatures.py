
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        answer = [0]*len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] =i- last
            stack.append(i)
        return answer


##시간초과
# right = 0
# left = right +1
# ans = []
# while right != len(temperatures):
#     while left != len(temperatures):
#         if temperatures[right] < temperatures[left]:
#             ans.append(left-right)
#             right +=1
#             left = right +1
#         else:
#             left += 1
#     ans.append(0)
#     right += 1
#     left = right+1
# print(ans)
