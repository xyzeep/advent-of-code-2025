from functools import cache

data = open("input.txt").read()
links = {
    f: ts.split()
    for line in data.splitlines()
    if line.strip() and (f := line.split(": ", 1)[0]) and (ts := line.split(": ", 1)[1])
}


@cache
def count(pos, target):
    return 1 if pos == target else sum(count(n, target) for n in links.get(pos, []))


print("Part 1:", count("you", "out"))
p2 = count("svr", "fft") * count("fft", "dac") * count("dac", "out")
p2 += count("svr", "dac") * count("dac", "fft") * count("fft", "out")
print("Part 2:", p2)

# Credit: bob.oblong on discord
