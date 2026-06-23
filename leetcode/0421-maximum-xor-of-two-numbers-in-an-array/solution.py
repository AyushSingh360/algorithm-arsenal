class TrieNode:
    def __init__(self):
        self.child = [None, None]


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()

        def insert(x: int) -> None:
            node = root
            for i in range(31, -1, -1):
                b = (x >> i) & 1
                if not node.child[b]:
                    node.child[b] = TrieNode()
                node = node.child[b]

        def query(x: int) -> int:
            node = root
            ans = 0
            for i in range(31, -1, -1):
                b = (x >> i) & 1
                want = 1 - b
                if node.child[want]:
                    ans = (ans << 1) | 1
                    node = node.child[want]
                else:
                    ans = ans << 1
                    node = node.child[b]
            return ans

        for num in nums:
            insert(num)

        best = 0
        for num in nums:
            best = max(best, query(num))

        return best
