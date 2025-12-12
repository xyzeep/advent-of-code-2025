rack = {}
devices = set()

with open("input.txt", "r") as file:
    for x in file:
        line = x.strip().split()
        device = line[0][:-1]
        devices.add(device)

        outputs = line[1:]
        rack[device] = outputs

devices = list(devices)

# ---------------------------------

start_device = "you"
end_device = "out"

stack = []

for each in rack["you"]:
    stack.append([each, ["you", each]])

all_paths = []

while stack:
    current_device, path_so_far = stack.pop()

    current_outputs = rack[current_device]

    for co in current_outputs:
        if co == end_device:
            all_paths.append(path_so_far + ["out"])

        elif co not in path_so_far:
            new_path = path_so_far + [co]
            stack.append([co, new_path])

print(len(all_paths))



