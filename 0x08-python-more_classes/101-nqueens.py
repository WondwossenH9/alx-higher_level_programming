#!/usr/bin/python3
"""Solves the N-queens puzzle.

It determines all possible solutions to place N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of the lists representing the chessboard.
    solutions (list): A list of the lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)
