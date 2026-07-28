class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = []
        cols = []
        boxes = []

        for i in range(9):
            rows.append(set())
        for i in range(9):
            cols.append(set())
        for i in range(9):
            boxes.append(set())

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue
                boxIndex = (r // 3) * 3 + (c // 3)

                if value in rows[r] or value in cols[c] or value in boxes[boxIndex]:
                    return False
                rows[r].add(value)
                cols[c].add(value)
                boxes[boxIndex].add(value)


        return True