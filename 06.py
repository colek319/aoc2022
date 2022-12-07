from lib.lib import readfile, readlines
from parse import parse
import sys

directories = {}
dir_sizes = {}
seen_dirs = set()

cd_template = '$ cd {}'

def part1():
    lines = readlines('06')
    curr_dir = []
    for line in lines:
        if line.startswith('$ cd'):
            arg = parse(cd_template, line)[0]
            if arg == '..':
                curr_dir.pop()
            elif arg == '/':
                curr_dir = []
            else:
                # cd to a directory I guess
                curr_dir.append(arg)
        elif line.startswith('$ ls'):
            continue
        else:
            # must be listing files
            o1, o2 = line.split(' ')
            curr_dir_str = '/'.join(curr_dir)
            dir_contents = directories.get(curr_dir_str, {'dirs': [], 'files': []})
            if o1 == 'dir':
                # directory
                dir_contents['dirs'].append(o2)
            else:
                # files is a list of tuples (filename, size)
                dir_contents['files'].append((o2, o1))
            directories[curr_dir_str] = dir_contents

    for f in directories:
        dir_sizes[f] = calculuate_dir_size(f)
    
    total = 0
    for _, size in dir_sizes.items():
        if size <= 100000:
            total += size
    print(total)

def part2():
    MAXSPACE = 70000000
    space_used = 0
    for contents in directories.values():
        for _, size in contents['files']:
            size = int(size)
            space_used += size
    space_remaining = MAXSPACE - space_used
    needed = 30000000 - space_remaining

    chosen_size = sys.maxsize
    for d, size in dir_sizes.items():
        if size > needed:
            if size < chosen_size:
                chosen_size = size
    print(chosen_size)

def calculuate_dir_size(dirname):
    if dirname in seen_dirs:
        return dir_sizes[dirname]
    seen_dirs.add(dirname)
    size = 0
    contents = directories[dirname]
    for d in contents['dirs']:
        subdir = dirname + '/' + d if dirname else d
        size += calculuate_dir_size(subdir)
    for _, s in contents['files']:
        size += int(s)
    dir_sizes[dirname] = size
    return size

if __name__ == '__main__':
    part1()
    part2()