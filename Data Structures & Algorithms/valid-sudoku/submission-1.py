class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each row must have 1-9 wthout dupes
        # each column must have 1-9 without dupes
        # each 3 by 3 grid must also have that
        cols = defaultdict(set)
        rows = defaultdict(set)
        sqrs = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                # gowing through the row so validate
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row]
                or board[row][col] in cols[col]
                or board[row][col] in sqrs[(row // 3, col // 3)]):
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                sqrs[(row // 3, col // 3)].add(board[row][col])
        return True
        
                


        