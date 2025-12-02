products = open("day2/input.txt").read().strip().split(",")
print("Part 1: ", sum(p for prod_range in products for start, end in [map(int, prod_range.split("-"))] for p in range(start, end + 1) if len(s := str(p)) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]))
print("Part 2: ",sum(p for prod_range in products for start, end in [map(int, prod_range.split("-"))] for p in range(start, end + 1) if (s := str(p)) and any(s[:l] * (len(s) // l) == s for l in range(1, len(s)) if len(s) % l == 0)))
