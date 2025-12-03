banks = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        banks.append(line)

# ----------------------------

joltages = []

for each in banks:
    batteries = list(map(int, str(each)))

    max_values = []
    to_remove = len(batteries) - 12

    for num in batteries:
        while max_values and to_remove > 0 and max_values[-1] < num:
            max_values.pop()
            to_remove -= 1
        max_values.append(num)

    max_jolt = int("".join(map(str, max_values[:12])))

    joltages.append(max_jolt)

print("Total Joltage:", sum(joltages))

    



