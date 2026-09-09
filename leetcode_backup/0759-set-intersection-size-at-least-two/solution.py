class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end asc; if same end, by start desc
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # last2 < last are the two largest points chosen so far
        last2 = -1
        last = -1
        res = 0

        for s, e in intervals:
            if s <= last2:
                # interval already has at least two points
                continue
            elif s > last:
                # interval has none of {last2, last}: add two new points
                res += 2
                last2 = e - 1
                last = e
            else:
                # interval has only `last`: add one more point
                res += 1
                last2 = last
                last = e

        return res
