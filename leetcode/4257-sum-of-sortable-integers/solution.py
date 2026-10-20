class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        pref_max = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref_max[i + 1] = max(pref_max[i], x)

        suff_min = [10**9] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        # descents before index i
        pref_drop = [0] * n
        for i in range(1, n):
            pref_drop[i] = pref_drop[i - 1] + (nums[i - 1] > nums[i])

        def can_sort_block(start: int, k: int) -> bool:
            end = start + k - 1

            # descents inside the block
            drops = pref_drop[end] - pref_drop[start]

            # wrap-around descent
            if nums[end] > nums[start]:
                drops += 1

            # block must be a cyclic rotation of its sorted version
            if drops > 1:
                return False

            # all elements before this block must be <= all elements from here on
            if pref_max[start] > suff_min[start]:
                return False

            return True

        def sortable(k: int) -> bool:
            return all(can_sort_block(start, k) for start in range(0, n, k))

        ans = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                if sortable(i):
                    ans += i

                j = n // i
                if i != j and sortable(j):
                    ans += j

            i += 1

        return ans
