class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        # Convert to list for easier manipulation
        s = list(s)

        # Continue while s is not "1"
        while len(s) > 1 or s[0] != "1":
            if s[-1] == "0":  # Even number - divide by 2 (remove last 0)
                s.pop()
                steps += 1
            else:  # Odd number - add 1
                # Add 1 to binary string
                i = len(s) - 1
                while i >= 0 and s[i] == "1":
                    s[i] = "0"
                    i -= 1

                if i >= 0:
                    s[i] = "1"
                else:
                    s.insert(0, "1")

                steps += 1

        return steps
