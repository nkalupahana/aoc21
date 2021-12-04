import numpy as np
import pandas as pd

nums = []
boards = []
BINGO_SIZE = 5
FOUND_MARKER = -1

def bingo(df):
    a = df.to_numpy()
    return (FOUND_MARKER == a).all(0)

# Read input into nums and boards (list of dataframes)
with open("day4.txt") as f:
    nums = [int(x) for x in f.readline().strip().split(",")]
    while True:
        board = []
        if f.readline() == "":
            break

        for _ in range(BINGO_SIZE):
            board.append([int(x) for x in f.readline().strip().split(" ") if x != ""])

        boards.append(pd.DataFrame(board))

def solve():
    for num in nums:
        for board in boards:
            board.replace(num, FOUND_MARKER, inplace=True)
            if np.any(bingo(board) + bingo(board.transpose())):
                print(board.replace(FOUND_MARKER, 0).sum().sum() * num)
                return

solve()