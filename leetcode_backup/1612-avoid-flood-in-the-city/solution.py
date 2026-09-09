from bisect import bisect_right


class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        n = len(rains)
        ans = [-1] * n

        # lastRain[lake] = last index when this lake got rain (is full from that day)
        lastRain = {}

        # sorted list of indices where rains[i] == 0 (days we can dry some lake)
        dryDays = []

        for i, lake in enumerate(rains):
            if lake > 0:
                # it's raining on lake
                if lake in lastRain:
                    # lake already full, we must dry it on some dry day > lastRain[lake]
                    prev = lastRain[lake]

                    # find smallest dry day index > prev
                    pos = bisect_right(dryDays, prev)
                    if pos == len(dryDays):
                        # no dry day available after prev -> impossible
                        return []

                    dryIndex = dryDays[pos]
                    # use this dry day to dry 'lake'
                    ans[dryIndex] = lake
                    # remove that dry day from available list
                    dryDays.pop(pos)

                # now lake becomes full today
                lastRain[lake] = i
                ans[i] = -1  # per problem, rainy days are -1
            else:
                # dry day, mark as 1 for now; if unused, any value is ok
                dryDays.append(i)
                ans[i] = 1  # placeholder, may be overwritten later

        return ans
