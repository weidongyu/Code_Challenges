class Solution():
    def countShips(self, board):
        counter = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    if not( r >= 1 and board[r-1][c] == 'X' or c >= 1 and board[r][c-1] == 'X'):
                        counter += 1
        return counter

s = Solution()

board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

print s.countShips(board)