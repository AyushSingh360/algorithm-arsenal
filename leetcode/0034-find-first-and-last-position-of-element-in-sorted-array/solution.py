class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    if isFirst:
                        right = mid - 1  # Move left
                    else:
                        left = mid + 1  # Move right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        first = findBound(True)
        last = findBound(False)
        return [first, last]
