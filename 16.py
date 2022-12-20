import os

TESTDIR = './days'

'''
7 units wide

input is just directions.

Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).
'''

MINUS = ([(0, 0), (0, 1), (0, 2), (0, 3)], (1, 4))
PLUS = ([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)], (3, 3))
L = ([(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)], (3, 3))
I = ([(0, 0), (1, 0), (2, 0), (3, 0)], (4, 1))
BLOCK = ([(0, 0), (0, 1), (1, 0), (1, 1)], (2, 2))
rock_formations = [MINUS, PLUS, L, I, BLOCK]

class Day():
    def __init__(self, problem='problem', test=False):
        self.problem = problem
        self.test = test   
        self.answers = {}
        self.bookkeep() # define stateful variables in bookkeep

    def bookkeep(self):
        # declare vars here
        self.move_distance = 0
        self.jets = []
        self.jet_round = 0
        self.width = 7
        self.tower_height = 0
        self.starting_column = 2
        self.starting_overhead = 3
        self.cave = None
        self.height = 10_000
        self.window_height = 10_000
        self.num_rounds = None
        self.height_codes_seen = {}
        self.round = 0
        self.which_rock = 0
        return

    def solve(self):
        for file in os.listdir(TESTDIR + '/' + self.problem):
            input_name = file.split('.')[0]
            if self.test and not 'test' in input_name:
                continue
            elif not self.test and 'test' in input_name:
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
            self.num_rounds = 2022
            self.height = self.num_rounds * 5
            self.cave = [['.' for _ in range(self.width)] for _ in range(self.height)]

    def _handle_input_part2(self, input_name):
        # handle input line for part 2 here
        with open(TESTDIR + '/' + self.problem + '/' + input_name + '.input', 'r') as fstream:
            # handle input for part 2
            self._handle_input(fstream)
            self.num_rounds = 1_000_000_000_000
            self.cave = [['.' for _ in range(self.width)] for _ in range(self.height)]
            # use a sliding window

    def _handle_input(self, fstream):
        # use this if part1 and part2 handle input the same way
        for d in fstream.read():
            if d == '>':
                # move right + 1
                self.jets.append(1)
            else:
                # move left - 1
                self.jets.append(-1)

    def _part1(self):
        return self._run()

    def _part2(self):
        return self._run()

    def _run(self):
        start, repeat = 0, 0
        for _ in range(10_000):
            self._drop()
            self.which_rock = (self.which_rock + 1) % len(rock_formations)
            self.round += 1
            if pattern_and_indices := self._check_pattern():
                _, i1, i2 = pattern_and_indices
                start = i1
                repeat = i2 - i1
                break
        start_cycle_round_height = self.tower_height
        
        # get to height of tower at start of cycle
        self._set_base(None)
        self.round = 0
        for _ in range(start):
            self._drop()
            self.which_rock = (self.which_rock + 1) % len(rock_formations)
        cycle_start_height = self.tower_height
        height_gained_per_cycle = start_cycle_round_height - cycle_start_height

        mid_cycle_rounds = (self.num_rounds - start) % repeat
        num_cycles = (self.num_rounds - start) // repeat

        for _ in range(mid_cycle_rounds):
            self._drop()
            self.which_rock = (self.which_rock + 1) % len(rock_formations)
        return self.tower_height + height_gained_per_cycle * num_cycles        

    def _drop(self):
        rock, rock_dim = rock_formations[self.which_rock]
        rock_height, rock_width = rock_dim
        root_row = self.tower_height + self.starting_overhead + rock_height - 1
        root_col = self.starting_column
        # print(f'dropping rock {which_rock} at {root_row}, {root_col}')
        while True:
            # adjust
            if self.jets[self.jet_round] < 0:
                # left
                if not self._blocked_left(root_row, root_col, rock):
                    root_col = max(root_col - 1, 0)
            else:
                # right
                if not self._blocked_right(root_row, root_col, rock):
                    root_col = min(root_col + 1, self.width - rock_width)     
            # try to fall
            stopped = self._rock_stopped(root_row, root_col, rock)
            if stopped:
                self._place(root_row, root_col, rock)
                self.tower_height = max(root_row + 1, self.tower_height)
                self.jet_round = (self.jet_round + 1) % len(self.jets)
                break
            else:
                root_row -= 1
            self.jet_round = (self.jet_round + 1) % len(self.jets)


    def _rock_stopped(self, root_row, root_col, rock):
        for row, col in rock:
            col = root_col + col
            row = root_row - row - 1
            if row < 0 or self.cave[row][col] == '#':
                return True
        return False

    def _blocked_left(self, root_row, root_col, rock):
        for row, col in rock:
            col = root_col + col - 1
            row = root_row - row
            if col < 0 or self.cave[row][col] == '#':
                return True
        return False

    def _blocked_right(self, root_row, root_col, rock):
        for row, col in rock:
            col = root_col + col + 1
            row = root_row - row
            if col >= self.width or self.cave[row][col] == '#':
                return True
        return False

    def _place(self, root_row, root_col, rock):
        # print(f'placing rock at {root_row}, {root_col}')
        for row, col in rock:
            rock_col = root_col + col
            self.cave[root_row - row][rock_col] = '#'

    def _check_pattern(self):
        barcode = self._height_barcode()
        if barcode in self.height_codes_seen:
            return barcode, self.height_codes_seen[barcode], self.round
        else:
            self.height_codes_seen[barcode] = self.round
            return 0        

    def _height_barcode(self):
        min = None
        column_heights = [0] * self.width
        for col in range(self.width):
            for row in range(self.window_height):
                if self.cave[self.window_height - row - 1][col] == '#':
                    column_heights[col] = row + 1
                    if min is None or row < min:
                        min = row
                    break
        barcode = [str(h - min) for h in column_heights] if min is not None else ['0'] * self.width
        return (','.join(barcode), self.jet_round, self.which_rock)

    def _set_base(self, barcode):
        self.cave = [['.' for _ in range(self.width)] for _ in range(self.height)]
        if barcode is None:
            self.jet_round = 0
            self.which_rock = 0
            self.tower_height = 0
            return
        heights, jet_round, which_rock = barcode
        self.jet_round = jet_round
        self.which_rock = which_rock + 1
        self.tower_height = max(int(height) for height in heights.split(','))
        for col, col_height in enumerate(heights.split(',')):
            for row in range(int(col_height)):
                self.cave[row][col] = '#'

    def _print_tower(self):
        for row in list(reversed(self.cave))[-self.tower_height - 10:]:
            print(''.join(row))

    def __str__(self):
        s = ''
        for k, v in self.answers.items():
            part1 = v['Part1']
            part2 = v['Part2']
            s += f'{k} --- Part 1: {part1} Part 2: {part2}\n'
        return s.strip()

d = Day(problem='16', test=False)
d.solve()
print(d)