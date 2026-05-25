class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # ans[i] = ans[i >> 1] + (i & 1)
            # i >> 1 is i // 2 (right shift removes LSB)
            # i & 1 is 1 if i is odd (LSB is 1), else 0
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans
