from lib.lib import readfile, shrink_whitespace

def part1():
    lines = readfile('04')
    io_stack = []
    movements = []
    read_stacks = True
    stack_lines = 0
    for line in lines:
        if line == '':
            read_stacks = False
            continue
        if read_stacks:
            io_stack.append(line)
        else:
            movements.append(line)
    
    # process inputs
    indices = shrink_whitespace(io_stack.pop()).split(' ')
    crate_map = {int(index): [] for index in indices}
    print(crate_map)
    while io_stack:
        level = io_stack.pop()
        for c in range(0, len(level), 4):
            crate = level[c+1]
            index = (c // 4) + 1
            crate_map[index].append(crate)
    print(crate_map)


def part2():
    lines = readfile('04')
    for line in lines:
        continue

if __name__ == '__main__':
    part1()
    part2()