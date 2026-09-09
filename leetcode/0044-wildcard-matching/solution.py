class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_ptr = p_ptr = 0
        match = star_idx = -1

        while s_ptr < len(s):
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == "?"):
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < len(p) and p[p_ptr] == "*":
                star_idx = p_ptr
                match = s_ptr
                p_ptr += 1
            elif star_idx != -1:
                p_ptr = star_idx + 1
                match += 1
                s_ptr = match
            else:
                return False

        while p_ptr < len(p) and p[p_ptr] == "*":
            p_ptr += 1

        return p_ptr == len(p)
