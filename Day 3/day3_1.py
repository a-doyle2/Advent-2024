import re

sum = 0

with open("Day 3/3.txt", "r") as f:
    for line in f.readlines():
        for mult in re.findall("mul\\(\\d+,\\d+\\)", line):
            expr = 1
            for num in re.findall("\\d+", mult):
                expr *= int(num)
        
            sum += expr

print(sum)