class Solution:
    def decodeString(self, s: str) -> str:
        stack = []          # will store pairs (prev_str, repeat_count)
        curr_str = ""
        curr_num = 0

        for c in s:
            if c.isdigit():
                # build multi-digit number, e.g. "12[ab]"
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                # push current context, reset for substring inside brackets
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif c == ']':
                # pop previous context and expand
                prev_str, num = stack.pop()
                curr_str = prev_str + num * curr_str
            else:
                # plain character, append to current string
                curr_str += c

        return curr_str
