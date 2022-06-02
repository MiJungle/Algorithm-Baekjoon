#소스: https://bellog.tistory.com/146

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
    	# 예외 처리
        if not root:
            return ''

        queue = collections.deque([root])
        result = []

        # bfs 방식으로 왼쪽 노드 -> 오른쪽 노드 순으로 순회
        while queue:
            node = queue.popleft()

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')
        return ' '.join(result)

	# 역직렬화
    def deserialize(self, data):
    	# 예외 처리
        if len(data) == 0:
            return []

        data = data.split()
        for i, value in enumerate(data):
            data[i] = TreeNode(value)

        for i in range(1, len(data) + 1):
            # 왼쪽 자식 노드는 본인 인덱스 값 * 2
            if i * 2 <= len(data):
                data[i - 1].left = data[(i * 2) - 1]
            # 오른쪽 자식 노드는 본인 인덱스 값 * 2 + 1
            if i * 2 + 1 <= len(data):
                data[i - 1].right = data[(i * 2 + 1) - 1]

        return data[0]
