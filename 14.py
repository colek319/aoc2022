import os
from parse import parse

TESTDIR = './days'
INPUT_TEMPLATE = 'Sensor at x={}, y={}: closest beacon is at x={}, y={}'
MIN_X_Y = 0

class Day():
    def __init__(self, problem='problem', test=False):
        self.problem = problem
        self.test = test
        self.answers = {}
        self.bookkeep() # define stateful variables in bookkeep

    def bookkeep(self):
        # declare vars here
        self.PART_1_Y = 2_000_000 if not self.test else 10
        self.MAX_X_Y = 4_000_000 if not self.test else 20
        self.TUNING_SCALER = 4_000_000
        self.sensors = set()
        self.beacons = set()
        self.sensor_beacon_distances = {}
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
            for line in fstream.read().splitlines():
                sensor_x, sensor_y, beacon_x, beacon_y = parse(INPUT_TEMPLATE, line)
                self.sensors.add((int(sensor_x), int(sensor_y)))
                self.beacons.add((int(beacon_x), int(beacon_y)))
                distance = self.manhattan_distance((int(sensor_x), int(sensor_y)), (int(beacon_x), int(beacon_y)))
                self.sensor_beacon_distances[(int(sensor_x), int(sensor_y))] = distance
                

    def _handle_input_part2(self, input_name):
        # handle input line for part 2 here
        with open(TESTDIR + '/' + self.problem + '/' + input_name + '.input', 'r') as fstream:
            # handle input for part 2
            for line in fstream.read().splitlines():
                sensor_x, sensor_y, beacon_x, beacon_y = parse(INPUT_TEMPLATE, line)
                self.sensors.add((int(sensor_x), int(sensor_y)))
                self.beacons.add((int(beacon_x), int(beacon_y)))
                distance = self.manhattan_distance((int(sensor_x), int(sensor_y)), (int(beacon_x), int(beacon_y)))
                self.sensor_beacon_distances[(int(sensor_x), int(sensor_y))] = distance

    def _handle_input(self, fstream):
        # use this if part1 and part2 handle input the same way
        for line in fstream.read().splitlines():
            # read input here
            pass
        return

    def manhattan_distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def _part1(self):
        coverage_intervals = []
        cover = set() # holds points covered by coverage_intervals
        for sensor, distance in self.sensor_beacon_distances.items():
            distance_to_row = self.manhattan_distance(sensor, (sensor[0], self.PART_1_Y)) # distance to row 2_000_000
            interval_radius = distance - distance_to_row # width of interval the beacon can be in
            if interval_radius < 0:
                continue
            interval = (sensor[0] - interval_radius, sensor[0] + interval_radius)
            coverage_intervals.append(interval)
        for interval in coverage_intervals:
            for x in range(interval[0], interval[1] + 1):
                if (x, self.PART_1_Y) in self.beacons:
                    continue
                if (x, self.PART_1_Y) in self.sensors:
                    continue
                cover.add(x)

        return len(cover)

    def _part2(self):
        for row in range(MIN_X_Y, self.MAX_X_Y + 1):
            if row % 100000 == 0:
                print(row)
            coverage_intervals = [] # track intervals for row
            for sensor, distance in self.sensor_beacon_distances.items():
                distance_to_row = self.manhattan_distance(sensor, (sensor[0], row))
                interval_radius = distance - distance_to_row # width of interval the beacon can be in
                if interval_radius < 0:
                    continue
                interval = (sensor[0] - interval_radius, sensor[0] + interval_radius)
                coverage_intervals.append(interval)                
            bounds_array = self.to_bound_array(coverage_intervals)
            # we use a closed open model. closed == False means a new interval is about to start
            # if closed, and the next element opens after the last index, then we have a gap
            index = 0
            bound_stack = []
            for bound in bounds_array:
                if len(bound_stack) == 0:
                    # potential gap
                    if index < bound[0]:
                        # we have a gap
                        return (index + 1) * self.TUNING_SCALER + row
                index = bound[0]
                if bound[1] == 'left':
                    bound_stack.append(bound)
                elif bound[1] == 'right':
                    bound_stack.pop()
        return 'TOTO'

    def to_bound_array(self, intervals):
        # onvert list of interbals into start and stop tuples in an array
        bound_array = []
        for interval in intervals:
            bound_array.append((interval[0], 'left'))
            bound_array.append((interval[1], 'right'))
        return sorted(bound_array, key=lambda x: x[0])

    def __str__(self):
        s = ''
        for k, v in self.answers.items():
            part1 = v['Part1']
            part2 = v['Part2']
            s += f'{k} --- Part 1: {part1} Part 2: {part2}\n'
        return s.strip()

d = Day(problem='14', test=False)
d.solve()
print(d)