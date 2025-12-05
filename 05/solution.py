with open("input.txt", "r") as file:
    data = file.read().strip()

ranges_data, ingre_data = data.split("\n\n")

ranges = []

for line in ranges_data.splitlines():
    start, end = map(int, line.split("-"))
    ranges.append((start, end))

ingre = [int(x) for x in ingre_data.splitlines()]

# ------------------------------------------------

fresh_ingres = set()

for each in ingre:
    fresh = False

    for s, e in ranges:
        if s <= each <= e:
            fresh = True

    if fresh:
        fresh_ingres.add(each)

print(len(fresh_ingres))

    



