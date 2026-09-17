class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float("inf")

        # best[i] = shortest valid subarray fully contained in arr[0:i+1]
        best = [INF] * n

        left = 0
        curr_sum = 0
        shortest_so_far = INF
        answer = INF

        for right, value in enumerate(arr):
            curr_sum += value

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # A previously completed valid subarray ends before `left`,
                # so it cannot overlap with the current [left, right].
                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, best[left - 1] + length)

                shortest_so_far = min(shortest_so_far, length)

            best[right] = shortest_so_far

        return -1 if answer == INF else answer
