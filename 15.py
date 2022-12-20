import os
import networkx as nx
from parse import parse
import matplotlib.pyplot as plt

TESTDIR = './days'

'''
Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?

maximize sum(flow(nodes)) where sum(weight(edges)) == 30

'''

INPUT_SINGULAR = 'Valve {} has flow rate={}; tunnel leads to valve {}'
INPUT_PLURAL = 'Valve {} has flow rate={}; tunnels lead to valves {}'

class Day():
    def __init__(self, problem='problem', test=False):
        self.problem = problem
        self.test = test   
        self.answers = {}
        self.bookkeep() # define stateful variables in bookkeep

    def bookkeep(self):
        # declare vars here
        self.adjacency_list = {}
        self.floyd_warshall_adjacency_list = {}
        self.valve_flow = {}
        self.start = None
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
            # handle input for part 2
            self._handle_input(fstream)

    def _handle_input_part2(self, input_name):
        # handle input line for part 2 here
        with open(TESTDIR + '/' + self.problem + '/' + input_name + '.input', 'r') as fstream:
            # handle input for part 2
            self._handle_input(fstream)

    def _handle_input(self, fstream):
        # use this if part1 and part2 handle input the same way
        for line in fstream.read().splitlines():
            source, flow, targets = None, None, None
            if match := parse(INPUT_SINGULAR, line):
                source = match[0]
                flow = int(match[1])
                targets = match[2].split(', ')
            elif match := parse(INPUT_PLURAL, line):
                source = match[0]
                flow = int(match[1])
                targets = match[2].split(', ')
            if self.start is None:
                self.start = source
            self.adjacency_list[source] = targets
            self.valve_flow[source] = flow
        self.floyd_warshall_adjacency_list = self._floyd_warshall()

    def _part1(self):
        return 'TODO'

    def _part2(self):     
        return 'TODO'

    def _floyd_warshall(self):
        pass

    def __str__(self):
        s = ''
        for k, v in self.answers.items():
            part1 = v['Part1']
            part2 = v['Part2']
            s += f'{k} --- Part 1: {part1} Part 2: {part2}\n'
        
        return s.strip()

d = Day(problem='15', test=True)
d.solve()
print(d)