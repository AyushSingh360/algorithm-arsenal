from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def is_valid(seg: str) -> bool:
            # No leading zeros unless segment is exactly "0"
            if len(seg) > 1 and seg[0] == "0":
                return False
            # Value must be in [0, 255]
            return 0 <= int(seg) <= 255

        def backtrack(start: int, parts: List[str]) -> None:
            # If we have 4 parts and used all characters, record answer
            if len(parts) == 4:
                if start == n:
                    res.append(".".join(parts))
                return

            # Prune: remaining chars must fit into remaining segments (1–3 each)
            remaining_parts = 4 - len(parts)
            remaining_chars = n - start
            if (
                remaining_chars < remaining_parts
                or remaining_chars > 3 * remaining_parts
            ):
                return

            # Try segment lengths 1 to 3
            for length in range(1, 4):
                if start + length > n:
                    break
                seg = s[start : start + length]
                if is_valid(seg):
                    parts.append(seg)
                    backtrack(start + length, parts)
                    parts.pop()

        backtrack(0, [])
        return res
