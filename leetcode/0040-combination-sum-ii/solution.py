class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(list(path))
                return
            if total > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue  # skip duplicates
                path.append(candidates[i])
                backtrack(
                    i + 1, path, total + candidates[i]
                )  # move to next index (no reuse)
                path.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return result
