X = []
M = []
A = []
S = []

with open("Day 4/4.txt", "r") as f:
    for y_idx, line in enumerate(f.readlines()):
        for x_idx, char in enumerate(line):
            if char == "X":
                X.append((x_idx, y_idx))
            if char == "M":
                M.append((x_idx, y_idx))
            if char == "A":
                A.append((x_idx, y_idx))
            if char == "S":
                S.append((x_idx, y_idx))

words = 0

for start in X:
    x = start[0]
    y = start[1]

    # left
    if (x+1, y) in M and (x+2, y) in A and (x+3, y) in S:
       words += 1
    # right
    if (x-1, y) in M and (x-2, y) in A and (x-3, y) in S:
        words += 1
    # up
    if (x, y-1) in M and (x, y-2) in A and (x, y-3) in S:
        words += 1
    # down
    if (x, y+1) in M and (x, y+2) in A and (x, y+3) in S:
        words += 1
    # upleft
    if (x+1, y-1) in M and (x+2, y-2) in A and (x+3, y-3) in S:
        words += 1
    # upright
    if (x-1, y-1) in M and (x-2, y-2) in A and (x-3, y-3) in S:
        words += 1
    # downleft
    if (x+1, y+1) in M and (x+2, y+2) in A and (x+3, y+3) in S:
        words += 1
    # downright
    if (x-1, y+1) in M and (x-2, y+2) in A and (x-3, y+3) in S:
        words += 1

print(words)