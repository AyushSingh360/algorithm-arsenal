class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        if rows == 0 or n == 0:
            return ""

        cols = n // rows
        res = []

        # Start from each column in the first row
        for start_col in range(cols):
            r, c = 0, start_col
            # Go down-right diagonally
            while r < rows and c < cols:
                idx = r * cols + c
                res.append(encodedText[idx])
                r += 1
                c += 1

        # Remove trailing spaces (originalText has no trailing spaces)
        return "".join(res).rstrip()
