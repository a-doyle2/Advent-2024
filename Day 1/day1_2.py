list1, list2 = [], []

with open("Day 1/1.txt", "r") as f:
    for line in f.readlines():
        nums = [int(i) for i in line.strip().split("   ")]
        list1.append(nums[0])
        list2.append(nums[1])

list2.sort()
sum = 0

for i in list1:
    if i not in list2:
        continue
    sum += i * (max([idx for idx, _ in enumerate(list2) if _ == i] + [0]) - (list2.index(i) if i in list2 else 0) + 1)

print(sum)