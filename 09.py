from lib.lib import readlines

def part1(src):
    cycle_num = 1
    signal_map = {}
    X = 1
    for line in src:
        if line.startswith('noop'):
            cycle_num += 1
            handle_step1(cycle_num, X, signal_map)
        elif line.startswith('addx'):        
            cycle_num += 1
            handle_step1(cycle_num, X, signal_map)
            cycle_num += 1
            _, v = line.split(' ')
            X += int(v)              
            handle_step1(cycle_num, X, signal_map)          
    print(sum(signal_map.values()))

def handle_step1(cycle_num, X, signal_map):
    if (cycle_num - 20) % 40 == 0:
        # print(X, cycle_num)
        signal_map[cycle_num] = cycle_num * X   

def part2(src):
    cycle = 0
    crt = [['.']* 40 for i in range(6)]
    crt[0][0] = '#' # init CRT
    X = 1
    for line in src:
        if line.startswith('noop'):
            cycle += 1
            handle_step2(cycle, X, crt)
        elif line.startswith('addx'):
            cycle += 1
            handle_step2(cycle, X, crt)
            cycle += 1
            _, v = line.split(' ')
            X += int(v)
            handle_step2(cycle, X, crt) 
    printcrt(crt)
    

def handle_step2(cycle, X, crt):
    # draw
    sprite_locs = [i for i in range(X - 1, X + 2, 1) if i >= 0 and i < 40] # get sprite locations
    row_cycle = cycle // 40 # get which row the cycle is in
    col_cycle = cycle % 40 # get which column the cycle is in    
    print(X, col_cycle)
    for loc in sprite_locs:
        if loc == col_cycle:
            crt[row_cycle][loc] = '#'

def printcrt(crt):
    for row in crt:
        print(''.join(row))

if __name__ == '__main__':
    src = readlines('09')
    part1(src)
    part2(src)