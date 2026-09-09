class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for ch in str(num):  # iterate over each character of the number
                ans.append(int(ch))  # convert back to int and append
        return ans
