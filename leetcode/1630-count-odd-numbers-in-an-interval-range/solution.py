class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Number of odds from 1 to high
        odds_up_to_high = (high + 1) // 2
        # Number of odds from 1 to low-1
        odds_before_low = low // 2
        # Odds in [low, high] = odds_up_to_high - odds_before_low
        return odds_up_to_high - odds_before_low
