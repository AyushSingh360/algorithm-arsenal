class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Stack will store NestedInteger objects in reverse order
        # so we can pop from the end (acting as a stack)
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        # hasNext() ensures the top is an integer
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        # Flatten until we find an integer or stack is empty
        while self.stack and not self.stack[-1].isInteger():
            # Pop the list and push its elements in reverse order
            nested_list = self.stack.pop().getList()
            self.stack.extend(nested_list[::-1])
        
        # True if stack top is an integer
        return bool(self.stack)
