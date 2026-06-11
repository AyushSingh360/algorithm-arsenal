class Solution:
    def deserialize(self, s: str) -> 'NestedInteger':
        # If it's just a single number, return it directly
        if not s:
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        curr = None
        num = ''
        sign = 1

        for ch in s:
            if ch == '[':
                # start a new list
                if curr is not None:
                    stack.append(curr)
                curr = NestedInteger()
            elif ch == ']':
                # flush last number if there is one
                if num:
                    curr.add(NestedInteger(sign * int(num)))
                    num = ''
                    sign = 1
                # end current list and attach to parent if exists
                if stack:
                    parent = stack.pop()
                    parent.add(curr)
                    curr = parent
            elif ch == ',':
                # end of an element; flush number if present
                if num:
                    curr.add(NestedInteger(sign * int(num)))
                    num = ''
                    sign = 1
            elif ch == '-':
                sign = -1
            else:  # digit
                num += ch

        return curr
