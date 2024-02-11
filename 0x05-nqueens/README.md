# N queens

The N queens puzzle is a challenge of placing N non-attacking queens on an NxN chessboard.

On a chessboard, queen can move any number of squares vertically, horizontally or diagonally.Thus, to solve puzzle, each queen must be placed on its own row, column and diagonal.

This is most efficiently solved using a backtracking algorithm. Backtracking is a general algorithm for finding solutions to some computational problems that incrementally builds candidates to the solutions, and abandons a candidate i.e.,
backtracks as soon as it determines that candidate cannot possibly be completed to a valid solution.

## Usage

```nqueens N```
where N is the number of queens.
      - N must be an integer greater or equal to 4
      - the program prints every possible solution to the problem in the format
        shown below
```

usage
$ ./0-nqueens 4

```
