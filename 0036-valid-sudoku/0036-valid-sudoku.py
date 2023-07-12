class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        # Use is unique for each row and column?
        # Then create a box with the key of [r/3,c/3], and it will containe the value of a hashset
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set)


        for r in range(9):
            for c in range(9):
                curNum = board[r][c]

                if curNum == ".":
                    continue

                if(
                    curNum in rows[r]
                    or curNum in cols[c]
                    or curNum in box[(r//3,c//3)]
                ): return False

                rows[r].add(curNum)
                cols[c].add(curNum)
                box[(r//3,c//3)].add(curNum)

        return True


