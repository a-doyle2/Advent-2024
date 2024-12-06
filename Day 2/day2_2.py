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
            # print(report)
            continue
      
    for mod_report in [report[:i]+report[i+1:] for i in range(len(report))]:
        if all(sorted(mod_report)[i] == mod_report[i] for i in range(len(mod_report))) or \
            all(sorted(mod_report)[i] == list(reversed(mod_report))[i] for i in range(len(mod_report))):
            dists = [abs(x - y) for x, y in zip(mod_report[1:], mod_report[:-1])]
            # print(dists, report, mod_report)

            if min(dists) >= 1 and max(dists) <= 3:
                safe += 1
                break

print(safe)