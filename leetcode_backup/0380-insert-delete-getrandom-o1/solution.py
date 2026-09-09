import random


class RandomizedSet(object):

    def __init__(self):
        self.arr = []  # store values
        self.pos = {}  # val -> index in arr

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last_val = self.arr[-1]

        # move last element into idx
        self.arr[idx] = last_val
        self.pos[last_val] = idx

        # remove last
        self.arr.pop()
        del self.pos[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.arr)
