from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # direction vectors: N, E, S, W
        dirs = (0, 1, 0, -1, 0)  # (dx, dy) pairs are (dirs[i], dirs[i+1]) [web:6]
        d = 0  # 0:N,1:E,2:S,3:W

        # set of obstacle coordinates for O(1) lookup [web:6][web:9]
        obs = {(x, y) for x, y in obstacles}

        x = y = 0
        ans = 0

        for cmd in commands:
            if cmd == -2:  # turn left
                d = (d + 3) % 4
            elif cmd == -1:  # turn right
                d = (d + 1) % 4
            else:
                for _ in range(cmd):
                    nx = x + dirs[d]
                    ny = y + dirs[d + 1]
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)

        return ans
