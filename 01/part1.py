lines = []

with open("input.txt", "r") as file:
    zero_count = 0
    state = 50

    for line in file:
        line = line.strip()
        lines.append(line)
        
zero_count = 0
state = 50

for line in lines:
    direction = line[0]
    magnitude = int(line[1:])
    
    if magnitude > 99:
        magnitude %= 100

    if direction == 'L':
        state -= magnitude
    elif direction == 'R':
        state += magnitude
    
    if state < 0:
        state = 100 + state
    elif state > 99:
        state = state - 100

    if state == 0:
        zero_count += 1

print("Number of times the dial stops at zero is", zero_count)  
