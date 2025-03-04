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


class Step:
    def __init__(self, init):
        self.insertion = init
        self.deletion = init
        self.substitution = init

    def get_min(self):
        return min(self.insertion, self.deletion, self.substitution)


class MinimumEditDistanceAndAlignment:
    def __init__(self, s1: str, s2: str, d_cost=1, i_cost=1, s_cost=1):
        step = 1
        self.s1, self.s2 = s1, s2
        m, n = len(s1), len(s2)
        self.grid = [[0] * (n + 1) for _ in range(m + 1)]
        self.steps = [[Step(float("inf")) for _ in range(n + 1)] for _ in range(m + 1)]
        self.steps[0][0] = Step(0)

        for i in range(1, m + 1):
            self.grid[i][0] = self.grid[i - 1][0] + d_cost
            self.steps[i][0].deletion = self.steps[i - 1][0].get_min() + step
        for j in range(1, n + 1):
            self.grid[0][j] = self.grid[0][j - 1] + i_cost
            self.steps[0][j].insertion = self.steps[0][j - 1].get_min() + step

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                i_dist = self.grid[i][j - 1] + i_cost
                d_dist = self.grid[i - 1][j] + d_cost
                s_dist = (
                    self.grid[i - 1][j - 1] + s_cost
                    if s1[i - 1] != s2[j - 1]
                    else self.grid[i - 1][j - 1]
                )
                self.grid[i][j] = min(i_dist, d_dist, s_dist)
                dist = self.grid[i][j]

                if dist == i_dist:
                    prev = self.steps[i][j - 1]
                    self.steps[i][j].insertion = prev.get_min() + step
                if dist == d_dist:
                    prev = self.steps[i - 1][j]
                    self.steps[i][j].deletion = prev.get_min() + step
                if dist == s_dist:
                    prev = self.steps[i - 1][j - 1]
                    self.steps[i][j].substitution = prev.get_min() + step

    def get_distance(self):
        return self.grid[-1][-1]

    def print_grid(self):
        print("   #", end="  ")
        for j in range(len(self.grid[-1]) - 1):
            print(self.s2[j], end="  ")
        print()
        for i in range(len(self.grid)):
            if i == 0:
                print("#", end="  ")
            else:
                print(self.s1[i - 1], end="  ")
            for j in range(len(self.grid[-1])):
                end = " " if self.grid[i][j] / 10 >= 1 else "  "
                print(self.grid[i][j], end=end)
            print()

    def print_alignment(self):
        ops = []
        i, j = len(self.steps) - 2, len(self.steps[0]) - 2
        while i >= 0 and j >= 0:
            c1, c2 = self.s1[i], self.s2[j]
            curr = self.steps[i][j]
            m = curr.get_min()

            if curr.deletion == m:
                ops.append("delete")
                i -= 1
            elif curr.insertion == m:
                ops.append("insert")
                j -= 1
            elif curr.substitution == m:
                ops.append("substitute")
                i, j = i - 1, j - 1
        print(ops)
        i, j = 0, 0
        while len(ops) > 0:
            c1, c2 = self.s1[i], self.s2[j]
            op = ops.pop()
            if op == "delete":
                i += 1
                c2 = "*"
            elif op == "insert":
                j += 1
                c1 = "*"
            else:
                i, j = i + 1, j + 1
            print(f"{op}: {c1} {c2}")


med = MinimumEditDistanceAndAlignment("intention", "execution", s_cost=2)
med.print_grid()
med.print_alignment()
