with open("day4/input.txt") as f:
    data = [list(i.strip()) for i in f.read().split("\n")]

# Part 1
accessible = 0
for i, row in enumerate(data):
    for j, pos in enumerate(row):
        if pos == ".":
            continue
        
        surrounding = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                
                ni, nj = i + di, j + dj
                if 0 <= ni < len(data) and 0 <= nj < len(row):
                    if data[ni][nj] == "@":
                        surrounding += 1
        if surrounding < 4:
            accessible += 1

print(accessible)

# Part 2
total_accessible = 0
while True:
    new_accessible = 0
    for i, row in enumerate(data):
        for j, pos in enumerate(row):
            if pos == ".":
                continue
            
            surrounding = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(data) and 0 <= nj < len(row):
                        if data[ni][nj] == "@":
                            surrounding += 1
            if surrounding < 4:
                new_accessible += 1
                total_accessible += 1
                row[j] = "."
    if new_accessible == 0:
        break


print(total_accessible)
