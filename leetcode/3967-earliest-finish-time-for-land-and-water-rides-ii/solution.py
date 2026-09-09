from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:

        def solve(
            A_start: List[int], A_dur: List[int], B_start: List[int], B_dur: List[int]
        ) -> int:
            # Earliest we can finish any ride in category A if we do A first
            first_finish = min(s + d for s, d in zip(A_start, A_dur))

            # Now pick best ride from category B as second
            best = float("inf")
            for s, d in zip(B_start, B_dur):
                start_second = max(first_finish, s)
                best = min(best, start_second + d)
            return best

        # Try both orders: land -> water and water -> land
        res1 = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        res2 = solve(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(res1, res2)
