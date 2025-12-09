from math import sqrt

junc_boxes = []

with open("input.txt") as file:
    for line in file:
        junc_boxes.append(tuple((line.strip().split(','))))

distances = [] # a list of sets

n = len(junc_boxes)

for i in range(n):
    x1, x2, x3 = map(int, junc_boxes[i])

    for j in range(i + 1, n):
        y1, y2, y3 = map(int, junc_boxes[j])

        d = sqrt(
                (x1 - y1)**2 +
                (x2 - y2)**2 +
                (x3 - y3)**2
                )
        distances.append((d, i, j))
 
distances.sort(key=lambda t: t[0]) # sort the list based on distance (0th value of each tuple)

circuits = []
connections = 0

for _, a, b in distances:
    s1 = s2 = None
    
    for s in circuits:
        if a in s and s1 is None:
            s1 = s
        if b in s and s2 is None:
            s2 = s

    if s1 and s2:
        if s1 is not s2:
            s1.update(s2)
            circuits.remove(s2)
    elif s1:
        s1.add(b)
    elif s2:
        s2.add(a)
    else:
        circuits.append({a, b})
    
    if len(circuits[0]) == 1000 and len(circuits) == 1:
        last1 = a
        last2 = b
        break

x_product = int(junc_boxes[a][0]) * int(junc_boxes[b][0])

print("Product of x coordinates of last two junction boxes:", x_product)
