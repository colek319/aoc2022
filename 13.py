import os

TESTDIR = './days'

'''
Each line of inut indicates a veritical or horizontal line segment

When does sand start falling forever?

When it hits the last "horizontal" line of sand

Just check when we get past lowest point -> that must keep forever.

either it stops, and we add it to sand set, or we reach lowest point, and we halt program, 
returning amount of sand 
'''

class Day():
    def __init__(self, problem='problem', test_only=False):
        self.problem = problem
        self.test_only = test_only        
        self.answers = {}
        self.bookkeep() # define stateful variables in bookkeep

    def bookkeep(self):
        # declare vars here
        self.rocks = []
        self.rocks_set = set() # TODO: we should have just used a set tbh
        self.min_row = None
        self.max_row = None
        self.min_col = None
        self.max_col = None
        self.width = None
        self.depth = None
        self.start = (0, 500)
        self.sand = set()
        return

    def solve(self):
        for file in os.listdir(TESTDIR + '/' + self.problem):
            input_name = file.split('.')[0]
            if self.test_only and not 'test' in input_name:
                continue
            self.answers[input_name] = {'Part1': 'TODO', 'Part2': 'TODO'}

            # we separate solving and IO for p1/p2 here in case they handle input differently
            # part 1
            self.bookkeep()
            self._handle_input_part1(input_name)
            self.answers[input_name]['Part1'] = self._part1()

            # part 2
            self.bookkeep()
            self._handle_input_part2(input_name)
            self.answers[input_name]['Part2'] = self._part2()

    def _handle_input_part1(self, input_name):
        # handle input line for part 1 here
        with open(TESTDIR + '/' + self.problem + '/' + input_name + '.input', 'r') as fstream:
            # handle input for part 1
            self._handle_input(fstream)

    def _handle_input_part2(self, input_name):
        # handle input line for part 2 here
        with open(TESTDIR + '/' + self.problem + '/' + input_name + '.input', 'r') as fstream:
            # handle input for part 2
            self._handle_input(fstream)
        self.rockset = set(self.rocks)
        self.max_row + 2 # for this problem, we need to add 2 to max_row

    def _handle_input(self, fstream):
        # use this if part1 and part2 handle input the same way
        for line in fstream.read().splitlines():
            # read input here
            rocks = list(map(lambda p: (int(p[1]), int(p[0])), (point.split(',') for point in line.split(' -> '))))
            for i in range(len(rocks) - 1):
                first, second = rocks[i], rocks[i + 1]
                if first[0] == second[0]:
                    # vertical line
                    start = min(first[1], second[1])
                    stop = max(first[1], second[1]) + 1
                    for y in range(start, stop):
                        self.rocks.append((first[0], y))
                else:
                    # horizontal line
                    start = min(first[0], second[0])
                    stop = max(first[0], second[0]) + 1
                    for x in range(start, stop):
                        self.rocks.append((x, first[1]))
        self.rocks = list(set(self.rocks))
        # find lowest point
        self.min_row = 0
        self.max_row = max(self.rocks, key=lambda x: int(x[0]))[0] + 1
        self.min_col = min(self.rocks, key=lambda x: int(x[1]))[1] - 1
        self.max_col = max(self.rocks, key=lambda x: int(x[1]))[1] + 1
        self.width = self.max_col - self.min_col + 1
        self.depth = self.max_row - self.min_row + 1
        self.cave_wall = [[0 for _ in range(self.width)] for _ in range(self.depth)]

        # add rocks to cave wall
        for rock in self.rocks:
            rock_row, rock_col = self.relative_position(rock)
            self.cave_wall[rock_row][rock_col] = 1
        return

    def _part1(self):
        # IDEA: add sand until sand reaches max_depth

        # add sand to cave wall
        absolute_sand_position = self.start
        while absolute_sand_position[0] != self.max_row: # run until we reach lowest index for y
            position_row, position_col = absolute_sand_position
            # down
            if not self.occupied_space((position_row + 1, position_col)):
                absolute_sand_position = (position_row + 1, position_col)
            # down left
            elif not self.occupied_space((position_row + 1, position_col - 1)):
                absolute_sand_position = (position_row + 1, position_col - 1)       
            # down right
            elif not self.occupied_space((position_row + 1, position_col + 1)):
                absolute_sand_position = (position_row + 1, position_col + 1)
            else:
                self.sand.add(absolute_sand_position)
                absolute_sand_position = self.start
        return len(self.sand)

    def _part2(self):
        # add sand to cave wall
        absolute_sand_position = self.start
        while absolute_sand_position not in self.sand: # run until we reach lowest index for y
            position_row, position_col = absolute_sand_position
            # down
            if not self.occupied_space2((position_row + 1, position_col)):
                absolute_sand_position = (position_row + 1, position_col)
            # down left
            elif not self.occupied_space2((position_row + 1, position_col - 1)):
                absolute_sand_position = (position_row + 1, position_col - 1)       
            # down right
            elif not self.occupied_space2((position_row + 1, position_col + 1)):
                absolute_sand_position = (position_row + 1, position_col + 1)
            else:
                self.sand.add(absolute_sand_position)
                absolute_sand_position = self.start
        return len(self.sand)

    def relative_position(self, position):
        return (position[0] - self.min_row, position[1] - self.min_col)

    def occupied_space(self, position):
        relative_row, relative_col = self.relative_position(position)
        return self.cave_wall[relative_row][relative_col] == 1 or position in self.sand

    def occupied_space2(self, position):
        return position in self.rockset or position in self.sand or position[0] == self.max_row + 1

    def __str__(self):
        s = ''
        for i, row in enumerate(self.cave_wall):
            for j, col in enumerate(row):
                c = '.' if col == 0 else '#'
                if (i + self.min_row, j + self.min_col) in self.sand:
                    c = 'o'
                s += c
            s += '\n'
        s += '\n'        
        for k, v in self.answers.items():
            part1 = v['Part1']
            part2 = v['Part2']
            s += f'{k} --- Part 1: {part1} Part 2: {part2}\n'
        return s.strip()

d = Day(problem='13', test_only=False)
d.solve()
print(d)