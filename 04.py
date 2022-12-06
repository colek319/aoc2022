from lib.lib import readfile, shrink_whitespace
from parse import parse

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
    while io_stack:
        level = io_stack.pop()
        for c in range(0, len(level), 4):
            crate = level[c+1]
            if crate == ' ':
                continue
            index = (c // 4) + 1
            crate_map[index].append(crate)

    parse_template = 'move {} from {} to {}'
    for movement in movements:
        res = parse(parse_template, movement)
        count = int(res[0])
        source_crate = int(res[1])
        target_crate = int(res[2])
        for _ in range(count):
            crate_map[target_crate].append(crate_map[source_crate].pop())

    output = ''
    for cs in crate_map.values():
        output += cs[-1]
    print(output)


def part2():
    lines = readfile('04')
    io_stack = []
    movements = []
    read_stacks = True
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
    while io_stack:
        level = io_stack.pop()
        for c in range(0, len(level), 4):
            crate = level[c+1]
            if crate == ' ':
                continue
            index = (c // 4) + 1
            crate_map[index].append(crate)

    parse_template = 'move {} from {} to {}'
    for movement in movements:
        res = parse(parse_template, movement)
        count = int(res[0])
        source_crate = int(res[1])
        target_crate = int(res[2])
        stack_height = len(crate_map[source_crate])
        crate_map[target_crate].extend(crate_map[source_crate][stack_height - count:])
        crate_map[source_crate] = crate_map[source_crate][:stack_height - count]

    output = ''
    for cs in crate_map.values():
        output += cs[-1]
    print(output)

if __name__ == '__main__':
    part1()
    part2()