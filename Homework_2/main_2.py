import random
import time

count_of_queens = 0
board = []
row_conflicts = []
diagr_conflicts = []
diagl_conflicts = []


def changeConflicts(col, row, val):
    row_conflicts[row] += val
    diagr_conflicts[col + row] += val
    diagl_conflicts[col + (count_of_queens - row - 1)] += val


def calculate_all_conflicts(current_row, count_of_queens, col):
    return row_conflicts[current_row] + diagr_conflicts[col + current_row] + diagl_conflicts[col + (count_of_queens - current_row - 1)]


def minConflictPos(col):
    minConflicts = count_of_queens
    minConflictRows = []
    for row in range(count_of_queens):
        conflicts = calculate_all_conflicts(row, count_of_queens, col)
        if conflicts == 0:
            return row
        if conflicts < minConflicts:
            minConflictRows = [row]
            minConflicts = conflicts
        elif conflicts == minConflicts:
            minConflictRows.append(row)
    choice = random.choice(minConflictRows)
    return choice


def findMaxConflictCol():
    conflicts = 0
    maxConflicts = 0
    maxConflictCols = []
    for col in range(0, count_of_queens):
        row = board[col]
        conflicts = calculate_all_conflicts(row, count_of_queens, col)
        if (conflicts > maxConflicts):
            maxConflictCols = [col]
            maxConflicts = conflicts
        elif conflicts == maxConflicts:
            maxConflictCols.append(col)
    choice = random.choice(maxConflictCols)
    return choice, maxConflicts

def createBoard():
    global board
    global row_conflicts
    global diagr_conflicts
    global diagl_conflicts

    board = random.sample(range(0, count_of_queens), count_of_queens)
    queens = set(range(0, count_of_queens))
    diagl_conflicts = [0 for i in range(count_of_queens*2 - 1)]
    diagr_conflicts = [0 for i in range(count_of_queens*2 - 1)]
    row_conflicts = [0 for i in range(count_of_queens)]
    diagonal_index = count_of_queens - 1
    for i in range(count_of_queens):
        diagl_conflicts[diagonal_index + i - board[i]] += 1
        diagr_conflicts[i + board[i]] += 1
        row_conflicts[board[i]] += 1

def solveNQueens():
    createBoard()
    iteration = 0
    maxIteration = 0.7 * count_of_queens

    while (iteration < maxIteration):
        col, numConflicts = findMaxConflictCol()
        if (numConflicts > 3):
            newLocation = minConflictPos(col)
            if (newLocation != board[col]):
                changeConflicts(col, board[col], -1)
                board[col] = newLocation
                changeConflicts(col, newLocation, 1)
            else:
                break
        elif numConflicts == 3:
            return True, board
        iteration += 1
    return False, board


def main():
    global count_of_queens
    global board
    global row_conflicts
    global diagr_conflicts
    global diagl_conflicts
    count_of_queens = int(input('Input number of queens: '))
    if count_of_queens <= 3 or count_of_queens > 10000000:
        print("Cannot build board of size: " + str(count_of_queens))
    else:
        time0 = time.time()
        solved = False
        while (not solved):
            solved, board = solveNQueens()
        time1 = time.time()
        tot_time = time1 - time0 + 1
    if count_of_queens <= 10:
        represent_board = [['_' for row in range(0, count_of_queens)] for i in range(count_of_queens)]
        for i in range(len(board)):
            represent_board[board[i]][i] = 'Q'
        for elem in represent_board:
            print(elem)
    else:
        print("Seconds: ")
        print(tot_time)


main()