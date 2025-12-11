
# PLEASE DO NOT FOLLOW THIS SOLUTION; THIS SOLUTION IS INCOMPLETE

from collections import deque

red_tiles = []
green_tiles = set()

with open("input.txt", "r") as file:
    for line in file:
        x, y = line.strip().split(',')
        red_tiles.append((int(x), int(y)))

largest = 0
n = len(red_tiles)

print("stuck here 1")
for i in range(n):
    tile1 = red_tiles[i]
    tile2 = red_tiles[(i + 1) % n]  

    if tile1[0] == tile2[0]:  
        col = tile1[0]
        for row in range(min(tile1[1], tile2[1]) + 1, max(tile1[1], tile2[1])):
            green_tiles.add((col, row))
    elif tile1[1] == tile2[1]:  
        row = tile1[1]
        for col in range(min(tile1[0], tile2[0]) + 1, max(tile1[0], tile2[0])):
            green_tiles.add((col, row))

# filling the green tiles
wall = set(red_tiles) | green_tiles

xs = [x for x, _ in wall]
ys = [y for _, y in wall]

min_x, max_x = min(xs) - 2, max(xs) + 2
min_y, max_y = min(ys) - 2, max(ys) + 2


start = (min(xs) -1 , min(ys) - 1) 
outside = set([start])
queue = deque([start])

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

print("stuck here 2")
hope = 0
while queue:
    print(hope)
    hope += 1
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx , y + dy

        if nx < min_x or nx > max_x or ny < min_y or ny > max_y:
            continue

        if (nx, ny) in wall:
            continue

        if (nx, ny) not in outside:
            outside.add((nx, ny))
            queue.append((nx, ny))

largest = 0
for i in range(n):
    tile1 = red_tiles[i]
    col1 = int(tile1[0])
    row1 = int(tile1[1])
    for j in range(i, n):
        tile2 = red_tiles[j]
        col2 = int(tile2[0])
        row2 = int(tile2[1])

        col_step = 1
        row_step = 1

        if col1 > col2: col_step = -1
        if row1 > row2: row_step = -1

        left = min(col1, col2)
        right = max(col1, col2)
        top = min(row1, row2)
        bottom = max(row1, row2)       
    
        valid = True
        for col in range(left, right+1):
            for row in range(top, bottom+1):
                if (col, row) in outside:
                    valid = False
                    break
            if not valid:
                break

    if valid:
        col_diff = abs(int(red_tiles[i][0]) - int(red_tiles[j][0])) + 1
        row_diff = abs(int(red_tiles[i][1]) - int(red_tiles[j][1])) + 1
    
        area = col_diff * row_diff
        if area > largest: largest = area

print(largest)
