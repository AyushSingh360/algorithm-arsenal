class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == "1":
            return False

        reachable = [False] * n
        reachable[0] = True
        prefix = 0

        for i in range(1, n):
            left = i - maxJump
            right = i - minJump

            if right >= 0:
                if reachable[right]:
                    prefix += 1

                if left - 1 >= 0 and reachable[left - 1]:
                    prefix -= 1

                if s[i] == "0" and prefix > 0:
                    reachable[i] = True

        return reachable[-1]
