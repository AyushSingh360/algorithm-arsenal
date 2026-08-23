class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2

        left_sum = right_sum = 0
        left_q = right_q = 0

        for i, ch in enumerate(num):
            if ch == '?':
                if i < n:
                    left_q += 1
                else:
                    right_q += 1
            else:
                if i < n:
                    left_sum += int(ch)
                else:
                    right_sum += int(ch)

        
        if (left_q + right_q) % 2 == 1:
            return True

        
        return left_sum - right_sum != (right_q - left_q) * 9 // 2
