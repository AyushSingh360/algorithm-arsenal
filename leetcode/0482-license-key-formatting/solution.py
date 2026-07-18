class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Step 1: remove dashes and convert to uppercase
        cleaned = ''.join(ch.upper() for ch in s if ch != '-')
        if not cleaned:
            return ""

        # Step 2: build result from right to left
        result = []
        count = 0

        for ch in reversed(cleaned):
            result.append(ch)
            count += 1
            if count == k:
                result.append('-')
                count = 0

        # Step 3: if the last character is '-', remove it, then reverse
        if result and result[-1] == '-':
            result.pop()

        return ''.join(reversed(result))
