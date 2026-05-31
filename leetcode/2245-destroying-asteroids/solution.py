from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        # Use a larger integer type if language requires; in Python int is unbounded
        cur_mass = mass

        for a in asteroids:
            if cur_mass < a:
                return False
            cur_mass += a

        return True
