banks = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        banks.append(line)

# ----------------------------

joltages_easy = []

for each in banks:
    batteries = list(map(int, str(each)))

    max_jolt = 0
    
    for i in range(len(batteries)):
        for j in range(len(batteries)):

            if not i < j:
                continue
            
            jolt = (10 * batteries[i]) + batteries[j]

            if jolt > max_jolt:
                max_jolt = jolt

    joltages_easy.append(max_jolt)


print("Sum of 2 jolatages from all banks:", sum(joltages_easy))

