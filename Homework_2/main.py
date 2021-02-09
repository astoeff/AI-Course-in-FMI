import random
import time 

def create_board_for_symmetric_board(n):
    '''symmetric boards all follow this pattern:
       _ Q _ _ _ _ _
       _ _ _ Q _ _ _
       _ _ _ _ _ Q _
       Q _ _ _ _ _ _
       _ _ Q _ _ _ _
       _ _ _ _ Q _ _
       _ _ _ _ _ _ Q
    '''

    board = []
    even_cols_index = int(n/2)
    odd_cols_index = 0
    diagonal_index = n - 1
    for i in range(n):
        if i % 2 == 0:
            board.append(even_cols_index)
            even_cols_index += 1
        else:
            board.append(odd_cols_index)
            odd_cols_index += 1

    return board

def calculate_conflicts_for_all_queens(n, board, queens_in_rows, d1, d2):
    conflicts = []
    diagonal_index = n - 1
    max_conflicts = 0
    for i in range(n):
        queens_per_row = queens_in_rows[board[i]]

        #do not count current queen for conflicts
        if queens_per_row > 0:
            queens_per_row -= 1
        conflicts.append(d1[diagonal_index + i - board[i]] + d2[i + board[i]]  - 2 + queens_per_row)
        if max_conflicts < conflicts[i]:
            max_conflicts = conflicts[i]

    return conflicts, max_conflicts

def get_col_of_queen_with_max_conflict(board, conflicts):
    max_conflicts = 0
    cols_of_queens_with_max_conflict = []
    index = 0
    for i in conflicts:
        if i > max_conflicts:
            max_conflicts = i
            cols_of_queens_with_max_conflict.append(index)
        elif i == max_conflicts:
            cols_of_queens_with_max_conflict.append(index)
        index += 1
    col_of_random_queen_of_queens_with_max_conflict = random.choice(cols_of_queens_with_max_conflict)
    return col_of_random_queen_of_queens_with_max_conflict

def get_row_with_min_conflict_for_col(n, board, queens_in_rows, d1, d2, col):
    current_row_of_queen_with_max_conflicts = board[col]

    min_conflicts = None
    min_conflicts_rows = []
    diagonal_index = n - 1

    all_conflicts_for_rows = []

    #go through all the rows
    for row in range(n):
        if row != current_row_of_queen_with_max_conflicts:
            queens_in_row = queens_in_rows[row]
            queens_in_d1 = d1[diagonal_index + row - col]
            queens_in_d2 = d2[row + col]

            all_conflicts_for_position = queens_in_row + queens_in_d1 + queens_in_d2
            all_conflicts_for_rows.append(queens_in_row + queens_in_d1 + queens_in_d2)
            if min_conflicts:
                if min_conflicts > all_conflicts_for_position:
                    min_conflicts = all_conflicts_for_position
                    min_conflicts_rows.append(row)
                elif min_conflicts == all_conflicts_for_position:
                    min_conflicts_rows.append(row)
            else:
                min_conflicts = all_conflicts_for_position
                min_conflicts_rows.append(row)

    random_min_conflict_row = random.choice(min_conflicts_rows)
    return random_min_conflict_row

def update_board(n, board, queens_in_rows, d1, d2, conflicts, previous_row, next_row, col):
    diagonal_index = n -1

    #update previous position diagonals
    d1[diagonal_index + col - previous_row] -= 1
    d2[previous_row + col] -= 1

    #update new position diagonals
    d1[diagonal_index + col - next_row] += 1
    d2[next_row + col] += 1

    #update board
    board[col] = next_row

    #update rows
    queens_in_rows[previous_row] -= 1
    queens_in_rows[next_row] += 1

    #update conflicts
    conflicts, max_conflicts = calculate_conflicts_for_all_queens(n, board, queens_in_rows, d1, d2)

    return board, d1, d2, queens_in_rows, conflicts

# def create_random_board(n):
#     board = random.sample(range(0, n), n)
#     d1 = [0 for i in range(n*2 - 1)]
#     d2 = [0 for i in range(n*2 - 1)]
#     queens_in_rows = [0 for i in range(n)]
#     diagonal_index = n - 1
#     for i in range(n):
#         d1[diagonal_index + i - board[i]] += 1
#         d2[i + board[i]] += 1
#         queens_in_rows[board[i]] += 1

