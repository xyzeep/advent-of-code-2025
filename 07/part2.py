grid = []
with open("input.txt", "r") as file:
    for line in file:
        grid.append(line.strip())

s_pos = (0, grid[0].index('S'))
s_row = s_pos[0] + 1
s_col = s_pos[1]

rows = len(grid)
cols = len(grid[0])

cell_mapping = {}

def count_timelines(row, col):

    if not (0 <= row < rows) or not (0 <= col < cols):
        return 1

    if (row, col) in cell_mapping:
        return cell_mapping[(row, col)]
    
    cell = grid[row][col]

    if cell == '.':
        return count_timelines(row + 1, col)

    elif cell == '^':
        left = 0
        right = 0
        
        left = count_timelines(row + 1, col - 1)
        right = count_timelines(row + 1, col + 1)

        timeline_count = left + right
        cell_mapping[(row, col)] = timeline_count

        return timeline_count

total_timelines = count_timelines(s_row, s_col)
print("Total timelines:", total_timelines)
