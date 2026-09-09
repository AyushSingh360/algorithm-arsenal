class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None
        """
        from collections import defaultdict

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(index):
            if index == len(empties):
                return True

            r, c = empties[index]
            b = (r // 3) * 3 + (c // 3)
            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if backtrack(index + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)
            return False

        backtrack(0)
