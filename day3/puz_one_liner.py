from functools import reduce

print("Part 1:", sum(int(str(max(b[:-1])) + str(max(b[max(range(len(b)-1), key=lambda x: b[x])+1:]))) for b in open("day3/input.txt").read().splitlines()))
print("Part 2:", sum(int("".join(reduce(lambda acc, i: (acc[0] + [max(seg := acc[1][: len(acc[1]) - (11 - i)] if i < 11 else acc[1])], acc[1][max(range(len(seg)), key=lambda x: seg[x]) + 1:]), range(12), ([], b))[0])) for b in open("day3/input.txt").read().splitlines()))
