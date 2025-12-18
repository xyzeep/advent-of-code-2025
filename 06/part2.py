from math import prod

lines = []
with open("input.txt") as file:
    for line in file:
        lines.append(line.rstrip("\n"))
operations = lines.pop().replace(" ", "")

answers = []
sym_idx = -1
columns = []
for col in reversed(range(len(lines[0]))):
    column = []
    for row in range(len(lines)):
        column.append(lines[row][col])
    if column.count(" ") == len(lines):
        if operations[sym_idx] == "*":
            answers.append(prod(columns))
        elif operations[sym_idx] == "+":
            answers.append(sum(columns))
        sym_idx -= 1
        columns = []
        continue
    digits = [c for c in column if c != " "]
    number = int("".join(digits))
    columns.append(number)
if operations[sym_idx] == "*":
    answers.append(prod(columns))
elif operations[sym_idx] == "+":
    answers.append(sum(columns))

print(sum(answers))
