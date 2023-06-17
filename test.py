import math
import copy


X = "X"
O = "O"
EMPTY = None

def main():
    board = [[X, EMPTY, EMPTY],
            [EMPTY, O, X],
            [EMPTY, O, EMPTY]]

    newboard = copy.deepcopy(board)
    print(len(board[0]))

if __name__ == "__main__":
    main()