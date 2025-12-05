with open("input.txt", "r") as file:
    data = file.read().strip()

ranges_data, ingre_data = data.split("\n\n")

ranges = []

for line in ranges_data.splitlines():
    start, end = map(int, line.split("-"))
    ranges.append((start, end))

ranges.sort()

ingre = [int(x) for x in ingre_data.splitlines()]

# ------------------------------------------------
# Part 1:

fresh_ingres = set()

for each in ingre:
    fresh = False

    for s, e in ranges:
        if s <= each <= e:
            fresh = True

    if fresh:
        fresh_ingres.add(each)

print("Number of available fresh ingredients:", len(fresh_ingres))

# ------------------------------------------------
# Part 2:

all_fresh_count = 0
c_s, c_e = ranges[0]

for s, e in ranges[1:]:

    #  if overlapping ranges
    if s <= c_e + 1:
        c_e = max(c_e, e)

    # add and change current_start and current_end if not
    else:
        all_fresh_count += c_e - c_s + 1
        c_s, c_e = s, e

all_fresh_count += c_e - c_s + 1

print("Number of all fresh ingredients:", all_fresh_count)

