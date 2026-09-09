class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        first_true = -1  # first index where citations[i] >= n - i

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                first_true = mid
                right = mid - 1  # try to find an earlier index
            else:
                left = mid + 1  # need more cited papers, move right

        return 0 if first_true == -1 else n - first_true
