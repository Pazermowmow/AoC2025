with open("day2/input.txt") as f:
    products = f.read().strip().split(",")

def shortest_repeated_substring(s):
    n = len(s)
    
    for length in range(1, n + 1):
        if n % length == 0:
            pattern = s[:length]
            if pattern * (n // length) == s:
                return pattern
    return s

p1 = 0
for prod_range in products:
    start, end = map(int, prod_range.split("-"))
    
    for p in range(start, end + 1):
        p_str = str(p)
        if len(p_str) % 2 != 0:
            continue

        first_half = p_str[:len(p_str)//2]
        second_half = p_str[len(p_str)//2:]

        if first_half == second_half:
            p1 += p

print(p1)

p2 = 0
for prod_range in products:
    start, end = map(int, prod_range.split("-"))

    for p in range(start, end + 1):
        p_str = str(p)
        srs = shortest_repeated_substring(p_str)
        if srs == p_str:
            continue

        p2 += p

print(p2)
