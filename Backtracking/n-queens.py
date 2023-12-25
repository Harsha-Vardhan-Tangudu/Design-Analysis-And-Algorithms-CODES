def is_safe(board, row, col):
    return all(board[i] != col and abs(board[i] - col) != row - i for i in range(row))


def solve_nqueens_util(board, row, n, solutions):
    if row == n:
        solution = ["".join("Q" if i == col else "." for i in range(n)) for col in board]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            solve_nqueens_util(board + [col], row + 1, n, solutions)


def solve_nqueens(n):
    solutions = []
    solve_nqueens_util([], 0, n, solutions)

    for solution in solutions:
        for row in solution:
            print(row)
        print()


solve_nqueens(4)