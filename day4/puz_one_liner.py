with open("day4/input.txt") as f:
    text = [list(i.strip()) for i in f.read().split("\n")]

# Part 1
print((lambda data: sum(1 for i, row in enumerate(data) for j, pos in enumerate(row) if pos == "@" and sum(1 for di in [-1, 0, 1] for dj in [-1, 0, 1] if (di != 0 or dj != 0) and 0 <= i + di < len(data) and 0 <= j + dj < len(row) and data[i + di][j + dj] == "@") < 4))([list(line) for line in text]))

# Part 2
print((f := lambda d, t=0: t if not (r := [(i, j) for i, row in enumerate(d) for j, v in enumerate(row) if v == "@" and sum(1 for di in [-1, 0, 1] for dj in [-1, 0, 1] if (di or dj) and 0 <= i + di < len(d) and 0 <= j + dj < len(row) and d[i + di][j + dj] == "@") < 4]) else f([["." if (i, j) in r else c for j, c in enumerate(row)] for i, row in enumerate(d)], t + len(r)))([list(line) for line in text]))
