
solution_count = 0


def print_board(board, n):
    global solution_count
    solution_count += 1

    print(f"\nSolution {solution_count}:\n")
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


def is_safe(board, row, col, n):

    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueen(board, col, n):

    if col == n:
        print_board(board, n)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueen(board, col + 1, n)
            board[i][col] = 0   



n = int(input("Enter number of queens (N): "))

board = [[0]*n for _ in range(n)]

solve_nqueen(board, 0, n)

print("Total Solutions =", solution_count)