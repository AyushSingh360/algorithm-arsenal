class MinStack:

    def __init__(self):
        # Each element: [value, current_min_at_this_point]
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            # If stack is empty, val is the current minimum
            self.stack.append([val, val])
        else:
            current_min = self.stack[-1][1]
            self.stack.append([val, min(val, current_min)])

    def pop(self) -> None:
        # Per constraints, pop is only called on non-empty stacks
        self.stack.pop()

    def top(self) -> int:
        # Return just the value part
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the current minimum stored with the top element
        return self.stack[-1][1]
