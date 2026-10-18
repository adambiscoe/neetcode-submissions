class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])
        minRow = 0
        maxRow = numRows - 1
        tgtRow = None
        while minRow <= maxRow:
            centerRow = matrix[(minRow + maxRow + 1) // 2]
            if target <= centerRow[numCols - 1] and target >= centerRow[0]:
                tgtRow = centerRow
                break
            if target > centerRow[numCols - 1]:
                minRow = ((minRow + maxRow + 1) // 2) + 1
            else:
                maxRow = ((minRow + maxRow + 1) // 2) - 1

        if tgtRow:
            print(tgtRow)
            minCol = 0
            maxCol = len(tgtRow) - 1
            while minCol <= maxCol:
                center = tgtRow[(minCol + maxCol + 1) // 2]
                if target == center:
                    return True
                if target > center:
                    minCol = ((minCol + maxCol + 1) // 2) + 1
                else:
                    maxCol = ((minCol + maxCol + 1) // 2) - 1

        else:
            return False
        return False


        