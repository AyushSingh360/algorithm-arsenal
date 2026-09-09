from collections import deque


class MyStack:

    def __init__(self):
        # single queue to simulate stack
        self.q = deque()

    def push(self, x: int) -> None:
        # add new element to the back
        self.q.append(x)
        # rotate: move all previous elements behind the new one
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # front of queue is the top of stack
        return self.q.popleft()

    def top(self) -> int:
        # peek front
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
