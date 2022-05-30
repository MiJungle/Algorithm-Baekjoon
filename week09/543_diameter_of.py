class Solution(object):
    longest = 0 #longetst 초기값 - 계속 갱신해나갈 예정
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left) #왼쪽 리프 노드까지 탐색
            right = dfs(node.right) #오른쪽 리프 노드까지 탐색 
            
            self.longest= max(self.longest, left+right+2) #left꺼 1개 더하고 right꺼 1개 더하고
            return max(left, right) +1 #올리면서 1개를 더함
        
        dfs(root)
        return self.longest