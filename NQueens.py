class NQueensCSP:
    def __init__(self, n):
        self.n = n
        self.grid = [["." for _ in range(n)] for _ in range(n)]

    def display(self):
        for r in range (self.n):
            print(" ".join(self.grid[r]))
        print()
            
    def place(self, row, col):
        for prev_row in range(row):
            prev_col = self.grid[prev_row].index("Q") if "Q" in self.grid[prev_row] else -1
            if prev_col == -1:
                continue
            if prev_col == col:
                return False
            if prev_row - prev_col == row - col:
                return False
            if prev_row + prev_col == row + col:
                return False

        return True

    def solve(self, row = 0):
        if row == self.n:
            self.display()
            return True
        for col in range(self.n):
            if self.place(row, col):
                self.grid[row][col] = "Q"
                if self.solve(row + 1):
                    return True
                self.grid[row][col] = "."
        return False
            
def main():
    n = int(input("Enter n: "))
    solver = NQueensCSP(n)
    if not solver.solve():
        print("No solution.")

main()
