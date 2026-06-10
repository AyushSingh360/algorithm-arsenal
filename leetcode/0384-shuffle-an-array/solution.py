import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        # Store the original array for reset
        self.original = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original[:]

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        arr = self.original[:]  # create a copy to shuffle
        n = len(arr)

        # Fisher-Yates shuffle
        for i in range(n - 1):
            j = random.randint(i, n - 1)
            arr[i], arr[j] = arr[j], arr[i]

        return arr
