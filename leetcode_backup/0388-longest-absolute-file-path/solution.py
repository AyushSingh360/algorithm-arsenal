class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Stack holds cumulative length up to each depth
        # stack[depth] = total length of path up to that depth (including '/')
        stack = [0]  # depth -1 has length 0
        ans = 0

        for token in input.split("\n"):
            # depth is number of leading '\t'
            depth = token.count("\t")
            name = token.replace("\t", "")

            # Ensure stack has correct depth (parent at index depth)
            # If we moved up, pop until current depth fits
            while len(stack) > depth + 1:
                stack.pop()

            if "." in name:  # it's a file
                # length = parent length + len(file name)
                curr_len = stack[-1] + len(name)
                ans = max(ans, curr_len)
            else:
                # it's a directory: push length including trailing '/'
                # parent length + len(dir) + 1 for '/'
                stack.append(stack[-1] + len(name) + 1)

        return ans
