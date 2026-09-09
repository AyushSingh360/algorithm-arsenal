class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        def max_gap(bars: List[int]) -> int:
            bars.sort()
            max_run = 1  # length (in bars) of longest consecutive sequence
            cur_run = 1

            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    cur_run += 1
                    if cur_run > max_run:
                        max_run = cur_run
                else:
                    cur_run = 1

            # removing `max_run` consecutive bars produces a gap of size `max_run + 1`
            return max_run + 1

        max_h = max_gap(hBars)  # max horizontal cell-span
        max_v = max_gap(vBars)  # max vertical cell-span

        side = min(max_h, max_v)
        return side * side
