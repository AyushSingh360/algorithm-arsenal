from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Step 1: sort the array
        arr.sort()  # [web:3][web:4][web:6]

        # Step 2: first element must become 1
        arr[0] = 1  # [web:6]

        # Step 3: greedily cap each element so that
        # arr[i] <= arr[i-1] + 1, while keeping it as large as possible
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)  # [web:3][web:4][web:6]

        # Step 4: last element is the maximum
        return arr[-1]  # [web:3][web:4][web:6]
