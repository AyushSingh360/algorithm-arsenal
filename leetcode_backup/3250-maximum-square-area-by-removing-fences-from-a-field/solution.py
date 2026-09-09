class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        MOD = 10**9 + 7

        def all_distances(fences: List[int], limit: int) -> set[int]:
            # Include borders as fixed fences
            positions = fences + [1, limit]
            positions.sort()
            dists = set()
            L = len(positions)
            for i in range(L):
                for j in range(i + 1, L):
                    dists.add(positions[j] - positions[i])
            return dists

        h_dists = all_distances(hFences, m)
        v_dists = all_distances(vFences, n)

        common = h_dists & v_dists
        if not common:
            return -1

        side = max(common)
        return (side * side) % MOD
