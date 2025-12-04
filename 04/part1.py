initial_grid = []

with open("input.txt", "r") as file:

    for line in file:
        initial_grid.append(line.strip())
        
# -------------------------------

def valid_roll(row, col):
    neighbor_count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue

            if (i < 0) or (i > len(initial_grid) - 1) or (j < 0) or (j > len(initial_grid[i]) - 1):
                continue

            if initial_grid[i][j] == '@':
                neighbor_count += 1

    return neighbor_count < 4

# -------------------------------

rolls_count = 0
for i in range(len(initial_grid)):
    for j in range(len(initial_grid[i])):
        if initial_grid[i][j] == '@' and valid_roll(i, j):
            rolls_count += 1

print("Number of rolls accessible by the fork lift:", rolls_count)
