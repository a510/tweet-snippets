N = 4

def safe(row, col, cols):
    for r, c in enumerate(cols):
        if c == col:
            return False
        if abs(c - col) == row - r:
            return False
    return True

def place(row, cols):
    if row == N:
        return True
    for col in range(N):
        if safe(row, col, cols):
            cols.append(col)
            if place(row + 1, cols):
                return True
            cols.pop()
    return False

cols = []
place(0, cols)
print(cols)   # [1, 3, 0, 2]: the queen's column in each row
