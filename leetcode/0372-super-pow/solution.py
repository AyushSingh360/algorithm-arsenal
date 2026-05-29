from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        a %= MOD
        result = 1

        for digit in b:
            # result = (result^10 * a^digit) % MOD
            result = (pow(result, 10, MOD) * pow(a, digit, MOD)) % MOD

        return result
        
