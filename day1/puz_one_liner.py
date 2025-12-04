from itertools import accumulate

INPUT = open("day1/input.txt").read().strip()
LINES = INPUT.split("\n")


def p1():
    return sum(pos == 0 for pos in accumulate(LINES, lambda s, l: (s - int(l[1:]) if l[0] == 'L' else s + int(l[1:])) % 100, initial=50))

def p2():
    return sum(abs(divmod(s - int(l[1:]), 100)[0]) + (1 if s > 0 and divmod(s - int(l[1:]), 100)[1] == 0 else 0) - (1 if s == 0 and divmod(s - int(l[1:]), 100)[1] > 0 else 0) if l[0] == 'L' else divmod(s + int(l[1:]), 100)[0] for s, l in zip(accumulate(LINES, lambda s, l: (divmod(s - int(l[1:]), 100)[1] if l[0] == 'L' else divmod(s + int(l[1:]), 100)[1]), initial=50), LINES))


if __name__ == "__main__":
    print(f"part1={p1()}")
    print(f"part2={p2()}")
