from typing import List


class Solution:
    def resultArray(
        self, nums: List[int], k: int, queries: List[List[int]]
    ) -> List[int]:
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1

        # Each node: [product_mod_k, count_of_prefixes_with_remainder_0, ...]
        tree = [[1] + [0] * k for _ in range(size * 2)]

        def merge(left: List[int], right: List[int]) -> List[int]:
            # Concatenation: segment_left followed by segment_right.
            res = [0] * (k + 1)
            left_product = left[0]
            res[0] = (left_product * right[0]) % k

            # Prefixes that end inside left.
            for rem in range(k):
                res[rem + 1] = left[rem + 1]

            # Prefixes that consume all of left, then extend into right.
            for rem in range(k):
                res[(left_product * rem) % k + 1] += right[rem + 1]

            return res

        def set_value(index: int, value: int) -> None:
            pos = size + index
            value %= k

            node = [0] * (k + 1)
            node[0] = value
            node[value + 1] = 1
            tree[pos] = node

            pos >>= 1
            while pos:
                tree[pos] = merge(tree[pos << 1], tree[pos << 1 | 1])
                pos >>= 1

        # Identity node: empty segment, product 1, no non-empty prefixes.
        identity = [1] + [0] * k

        def range_query(left: int, right: int) -> List[int]:
            """Returns aggregate for nums[left : right + 1]."""
            left += size
            right += size

            acc_left = identity
            acc_right = identity

            while left <= right:
                if left & 1:
                    acc_left = merge(acc_left, tree[left])
                    left += 1
                if not (right & 1):
                    acc_right = merge(tree[right], acc_right)
                    right -= 1

                left >>= 1
                right >>= 1

            return merge(acc_left, acc_right)

        for i, value in enumerate(nums):
            set_value(i, value)

        answer = []
        for index, value, start, x in queries:
            set_value(index, value)
            node = range_query(start, n - 1)
            answer.append(node[x + 1])

        return answer
