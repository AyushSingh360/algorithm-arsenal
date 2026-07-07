class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Step 1: collect non-zero digits in order as a string
        x_str = ''.join(ch for ch in str(n) if ch != '0')
        
        # Step 2: if there are no non-zero digits, x = 0 and answer is 0
        if not x_str:
            return 0
        
        # Step 3: convert to integer x
        x = int(x_str)
        
        # Step 4: compute sum of digits of x
        digit_sum = sum(int(ch) for ch in x_str)
        
        # Step 5: return x * digit_sum
        return x * digit_sum
