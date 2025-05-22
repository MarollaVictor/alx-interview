import sys

def is_safe(col, current_cols):
    current_row = len(current_cols)
    for r, c in enumerate(current_cols):
        if c == col or (current_row - r) == abs(col - c):
            return False
    return True

def backtrack(current_cols, solutions, N):
    current_row = len(current_cols)
    if current_row == N:
        solutions.append([[r, c] for r, c in enumerate(current_cols)])
        return
    for col in range(N):
        if is_safe(col, current_cols):
            current_cols.append(col)
            backtrack(current_cols, solutions, N)
            current_cols.pop()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    backtrack([], solutions, N)
    for sol in solutions:
        print(sol)

if __name__ == "__main__":
    main()
