from typing import List


class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.perimeter = 2 * (width + height) - 4
        self.offset = 0
        self.moved = False

    def step(self, num: int) -> None:
        if num == 0:
            return

        self.offset = (self.offset + num) % self.perimeter
        self.moved = True

    def getPos(self) -> List[int]:
        east = self.width - 1
        north = east + self.height - 1
        west = north + self.width - 1

        if self.offset <= east:
            return [self.offset, 0]
        if self.offset <= north:
            return [self.width - 1, self.offset - east]
        if self.offset <= west:
            return [self.width - 1 - (self.offset - north), self.height - 1]
        return [0, self.height - 1 - (self.offset - west)]

    def getDir(self) -> str:
        if self.offset == 0:
            return "South" if self.moved else "East"

        east = self.width - 1
        north = east + self.height - 1
        west = north + self.width - 1

        if self.offset <= east:
            return "East"
        if self.offset <= north:
            return "North"
        if self.offset <= west:
            return "West"
        return "South"
