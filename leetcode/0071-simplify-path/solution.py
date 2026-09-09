class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")

        for part in parts:
            # Skip empty strings, '.', and '//'
            if part == "" or part == ".":
                continue
            # Go to parent directory if '..' and we're not at root
            elif part == "..":
                if stack:
                    stack.pop()
            # Add valid directory/file name
            else:
                stack.append(part)

        # Join with '/' and add leading '/' for root
        return "/" + "/".join(stack)
