class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False
        
        lCol = 0
        rCol = len(matrix[-1]) - 1

        lRow = 0
        rRow = len(matrix) - 1

        while lRow <= rRow:
            mRow = lRow + ((rRow - lRow) // 2)

            if target < matrix[mRow][lCol]:
                rRow = mRow - 1
            elif target > matrix[mRow][rCol]:
                lRow = mRow + 1
            else:
                if not (lRow <= rRow):
                    return False
                else:
                    while lCol <= rCol:
                        m = lCol + ((rCol - lCol) // 2)

                        if target < matrix[mRow][m]:
                            rCol = m - 1
                        elif target > matrix[mRow][m]:
                            lCol = m + 1
                        else:
                            return True
        
        return False
                    


        