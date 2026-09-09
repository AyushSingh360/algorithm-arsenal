from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node: Optional[TreeNode], path: str) -> None:
            if not node:
                return

            # Extend path with current node
            if path:
                path += "->" + str(node.val)
            else:
                path = str(node.val)

            # If leaf, record the path
            if not node.left and not node.right:
                res.append(path)
                return

            # Continue DFS
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return res
