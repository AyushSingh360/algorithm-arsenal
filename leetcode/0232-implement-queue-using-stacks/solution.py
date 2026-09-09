class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        # Always push to in_stack
        self.in_stack.append(x)

    def _move_if_needed(self) -> None:
        # Move elements to out_stack only when it's empty
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        # Ensure front is on top of out_stack
        self._move_if_needed()
        return self.out_stack.pop()

    def peek(self) -> int:
        # Ensure front is on top of out_stack
        self._move_if_needed()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
