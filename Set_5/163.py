

def recursion(board, row=0, col=0):
    if row == col == 7:
        return True
    if col < 7 and str(board[row][col+1])[0] > str(board[row][col])[-1]:
        if recursion(board, row, col+1):
            return True
    if row < 7 and col < 7 and str(board[row+1][col+1])[0] > str(board[row][col])[-1]:
        if recursion(board, row+1, col+1):
            return True
    if row < 7 and str(board[row+1][col])[0] > str(board[row][col])[-1]:
        if recursion(board, row+1, col):
            return True

    return False



if __name__ == '__main__':
    from random import randint
    board = [[randint(1, 100) for _ in range(8)] for _ in range(8)]

    print(recursion(board))


