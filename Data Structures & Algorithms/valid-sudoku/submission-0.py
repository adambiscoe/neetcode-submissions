class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def squareFinder(row, col):
            #first row of squares

            squareRow = row // 3
            squareCol = col // 3
            return squareRow * 3 + squareCol


        squares = [set(),set(),set(),set(),set(),set(),set(),set(),set()]  
        rows = [set(),set(),set(),set(),set(),set(),set(),set(),set()]        
        cols = [set(),set(),set(),set(),set(),set(),set(),set(),set()]        
      
      #by rows first, then cols
        for i in range(9):
            currRow = board[i]
            for j in range(9):
                if not currRow[j] == ".":

                    if currRow[j] in rows[i]:
                        return False
                    rows[i].add(currRow[j])
                    if currRow[j] in cols[j]:
                        return False
                    cols[j].add(currRow[j])
                    if currRow[j] in squares[squareFinder(i, j)]:
                        return False
                    squares[squareFinder(i, j)].add(currRow[j])
        return True

        

        