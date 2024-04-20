

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        from collections import defaultdict

        rows = defaultdict(set)
        cols = defaultdict(set)
        subs = defaultdict(set)

        board_size = len(board)
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == ".":
                    continue
                if any(
                    [
                        board[row][col] in rows[row],
                        board[row][col] in cols[col],
                        board[row][col] in subs[row // 3, col // 3]]):
                        return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                subs[row // 3, col // 3].add(board[row][col])
        return True