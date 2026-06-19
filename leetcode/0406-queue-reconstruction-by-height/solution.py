class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending, and for same height, k ascending
        people.sort(key=lambda x: (-x[0], x[1]))

        result = []
        for p in people:
            # Insert at position p[1] (which is k)
            result.insert(p[1], p)

        return result
