import random
import time 

def create_board(n):
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

def create_for_false(board):
    d1 = [0 for i in range(n*2 - 1)]
    d2 = [0 for i in range(n*2 - 1)]
    diagonal_index = n - 1
    for i in range(n):
        if i % 2 == 0:
            d1[diagonal_index + i - board[i]] += 1
            d2[i + board[i]] += 1
        else:
            board.append(odd_cols_index)
            d1[diagonal_index + i - board[i]] += 1
            d2[i + board[i]] += 1
            odd_cols_index += 1

    return board, d1, d2

def create_random_board(n):
    board = random.sample(range(0, n), n)
    print(board)

def check_is_solved(board, d1, d2):
    is_there_one_queen_per_row = len(set(board)) == len(board)
    is_there_one_queen_per_d1 = max(d1) == 1
    is_there_one_queen_per_d2 = max(d2) == 1
    return is_there_one_queen_per_row and is_there_one_queen_per_d1 and is_there_one_queen_per_d2


if __name__ == '__main__':
    # init = create_board(14)
    # board = init[0]
    # # for i in range(37):
    # #     row = ''
    # #     for j in range(37):
    # #         if board[j] == i:
    # #             row += 'X '
    # #         else:
    # #             row += '_ '
    # #     print(row)
    # d1 = init[1]
    # d2 = init[2]

    start_time = time.time()
    print(check_is_solved(board, d1, d2))
    print("--- %s seconds ---" % (time.time() - start_time))