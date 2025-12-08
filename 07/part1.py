grid = []
with open("input.txt", "r") as file:
    for line in file:
        grid.append(line.strip())

s_pos = (0, grid[0].index('S'))
rows = len(grid)
cols = len(grid[0])

beams = {(s_pos[0] + 1, s_pos[1])}
splits = 0

iteration = 0
while iteration < rows:
    new_beams = set()

    for row, col in beams:
        if col < cols and row < rows:
            if grid[row][col] == '.':
                new_beams.add((row + 1, col))

            elif grid[row][col] == '^':
                splits += 1
                new_beams.add((row + 1, col - 1))
                new_beams.add((row + 1, col + 1))
        
    beams = new_beams
    iteration += 1

print("Total Splits:", splits)
