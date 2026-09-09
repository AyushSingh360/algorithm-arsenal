class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # sort by start time
        intervals.sort(key=lambda x: x[0])

        merged = []
        current_start, current_end = intervals[0]

        for start, end in intervals[1:]:
            # if overlapping, extend the current interval
            if start <= current_end:
                current_end = max(current_end, end)
            else:
                # no overlap, push the finished interval and start a new one
                merged.append([current_start, current_end])
                current_start, current_end = start, end

        # add the last interval
        merged.append([current_start, current_end])
        return merged
