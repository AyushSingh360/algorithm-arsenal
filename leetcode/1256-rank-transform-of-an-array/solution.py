from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Get sorted unique values
        sorted_unique = sorted(set(arr))  # smallest → largest[web:7]

        # Map each value to its rank (starting at 1)
        rank = {
            num: i + 1 for i, num in enumerate(sorted_unique)
        }  # num -> rank.[web:7]

        # Replace each element in arr with its rank
        return [
            rank[num] for num in arr
        ]  # O(n) lookup with the dictionary.[web:7][web:6]
