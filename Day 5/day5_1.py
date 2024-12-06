import regex as re

rules = []
valid = []
def index(list, obj):
    return (list.index(obj) if obj in list else 1e9)

with open("Day 5/5.txt", "r") as f:
    ruleMode = True

    for line in f.readlines():
        if line.strip() == "":
            ruleMode = False
            continue
        
        if ruleMode:
            rules.append(re.findall("\\d+", line))
        if not ruleMode:
            updates = line.strip().split(",")
            invalid = False

            for rule in rules:
                if not ((rule[1] in updates and rule[0] not in updates) or index(updates, rule[0]) <= index(updates, rule[1])):
                    invalid = True
                    # print(rule, line)
                    break

            if not invalid:
                valid.append(updates)


sum = 0
for update in valid:
    sum += int(update[int(len(update)/2)])

print(sum)