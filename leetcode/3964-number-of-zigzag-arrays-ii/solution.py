class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # Handle n = 1 separately: any value in [l, r] is valid
        if n == 1:
            return m % MOD

        # We will encode states as follows:
        # index 0..m-1: state (cur = x, next comparison must be DOWN), x in 0..m-1
        # index m..2m-1: state (cur = x, next comparison must be UP),   x in 0..m-1
        #
        # Transition:
        #   from state (down, x): we must pick y < x (strictly decreasing),
        #       so we go to (up, y) for all y in 0..x-1
        #   from state (up, x): we must pick y > x (strictly increasing),
        #       so we go to (down, y) for all y in x+1..m-1
        #
        # We'll build a 2m x 2m transition matrix T and use fast exponentiation.
        size = 2 * m

        # Build T as list of lists
        T = [[0] * size for _ in range(size)]

        # Helper to map (dir, x) to index; dir=0 -> down, dir=1 -> up
        def idx(dir_, x):
            return (dir_ * m) + x

        # Fill transitions
        # from (down, x) -> (up, y) for y < x
        for x in range(m):
            from_idx = idx(0, x)  # down, x
            for y in range(x):
                to_idx = idx(1, y)  # up, y
                T[to_idx][from_idx] = 1

        # from (up, x) -> (down, y) for y > x
        for x in range(m):
            from_idx = idx(1, x)  # up, x
            for y in range(x + 1, m):
                to_idx = idx(0, y)  # down, y
                T[to_idx][from_idx] = 1

        # Matrix multiplication (size x size) modulo MOD
        def mat_mul(A, B):
            # A, B are size x size
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                Ai = A[i]
                Ci = C[i]
                for k in range(size):
                    if Ai[k] == 0:
                        continue
                    aik = Ai[k]
                    Bk = B[k]
                    for j in range(size):
                        if Bk[j]:
                            Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
            return C

        # Matrix exponentiation: T^power
        def mat_pow(M, power):
            # Initialize result as identity
            R = [[0] * size for _ in range(size)]
            for i in range(size):
                R[i][i] = 1
            base = M
            p = power
            while p > 0:
                if p & 1:
                    R = mat_mul(base, R)
                base = mat_mul(base, base)
                p >>= 1
            return R

        # Initial vectors:
        # We count sequences where the first comparison is UP and where it is DOWN,
        # and use symmetry: answer = (count_up + count_down).
        #
        # For a fixed direction, the first element can be any x in [0, m-1],
        # and the next comparison direction is either up or down accordingly.
        #
        # It is enough (by symmetry) to compute one and multiply by 2.[page:1]

        # Let's construct initial vector v0 for "next comparison up":
        # v0[(up, x)] = 1 for all x, others 0
        v0 = [0] * size
        for x in range(m):
            v0[idx(1, x)] = 1  # up, x

        # We need sequences of length n.
        # We already fixed a starting value and direction; there will be n-1 transitions.
        T_pow = mat_pow(T, n - 1)

        # Multiply T^(n-1) * v0
        fn = [0] * size
        for i in range(size):
            s = 0
            Ti = T_pow[i]
            for j in range(size):
                if Ti[j] and v0[j]:
                    s = (s + Ti[j] * v0[j]) % MOD
            fn[i] = s

        # Sum over all states for this orientation
        subtotal = sum(fn) % MOD

        # By symmetry, we have same count for "next comparison down" start.[page:1]
        ans = (subtotal * 2) % MOD
        return ans