#     return board, queens_in_rows, d1, d2

def changeConflicts(col, row, val, row_conflicts, diagr_conflicts, diagl_conflicts, n):
    row_conflicts[row] += val
    diagr_conflicts[col + row] += val
    diagl_conflicts[col + (n - row - 1)] += val


def calculate_all_conflicts(current_row, n, col, row_conflicts, diagr_conflicts, diagl_conflicts):
    return row_conflicts[current_row] + diagr_conflicts[col + current_row] + diagl_conflicts[col + (n - current_row - 1)]

def create_random_board(n):
    # global board
    # global row_conflicts
    # global diagr_conflicts
    # global diagl_conflicts
    board = []
    diagr_conflicts = [0] * ((2 * n) - 1)
    diagl_conflicts = [0] * ((2 * n) - 1)
    row_conflicts = [0] * n
    #random_queens = random.sample(range(0, count_of_queens), count_of_queens)
    random_queens = set(range(0, n))
    notPlaced = []
    for col in range(0, n):
        current_queen = random_queens.pop()
        conflicts = calculate_all_conflicts(current_queen, n, col, row_conflicts, diagr_conflicts, diagl_conflicts)
        if conflicts == 0:
            board.append(current_queen)
            changeConflicts(col, board[col], 1, row_conflicts, diagr_conflicts, diagl_conflicts, n)
        else:
            random_queens.add(current_queen)
            current_queen2 = random_queens.pop()
            conflicts2 = calculate_all_conflicts(current_queen2, n, col, row_conflicts, diagr_conflicts, diagl_conflicts)
            if conflicts2 == 0:
                board.append(current_queen2)
                changeConflicts(col, board[col], 1, row_conflicts, diagr_conflicts, diagl_conflicts, n)
            else:
                random_queens.add(current_queen2)
                board.append(None)
                notPlaced.append(col)
    for col in notPlaced:
        board[col] = random_queens.pop()
        changeConflicts(col, board[col], 1, row_conflicts, diagr_conflicts, diagl_conflicts, n)

    return board, row_conflicts, diagl_conflicts, diagr_conflicts

def print_board(n, board):
    first_row = '  '
    for i in range(n):
        first_row += str(i) + ' '
    print(first_row)

    for i in range(n):
        row = str(i) + ' '
        for j in range(n):
            if board[j] == i:
                row += 'Q '
            else:
                row += '_ '
        print(row)

def main():
    n = int(input('Enter size of board: '))
    solved_board_queens_positions = []

    #for n = 2 and n = 3 there is no solution
    assert n != 2 and n != 3, 'The board is not solvable, please try with size different from 2 or 3!'

    #all sizes except for 8, 9, 14, 15, 20, 21, 26, 27 ... (6 % 2 == 2 or 6 % 3 == 3) follow a symmetric pattern for solution
    is_n_size_of_symmetric_board = n % 6 != 2 and n % 6 != 3
    is_n_size_of_symmetric_board = False
    if is_n_size_of_symmetric_board:
        solved_board_queens_positions = create_board_for_symmetric_board(n)
    else:
        k = 8
        is_solved = False
        start_time = time.time()
        while not is_solved:
            board, queens_in_rows, d1, d2 = create_random_board(n)
            conflicts, max_conflicts = calculate_conflicts_for_all_queens(n, board, queens_in_rows, d1, d2)
            if max_conflicts == 0:
                solved_board_queens_positions = board
                break

            condition_for_restart = k * n
            while condition_for_restart > 0:
                col = get_col_of_queen_with_max_conflict(board, conflicts)
                row = get_row_with_min_conflict_for_col(n, board, queens_in_rows, d1, d2, col)
                board, d1, d2, queens_in_rows, conflicts = update_board(n, board, queens_in_rows, d1, d2, conflicts, board[col], row, col)
                if max(conflicts) == 0:
                    solved_board_queens_positions = board
                    is_solved = True
                    break
                condition_for_restart -= 1

        print("--- %s seconds ---" % (time.time() - start_time))

    if n < 40:
         print_board(n, solved_board_queens_positions)


if __name__ == '__main__':
   main()
