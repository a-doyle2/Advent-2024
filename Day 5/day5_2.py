import regex as re

rules = []
incorrect = []
def index(list, obj):
    return (list.index(obj) if obj in list else 1e9)

def check(updates, rules):
    for rule in rules:
        if not ((rule[1] in updates and rule[0] not in updates) or index(updates, rule[0]) <= index(updates, rule[1])):
            return rule

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

            if invalid:
                incorrect.append(updates)

correct = []
for updates in incorrect:
    while (wrong := check(updates, rules)) is not None:
        updates.remove(wrong[0])
        updates = [wrong[0]] + updates
    correct.append(updates)


sum = 0
for update in correct:
    sum += int(update[int(len(update)/2)])

print(sum)