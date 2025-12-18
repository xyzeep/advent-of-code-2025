red_tiles = []
with open("input.txt", "r") as file:
    for line in file:
        red_tiles.append(line.strip().split(","))

largest = 0
n = len(red_tiles)
for i in range(n):
    for j in range(i, n):
        col_diff = abs(int(red_tiles[i][0]) - int(red_tiles[j][0])) + 1
        row_diff = abs(int(red_tiles[i][1]) - int(red_tiles[j][1])) + 1
        area = col_diff * row_diff
        if area > largest:
            largest = area

print(largest)
