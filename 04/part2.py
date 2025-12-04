grid = []

with open("input.txt", "r") as file:
    for line in file:
        grid.append(line.strip())
        
# -------------------------------

def valid_roll(row, col):
    neighbor_count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue

            if (i < 0) or (i > len(grid) - 1) or (j < 0) or (j > len(grid[i]) - 1):
                continue

            if grid[i][j] == '@':
                neighbor_count += 1

    return neighbor_count < 4

# -------------------------------

def revise_grid(to_remove):
    for i, j in to_remove:
        grid[i] = grid[i][:j] + '.' + grid[i][j + 1:]

# -------------------------------

rolls_count = 0
stopped = False

while not stopped:
    stopped = True
    to_remove = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@' and valid_roll(i, j):
                rolls_count += 1
                stopped = False
                to_remove.append((i, j))
    
                revise_grid(to_remove)

print("Number of removable rolls in total:", rolls_count)
