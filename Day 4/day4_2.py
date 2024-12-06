M = []
A = []
S = []

with open("Day 4/4.txt", "r") as f:
    for y_idx, line in enumerate(f.readlines()):
        for x_idx, char in enumerate(line):
            if char == "M":
                M.append((x_idx, y_idx))
            if char == "A":
                A.append((x_idx, y_idx))
            if char == "S":
                S.append((x_idx, y_idx))

words = 0

for a in A:
    x = a[0]
    y = a[1]

    # left
    if (x-1, y-1) in M and (x-1, y+1) in M and (x+1, y-1) in S and (x+1,y+1) in S:
        words += 1
    # right
    if (x-1, y-1) in S and (x-1, y+1) in S and (x+1, y-1) in M and (x+1,y+1) in M:
        words += 1
    # down
    if (x-1, y+1) in M and (x+1, y+1) in M and (x-1, y-1) in S and (x+1, y-1) in S:
        words += 1
    # up
    if (x-1, y+1) in S and (x+1, y+1) in S and (x-1, y-1) in M and (x+1, y-1) in M:
        words += 1
    
print(words)