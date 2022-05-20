# class Solution(object):
#     def numJewelsInStones(self, jewels, stones):
#         count = 0
#         for i in jewels:
#             for j in stones:
#                 if i == j:
#                     count+=1
#         return count
# import collections
# class Solution(object):
#      def numJewelsInStones(self, jewels, stones):

#          freqs = collections.Counter(s)
#          count = 0
#          return freqs

class Solution(object):
     def numJewelsInStones(self, jewels, stones):
         return sum(s in jewels for s in stones)

j="aA"
s= "aAAbbbb"
print(Solution().numJewelsInStones(j,s))