import heapq
g = [1,2,3]
s = [1,2]


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """ 

        count = 0
        heapq.heapify(g)

        while g or s: 
            person = heapq.heappop(g) 
            print(person)
            if person <= s[0]:
                count += 1
                s.pop(0)
                if not s:
                    return count
        return count

print(Solution().findContentChildren(g,s))