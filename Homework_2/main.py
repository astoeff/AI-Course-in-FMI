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

# def create_board_for_asymmetric_board(n):
#     board = []
#     d1 = [0 for i in range(n*2 - 1)]
#     d2 = [0 for i in range(n*2 - 1)]
#     conflicts = []
#     even_cols_index = int(n/2)
#     odd_cols_index = 0
#     diagonal_index = n - 1
#     for i in range(n):
#         if i % 2 == 0:
#             board.append(even_cols_index)
#             even_cols_index += 1
#         else:
#             board.append(odd_cols_index)
#             odd_cols_index += 1
#         d1[diagonal_index + i - board[i]] += 1
#         d2[i + board[i]] += 1
#         # print(d1[diagonal_index + i - board[i]])
#         # print(d2[i + board[i]])
#         conflicts.append(d1[diagonal_index + i - board[i]] + d2[i + board[i]]  - 2)

    return board, d1, d2

def calculate_conflicts_for_all_queens(n, board, d1, d2):
    conflicts = []
    diagonal_index = n - 1
    # print('QUEEENS PER ROOOW')
    for i in range(n):
        queens_per_row = board.count(i)

        #do not count current queen for conflicts
        if queens_per_row > 0:
            queens_per_row -= 1
        # print(queens_per_row)
        conflicts.append(d1[diagonal_index + i - board[i]] + d2[i + board[i]]  - 2 + queens_per_row)

    return conflicts

def get_col_of_queen_with_max_conflict(board, conflicts):
    max_conflicts = max(conflicts)
    cols_of_queens_with_max_conflict = [i for i,x in enumerate(conflicts) if x == max_conflicts]
    col_of_random_queen_of_queens_with_max_conflict = random.choice(cols_of_queens_with_max_conflict)
    return col_of_random_queen_of_queens_with_max_conflict

def get_row_with_min_conflict_for_col(n, board, d1, d2, col):
    current_row_of_queen_with_max_conflicts = board[col]
    # print(current_row_of_queen_with_max_conflicts)

    min_conflicts = None
    min_conflicts_rows = []
    diagonal_index = n - 1

    all_conflicts_for_rows = []
    # print(d1)
    # print(d2)
    #go through all the rows
    for row in range(n):
        if row != current_row_of_queen_with_max_conflicts:
            queens_in_row = board.count(row)
            queens_in_d1 = d1[diagonal_index + row - col]
            queens_in_d2 = d2[row + col]
            # print(str(queens_in_d1) + ' ' + str(queens_in_d2))
            all_conflicts_for_position = queens_in_row + queens_in_d1 + queens_in_d2
            all_conflicts_for_rows.append(queens_in_row + queens_in_d1 + queens_in_d2)
            if min_conflicts:
                if min_conflicts > all_conflicts_for_position:
                    min_conflicts = all_conflicts_for_position
                    min_conflicts_rows = [row]
                elif min_conflicts == all_conflicts_for_position:
                    min_conflicts_rows.append(row)
            else:
                min_conflicts = all_conflicts_for_position
                min_conflicts_rows.append(row)
    # print(all_conflicts_for_rows)
    # print(min_conflicts_rows)

    random_min_conflict_row = random.choice(min_conflicts_rows)
    return random_min_conflict_row

def update_board(n ,board, d1, d2, conflicts, previous_row, next_row, col):
    # print(next_row)
    diagonal_index = n -1

    #update previous position diagonals
    d1[diagonal_index + col - previous_row] -= 1
    d2[previous_row + col] -= 1

    #update new position diagonals
    d1[diagonal_index + col - next_row] += 1
    d2[next_row + col] += 1

    #update board
    board[col] = next_row

    #update conflicts
    conflicts = calculate_conflicts_for_all_queens(n, board, d1, d2)
    # print(d1[diagonal_index + previous_row - col])
    # print(d2[previous_row + col])
    # print(d1[diagonal_index + next_row - col] )
    # print(d2[next_row + col])

    return board, d1, d2, conflicts

def create_random_board(n):
    board = random.sample(range(0, n), n)
    d1 = [0 for i in range(n*2 - 1)]
    d2 = [0 for i in range(n*2 - 1)]
    diagonal_index = n - 1
    for i in range(n):
        d1[diagonal_index + i - board[i]] += 1
        d2[i + board[i]] += 1

    return board, d1, d2

def check_is_solved(board, d1, d2):
    is_there_one_queen_per_row = len(set(board)) == len(board)
    is_there_one_queen_per_d1 = max(d1) == 1
    is_there_one_queen_per_d2 = max(d2) == 1
    return is_there_one_queen_per_row and is_there_one_queen_per_d1 and is_there_one_queen_per_d2

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
        k = 12
        is_solved = False
        start_time = time.time()
        c = 0
        while not is_solved:
            c += 1
            print(c)
            board, d1, d2 = create_random_board(n)
            conflicts = calculate_conflicts_for_all_queens(n, board, d1, d2)
            if max(conflicts) == 0:
                break

            condition_for_restart = k * n
            while condition_for_restart > 0:
                col = get_col_of_queen_with_max_conflict(board, conflicts)
                row = get_row_with_min_conflict_for_col(n, board, d1, d2, col)
                board, d1, d2, conflicts = update_board(n ,board, d1, d2, conflicts, board[col], row, col)
                if max(conflicts) == 0:
                    solved_board_queens_positions = board
                    is_solved = True
                    break
                condition_for_restart -= 1
        # print('Queens: ', board)
        # print('D1: ', d1)
        # print('D2: ', d2)
        # print('Conflicts: ', conflicts)

        print("--- %s seconds ---" % (time.time() - start_time))

    if n < 100:
         print_board(n, solved_board_queens_positions)


if __name__ == '__main__':
   main()
# https://queens.lyndenlea.info/nqueens.php?pg=solutions&sol=14