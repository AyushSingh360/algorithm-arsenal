class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort in descending order
        citations.sort(reverse=True)

        h = 0
        # p is the index, so p + 1 is the candidate h value
        for p, c in enumerate(citations):
            if c >= p + 1:
                h = p + 1
            else:
                break

        return h
