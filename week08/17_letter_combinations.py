# 소스:https://velog.io/@ahn16/Leetcode-17-m9qafcsk

li = [[0],[0],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"]]
digits = "23"

class Solution(object):
    def letterCombinations(self, digits):
        # Lookup table for number to character
        dic = {"2":"abc" , "3":"def", "4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv", "9":"wxyz"}

        # Implement DFS
        def dfs(index,path):
            if len(path) == len(digits):
                result.append(path)
                return
            for i in range(index,len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1,path+j)


        # Exception handling
        if not digits:
            return []
        # Run dfs
        result = []
        dfs(0,"")
        return result