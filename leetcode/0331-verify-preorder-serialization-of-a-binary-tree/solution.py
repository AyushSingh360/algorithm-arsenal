class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1  # one slot for the root
        
        for node in preorder.split(','):
            slots -= 1  # every node consumes one slot
            if slots < 0:
                return False  # more nodes than available slots
            
            if node != '#':
                slots += 2  # non-null node provides two child slots
        
        return slots == 0  # all slots must be exactly filled
