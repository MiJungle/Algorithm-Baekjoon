#재귀탐색해서 value 값이 low 이상 high 이하 일때 다 더함
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    val = 0
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not node:
            return -1
        
        
        if node< low:
            rangeSumBST(node.right)
        
        if node > high:
            rangeSumBST(node.left)
            