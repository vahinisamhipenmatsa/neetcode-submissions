class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each row must have 1-9 wthout dupes
        # each column must have 1-9 without dupes
        # each 3 by 3 grid must also have that
        col = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # first we are checking if it is a dot that just means empty
                if board[r][c]== ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in col[c] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                # now we need to add to our dictipnaires
                col[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True





        