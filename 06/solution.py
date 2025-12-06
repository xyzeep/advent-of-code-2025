from math import prod

lines = []
with open("input.txt", "r") as file:
    for line in file:
        lines.append(line.split())


# Part 1:

answers1 = []
for i in range(len(lines[0])):

    symbol = lines[4][i]
    
    if symbol == '*':
        answer = 1
        for j in range(4):
            answer *= int(lines[j][i])

    if symbol == '+':
        answer = 0
        for j in range(4):
            answer += int(lines[j][i])

    answers1.append(answer)
print("Part 1 answer:", sum(answers1))
