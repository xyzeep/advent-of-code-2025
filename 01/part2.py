lines = []

with open("input.txt", "r") as file:
    zero_count = 0
    state = 50

    for line in file:
        line = line.strip()
        lines.append(line)

# ------------------------------

zero_count = 0
state = 50

for line in lines:
    direction = line[0]  # 'L' or 'R'
    magnitude = int(line[1:])  # some integer

    if magnitude > 99:
        zero_count += int(magnitude / 100)
        magnitude %= 100

    if direction == 'L':
        new_state = state - magnitude
    elif direction == 'R':
        new_state = state + magnitude

    if new_state < 0:
        new_state = 100 + new_state
    elif new_state > 99:
        new_state = new_state - 100

    if direction == 'L' and new_state > state and state != 0:
        zero_count += 1
    
    elif direction == 'R' and new_state < state and new_state != 0:
        zero_count += 1

    if new_state == 0:
        zero_count += 1

    state = new_state

print("Number of times the dial points at zero is", zero_count)
