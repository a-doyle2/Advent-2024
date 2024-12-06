list1, list2 = [], []

with open("Day 1/1.txt", "r") as f:
    for line in f.readlines():
        nums = [int(i) for i in line.strip().split("   ")]
        list1.append(nums[0])
        list2.append(nums[1])

list1.sort()
list2.sort()
sum = 0

for idx, i in enumerate(list1):
    sum += abs(list1[idx] - list2[idx])

print(sum)