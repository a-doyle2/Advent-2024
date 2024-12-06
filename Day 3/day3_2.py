import regex as re

sum = 0

with open("Day 3/3.txt", "r") as f:
    enabled = True

    for line in f.readlines():
        instructions = re.findall("mul\\(\\d+,\\d+\\)|don't\\(\\)|do\\(\\)", line)

        for instruction in instructions:
            if instruction == "do()":
                enabled = True
                continue
            elif instruction == "don't()":
                enabled = False
                continue

            if enabled:
                expr = 1
                for num in re.findall("\\d+", instruction):
                    expr *= int(num)
            
                sum += expr

print(sum)