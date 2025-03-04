class MinimumEditDistance:
    def __init__(self, s1: str, s2: str, d_cost=1, i_cost=1, s_cost=1):
        m, n = len(s1), len(s2)
        self.grid = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            self.grid[i][0] = self.grid[i - 1][0] + d_cost
        for j in range(1, n + 1):
            self.grid[0][j] = self.grid[0][j - 1] + i_cost

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                i_dist = self.grid[i][j - 1] + i_cost
                d_dist = self.grid[i - 1][j] + d_cost
                s_dist = (
                    self.grid[i - 1][j - 1] + s_cost
                    if s1[i - 1] != s2[j - 1]
                    else self.grid[i - 1][j - 1]
                )
                self.grid[i][j] = min(s_dist, i_dist, d_dist)

    def get_distance(self):
        return self.grid[-1][-1]

    def print_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[-1])):
                end = " " if self.grid[i][j] / 10 >= 1 else "  "
                print(self.grid[i][j], end=end)
            print("\n")

    def print_alignment():
        pass


med = MinimumEditDistance("intention", "execution", s_cost=2)
med = MinimumEditDistance("leda", "deal")
print(med.get_distance())
med.print_grid()
