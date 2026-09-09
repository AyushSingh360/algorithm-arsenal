from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        # hours: 0..11 (4 bits), minutes: 0..59 (6 bits)
        for h in range(12):
            for m in range(60):
                # total LEDs on = set bits in hour and minute
                if (h.bit_count() + m.bit_count()) == turnedOn:
                    ans.append(f"{h}:{m:02d}")
        return ans
