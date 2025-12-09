from random import randint


def find_optimal_path(table, col, row=0, results=[], cost=0):
    cost += table[row][col]
    if row == 7:
        results.append(cost)
        return
    if col == 0:
        find_optimal_path(table, col, row+1, results, cost)
        find_optimal_path(table, col+1, row+1, results, cost)
    if col == 7:
        find_optimal_path(table, col, row+1, results, cost)
        find_optimal_path(table, col-1, row+1, results, cost)
    if 0 < col < 7:
        find_optimal_path(table, col-1, row+1, results, cost)
        find_optimal_path(table, col, row+1, results, cost)
        find_optimal_path(table, col+1, row+1, results, cost)
    return min(results)


if __name__ == '__main__':
    board = [[randint(1, 10) for _ in range(8)] for _ in range(8)]
    for r in board:
        print(r)
    print(find_optimal_path(board, 2))
