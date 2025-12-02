import re
import time

easy_pattern = re.compile(r"^(\d+)\1$")
hard_pattern = re.compile(r"^(\d+)\1+$")

with open('input.txt', 'r') as file:
    line = file.readline()
    id_ranges = line.split(',')

# -------------------------------

# Easy = Part 1
# Hard = Part 2

t_s = time.perf_counter()

invalid_ids_easy = []
invalid_ids_hard = []

for each in id_ranges:
    id_range = each.split('-')
    start = id_range[0]
    end = id_range[1]

    for i in range (int(start), int(end) + 1):
        if easy_pattern.match(str(i)):
            invalid_ids_hard.append(i)
        if hard_pattern.match(str(i)):
            invalid_ids_soft.append(i)

easy_sum = sum(invalid_ids_soft)
hard_sum = sum(invalid_ids_hard)

t_e = time.perf_counter()
print("Time:", (t_e - t_s) * 1000, "ms")

print("The sum of invalid IDs (easy) is:", easy_sum)
print("The sum of invalid IDs (hard) is:", hard_sum)
