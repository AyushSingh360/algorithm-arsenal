from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        # good[i] == True means strs[i] < strs[i+1] already fixed
        good = [False] * (n - 1)
        ans = 0
        
        for c in range(m):
            # Check if this column creates any inversion for unresolved pairs
            bad = False
            for i in range(n - 1):
                if not good[i] and strs[i][c] > strs[i + 1][c]:
                    bad = True
                    break
            
            if bad:
                # Must delete this column
                ans += 1
                continue
            
            # Safe to keep this column; update good[] for newly resolved pairs
            for i in range(n - 1):
                if not good[i] and strs[i][c] < strs[i + 1][c]:
                    good[i] = True
        
        return ans
