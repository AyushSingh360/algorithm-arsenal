from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)
        robots = sorted([(positions[i], i) for i in range(n)])

        stack = []  # indices of surviving right-moving robots
        alive = [True] * n

        for _, i in robots:
            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and alive[i]:
                    j = stack[-1]  # right-moving robot

                    if healths[j] < healths[i]:
                        alive[j] = False
                        stack.pop()
                        healths[i] -= 1
                    elif healths[j] > healths[i]:
                        alive[i] = False
                        healths[j] -= 1
                    else:
                        alive[i] = False
                        alive[j] = False
                        stack.pop()

        return [healths[i] for i in range(n) if alive[i]]
