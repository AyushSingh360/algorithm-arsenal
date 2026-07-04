from typing import Optional, List


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            vals.append(str(node.val))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nums = list(map(int, data.split(",")))
        n = len(nums)
        idx = 0

        def build(lower, upper):
            nonlocal idx
            if idx >= n:
                return None
            val = nums[idx]
            if val < lower or val > upper:
                return None
            idx += 1
            node = TreeNode(val)
            node.left = build(lower, val - 1 if isinstance(val, int) else val)
            node.right = build(val + 1 if isinstance(val, int) else val, upper)
            return node

        return build(-(10**9), 10**9)
