reports = []

with open("Day 2/2.txt", "r") as f:
    for line in f.readlines():
        reports.append([int(i) for i in line.split(" ")])

safe = 0

for report in reports:
    if all(sorted(report)[i] == report[i] for i in range(len(report))) or \
       all(sorted(report)[i] == list(reversed(report))[i] for i in range(len(report))):
        dists = [abs(x - y) for x, y in zip(report[1:], report[:-1])]

        if min(dists) >= 1 and max(dists) <= 3:
            safe += 1

print(safe)