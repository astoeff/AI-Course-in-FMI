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

def create_board_for_asymmetric_board(n):
    board = []
    d1 = [0 for i in range(n*2 - 1)]
    d2 = [0 for i in range(n*2 - 1)]
    even_cols_index = int(n/2)
    odd_cols_index = 0
    diagonal_index = n - 1
    for i in range(n):

        if i % 2 == 0:
            board.append(even_cols_index)
            d1[diagonal_index + i - board[i]] += 1
            d2[i + board[i]] += 1
            even_cols_index += 1
        else:
            board.append(odd_cols_index)
            d1[diagonal_index + i - board[i]] += 1
            d2[i + board[i]] += 1
            odd_cols_index += 1

    return board, d1, d2

# def create_for_false(board):
#     d1 = [0 for i in range(n*2 - 1)]
#     d2 = [0 for i in range(n*2 - 1)]
#     diagonal_index = n - 1
#     for i in range(n):
#         if i % 2 == 0:
#             d1[diagonal_index + i - board[i]] += 1
#             d2[i + board[i]] += 1
#         else:
#             board.append(odd_cols_index)
#             d1[diagonal_index + i - board[i]] += 1
#             d2[i + board[i]] += 1
#             odd_cols_index += 1

#     return board, d1, d2

def create_random_board(n):
    board = random.sample(range(0, n), n)
    print(board)

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
    if is_n_size_of_symmetric_board:
        solved_board_queens_positions = create_board_for_symmetric_board(n)
    else:
        board, d1, d2 = create_board_for_asymmetric_board(n)
        print_board(n, board)
        print(board)
        print(d1)
        print(d2)

    # print(n, '---->', solved_board_queens_positions)

    # init = create_board(7)
    # board = init[0]
    # for i in range(7):
    #     row = ''
    #     for j in range(7):
    #         if board[j] == i:
    #             row += 'X '
    #         else:
    #             row += '_ '
    #     print(row)
    # d1 = init[1]
    # d2 = init[2]

    # start_time = time.time()
    # print(check_is_solved(board, d1, d2))
    # print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
   main()
