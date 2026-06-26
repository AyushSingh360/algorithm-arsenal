from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        chars = ["A", "C", "G", "T"]
        q = deque([(startGene, 0)])
        seen = {startGene}

        while q:
            gene, steps = q.popleft()
            if gene == endGene:
                return steps

            # try all 1-step mutations
            arr = list(gene)
            for i in range(len(arr)):
                orig = arr[i]
                for c in chars:
                    if c == orig:
                        continue
                    arr[i] = c
                    candidate = "".join(arr)
                    if candidate in bank_set and candidate not in seen:
                        seen.add(candidate)
                        q.append((candidate, steps + 1))
                arr[i] = orig

        return -1
