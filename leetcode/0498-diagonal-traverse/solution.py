class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        
        # There are m + n - 1 diagonals, each identified by k = i + j
        for k in range(m + n - 1):
            temp = []
            
            # Start indices for this diagonal
            i = 0 if k < n else k - n + 1
            j = k if k < n else n - 1
            
            # Collect all elements on this diagonal going down-left
            while i < m and j >= 0:
                temp.append(mat[i][j])
                i += 1
                j -= 1
            
            # Reverse on even k to get the zig-zag order
            if k % 2 == 0:
                temp.reverse()
            
            res.extend(temp)
        
        return res
