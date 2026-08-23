
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # each 3x3 box
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue  # empty cell, ignore
                # compute which 3x3 box this cell belongs to
                box_index = (r // 3) * 3 + (c // 3)
                # check duplicates in row, column, or box
                if (val in rows[r] or
                    val in cols[c] or
                    val in boxes[box_index]):
                    return False
                # mark this value as seen
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        return True
