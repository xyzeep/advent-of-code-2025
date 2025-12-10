red_tiles = []
green_tiles = []

with open("small.txt", "r") as file:
    for line in file:
        red_tiles.append(line.strip().split(','))

n = len(red_tiles)

print(red_tiles)

for i in range(n):
    tile1 = red_tiles[i]

    for j in range(i, n):
        tile2 = red_tiles[j]

        col_match = row_match = None

        if tile1[0] == red_tiles[j][0]: col_match = red_tiles[i][0]
        if tile1[1] == red_tiles[j][1]: row_match = red_tiles[i][1]
        
        if col_match is not None:
           for k in range(int(tile1[1]), int(tile2[1]) + 1):
                green_tiles.append([col_match, k])
        
        elif row_match is not None:
            for k in range(int(tile1[0]), int(tile2[0]) + 1):
                green_tiles.append([k, row_match])

for i in range(n):
    x1, y1 = map(int, red_tiles[i])
    x2, y2 = map(int, red_tiles[(i + 1) % n]) 

    # vertical segment
    if x1 == x2:
        start = min(y1, y2)
        end   = max(y1, y2)
        for y in range(start, end + 1):
            green_tiles.append((x1, y))

    elif y1 == y2:
        start = min(x1, x2)
        end   = max(x1, x2)
        for x in range(start, end + 1):
            green_tiles.append((x, y1))



largest_area = 0

red_set = set((int(x), int(y)) for x, y in red_tiles)
green_set = set((x, y) for x, y in green_tiles)

for i in range(n):
    x1, y1 = map(int, red_tiles[i])

    for j in range(i + 1, n):
        x2, y2 = map(int, red_tiles[j])

        left   = min(x1, x2)
        right  = max(x1, x2)
        bottom = min(y1, y2)
        top    = max(y1, y2)

        valid = True
        for x in range(left, right + 1):
            for y in range(bottom, top + 1):
                if (x, y) not in red_set and (x, y) not in green_set:
                    valid = False
                    break
            if not valid:
                break

        if not valid:
            continue

        area = (right - left + 1) * (top - bottom + 1)

        if area > largest_area:
            largest_area = area

print(largest_area)
