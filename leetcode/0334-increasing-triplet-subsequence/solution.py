class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num          # smallest value so far
            elif num <= second:
                second = num         # smallest value > first, with a first before it
            else:
                return True          # num > second, so first < second < num
        
        return False
