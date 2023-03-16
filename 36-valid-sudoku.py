class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 1-9 no repetition in rows or col
        # 1-9 no repetition at every sub-box

        #create a hashmap to detect duplicates in the cols and rows
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)

        #to find which square the cell is
        squares = collections.defaultdict(set) #key = (r//3, c//3)

        #iterate over the entire grid
        for r in range(9):  #we know the damensions are 9x9
            for c in range(9):
                #check if its an empty space. if it is, just skip it
                if board[r][c] == ".":
                    continue 
                
                #check if we found a duplicate
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:  #rows=hashmap, r=currect row we are in. checking if the number in board[r][c] is already in the dict 'rows'/ same thing with cols/ for square we're checking if this cell is in the set with all the values seen in the current square
                    return False #its a duplicate, so its an unvalid sudoku
                
                #if not false, update all the values
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True