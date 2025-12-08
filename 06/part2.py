from math import prod
import re

lines = []
with open("input.txt") as file:
    for idx, line in enumerate(file):
        line = line.rstrip('\n')
        if idx == 4:  # last row with operators
            # only '*' and '+'
            symbols = [c for c in line if c in '*+']
            lines.append(symbols)
        else:
            numbers = re.findall(r'\s*\d+', line)
            lines.append(numbers)

print(lines)

answers = []

for i in reversed(range(len(lines[0]))):
    for j in range(len(lines[0][i])):
        sym = lines[-1][i]

        column = [lines[row][i] for row in range(len(lines)-1)]
        digits = [''.join(c for c in s if c.isdigit()) for s in column]
        numbers = [int(d) for d in digits]

        if sym == '*':
            answer = prod(numbers)
        if sym == '+':
            answer = sum(numbers)

    answers.append(answer)

print("Part 2 solution:", sum(answers))

