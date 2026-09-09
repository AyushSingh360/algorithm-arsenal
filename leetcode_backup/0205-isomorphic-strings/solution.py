class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for cs, ct in zip(s, t):
            # If s -> t mapping exists, it must match ct
            if cs in s_to_t and s_to_t[cs] != ct:
                return False

            # If t -> s mapping exists, it must match cs
            if ct in t_to_s and t_to_s[ct] != cs:
                return False

            # Set/update mappings
            s_to_t[cs] = ct
            t_to_s[ct] = cs

        return True
