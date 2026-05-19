class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        # Add two non-negative integers represented as decimal strings
        def add_str(a: str, b: str) -> str:
            i, j = len(a) - 1, len(b) - 1
            carry = 0
            res = []

            while i >= 0 or j >= 0 or carry:
                da = ord(a[i]) - ord('0') if i >= 0 else 0
                db = ord(b[j]) - ord('0') if j >= 0 else 0
                s = da + db + carry
                res.append(chr(s % 10 + ord('0')))
                carry = s // 10
                i -= 1
                j -= 1

            return ''.join(reversed(res))

        # Try all possible first and second numbers
        for i in range(1, n):          # num[0:i] is first
            first = num[0:i]
            # leading zero check for first
            if len(first) > 1 and first[0] == '0':
                break

            for j in range(i + 1, n):  # num[i:j] is second
                second = num[i:j]
                # leading zero check for second
                if len(second) > 1 and second[0] == '0':
                    break

                a, b = first, second
                k = j

                # build the sequence and see if it matches the whole string
                while k < n:
                    c = add_str(a, b)
                    # next piece in num must be exactly c
                    if not num.startswith(c, k):
                        break
                    k += len(c)
                    a, b = b, c

                # valid additive sequence uses all digits and has at least 3 numbers
                if k == n:
                    # There are at least 3 numbers because we fixed first and second
                    return True

        return False
