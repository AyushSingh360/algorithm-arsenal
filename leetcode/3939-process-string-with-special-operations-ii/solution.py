class Solution:
    def processStr(self, s: str, k: int) -> str:
        # 1) Forward pass: compute final length L only
        L = 0
        for ch in s:
            if ch == '*':
                if L > 0:
                    L -= 1
            elif ch == '#':
                L *= 2
            elif ch == '%':
                # reverse does not change length
                continue
            else:
                # letter
                L += 1
            if L > 10**15:
                # Problem guarantees final length ≤ 1e15, but be safe
                L = 10**15 + 1

        if k >= L:
            return '.'

        # 2) Backward pass: undo operations, remap k
        # We treat indices as 0-based: result[0..L-1]
        for ch in reversed(s):
            if ch == '*':
                # Forward: if L>0, L-- (removed last char)
                # Backward: if a char was removed at end, then previous length was L+1
                # Our current k is in range [0, L-1]; that same index existed before removal.
                # So k unchanged, just restore length.
                if L > 0:
                    L += 1

            elif ch == '#':
                # Forward: result = result + result, so L_new = 2 * L_old
                # Backward: we know current length is L, so previous length was L // 2.
                half = L // 2
                if k >= half:
                    # k was in the second copy; map it to first copy
                    k -= half
                L = half

            elif ch == '%':
                # Forward: reverse result, length unchanged.
                # Backward: undo reverse by reversing index:
                # pos i becomes L-1-i, so inverse mapping is same formula.
                k = L - 1 - k

            else:
                # Letter
                # Forward: appended this letter, increasing length by 1.
                # So previous length was L-1, and this letter sits at index L-1.
                if L == 0:
                    continue  # no effect
                if k == L - 1:
                    return ch
                # Otherwise k was in the previous part.
                L -= 1

        return '.'
