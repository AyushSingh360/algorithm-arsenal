class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1
        prev_critical = -1
        min_dist = float("inf")

        prev = head
        curr = head.next
        pos = 2  # 1-indexed position of curr

        while curr and curr.next:
            nxt = curr.next

            is_maxima = curr.val > prev.val and curr.val > nxt.val
            is_minima = curr.val < prev.val and curr.val < nxt.val

            if is_maxima or is_minima:
                if first == -1:
                    first = pos
                else:
                    min_dist = min(min_dist, pos - prev_critical)

                prev_critical = pos

            prev = curr
            curr = nxt
            pos += 1

        if first == -1 or first == prev_critical:
            return [-1, -1]

        return [min_dist, prev_critical - first]
