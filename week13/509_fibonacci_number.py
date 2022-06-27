class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        val = [0,1,1]
        
        if n < 3:
            return val[n]
        
        else:
            for i in range(3, n+1):
                val.append(val[i-1] + val[i-2])
                
            return val[i]