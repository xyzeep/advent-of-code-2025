import re
import time

machines = []
with open("input.txt", "r") as file:
    for line in file:
        machines.append(line.strip())
LD = []
BTNS = []
JR = []
for machine in machines:
    ld_match = re.findall(r"\[(.*?)\]", machine)[0]  # get inside brackets
    LD.append(ld_match)

    btn_strings = re.findall(r"\(.*?\)", machine)
    btn_tuples = [tuple(map(int, s.strip("()").split(","))) for s in btn_strings]
    BTNS.append(btn_tuples)
    JR.append(re.findall(r"\{.*?\}", machine))


def pushBtn(button, light_diagram):
    new_ld = list(light_diagram)
    for pos in button:
        new_ld[pos] = "." if new_ld[pos] == "#" else "#"
    return "".join(new_ld)


start = time.time()
minimum_presses = []
for i in range(len(machines)):
    n = len(LD[i])
    initial_state = "." * n
    queue = [(initial_state, 0)]
    explored = {initial_state}
    goal = LD[i]
    while queue:
        current_state, path_cost = queue.pop(0)
        explored.add(current_state)
        if current_state == goal:
            break
        for button in BTNS[i]:
            new_state = pushBtn(button, current_state)
            if new_state not in explored:
                explored.add(new_state)
                queue.append((new_state, path_cost + 1))
    if current_state == goal:
        minimum_presses.append(path_cost)
    else:
        print("No solution found for machine #", i)

end = time.time()
print("time_taken:", end - start, "seconds.")
print("answer to part 1:", sum(minimum_presses))
