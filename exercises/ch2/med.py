class MinimumEditDistance:
    def __init__(self, s1: str, s2: str, d_cost=1, i_cost=1, s_cost=1):
        self.s1, self.s2 = s1, s2
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

    def get_grid(self):
        out = "   #  "
        for j in range(len(self.grid[-1]) - 1):
            out += f"{self.s2[j]}  "
        out += r"\n"
        for i in range(len(self.grid)):
            if i == 0:
                out += "#  "
            else:
                out += f"{self.s1[i - 1]}  "
            for j in range(len(self.grid[-1])):
                end = " " if self.grid[i][j] / 10 >= 1 else "  "
                out += f"{self.grid[i][j]}{end}"
            out += r"\n"
        return out


class Step:
    def __init__(self, init):
        self.insertion = init
        self.deletion = init
        self.substitution = init

    def get_min(self):
        return min(self.insertion, self.deletion, self.substitution)


class MinimumEditDistanceAndAlignment(MinimumEditDistance):
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

    def get_alignment(self):
        ops = []
        i, j = len(self.steps) - 1, len(self.steps[0]) - 1
        while i >= 0 and j >= 0:
            if i == 0 and j == 0:
                break
            curr = self.steps[i][j]
            m = curr.get_min()

            if curr.substitution == m:
                ops.append("substitute")
                i, j = i - 1, j - 1
            elif curr.insertion == m:
                ops.append("insert")
                j -= 1
            elif curr.deletion == m:
                ops.append("delete")
                i -= 1

        i, j = 0, 0
        out = ""
        while len(ops) > 0:
            if i < len(self.s1):
                c1 = self.s1[i]
            if j < len(self.s2):
                c2 = self.s2[j]
            op = ops.pop()
            if op == "insert":
                j += 1
                c1 = "*"
            elif op == "delete":
                i += 1
                c2 = "*"
            else:
                i, j = i + 1, j + 1

            if c1 != c2:
                out += f"{c1} {c2} <- {op}"
                out += r"\n"
            else:
                out += f"{c1} {c2}"
                out += r"\n"
        return out
