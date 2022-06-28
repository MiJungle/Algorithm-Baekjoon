class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        val = [0,1,2]
        if n <3:
            return val[n]
        
        else:
            for i in range(3,n+1):
                val.append(val[i-1]+val[i-2])
        return val[n]

# Runtime: 27 ms, faster than 38.78% of Python online submissions for Climbing Stairs.
# Memory Usage: 13.6 MB, less than 12.27% of Python online submissions for Climbing Stairs.