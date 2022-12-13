import os
from collections import deque

'''
a is lowest, z is highest

S has elevation a
E has elevation z

we want to go from S to E

use dijkstras

shortest_path(G, source=None, target=None, weight=None, method='dijkstra')
'''

ELEVATIONS = {letter: i for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz')}

class Day():
    def __init__(self, day='day', test_only=False):
        self.day = day
        self.test_only = test_only        
        self.answers = {}

    def bookkeep(self):
        # declare vars here
        self.terrain = []
        self.start = None
        self.starts = [] # for multiple starting positions

    def solve(self):
        for file in os.listdir('./days/' + self.day):
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
        with open('./days/' + self.day + '/' + input_name + '.input', 'r') as fstream:
            # handle input for part 1
            lines = fstream.read().splitlines()
            self.terrain = lines
            for line in lines:
                for i, letter in enumerate(line):
                    if letter == 'S':
                        self.start = (lines.index(line), i)
                        break
                if self.start:
                    break

    def _handle_input_part2(self, input_name):
        # handle input line for part 2 here
        with open('./days/' + self.day + '/' + input_name + '.input', 'r') as fstream:
            # handle input for part 1
            lines = fstream.read().splitlines()
            self.terrain = lines
            for line in lines:
                for i, letter in enumerate(line):
                    if letter == 'S' or letter == 'a':
                        # add all S or a to start
                        self.starts.append((lines.index(line), i))

    def _handle_input(self, fstream):
        # use this if part1 and part2 handle input the same way
        for line in fstream.read().splitlines():
            # read input here
            pass
        return

    def _part1(self):
        numrows, numcols = len(self.terrain), len(self.terrain[0])
        # bfs from start to find shortest path to E
        starti, startj = self.start
        visited = set()
        queue = deque()
        queue.append((starti, startj, 0)) # row, col, distance from start
        while queue:
            node = queue.popleft()
            i, j, distance = node
            if (i, j) in visited:
                continue
            visited.add((i, j)) # mark that we visited this node already
            letter = self.terrain[i][j]
            if letter == 'E':
                return distance
            elevation = ELEVATIONS[letter] if letter != 'S' else 0
            # go through all adjacent nodes
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + di < numrows and 0 <= j + dj < numcols:
                    if (i + di, j + dj) in visited:
                        # dont inspect visited nodes
                        continue
                    new_letter = self.terrain[i + di][j + dj]
                    new_elevation = ELEVATIONS[new_letter] if new_letter != 'E' else 25
                    if new_elevation > elevation + 1:
                        # too high. cant go here
                        continue

                    queue.append((i + di, j + dj, distance + 1))        
        return 'NOT FOUND'

    def _part2(self):
        distances = []
        for start in self.starts:
            numrows, numcols = len(self.terrain), len(self.terrain[0])
            # bfs from start to find shortest path to E
            starti, startj = start
            visited = set()
            queue = deque()
            queue.append((starti, startj, 0)) # row, col, distance from start
            while queue:
                node = queue.popleft()
                i, j, distance = node
                if (i, j) in visited:
                    continue
                visited.add((i, j)) # mark that we visited this node already
                letter = self.terrain[i][j]
                if letter == 'E':
                    distances.append(distance)
                    break
                elevation = ELEVATIONS[letter] if letter != 'S' else 0
                # go through all adjacent nodes
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= i + di < numrows and 0 <= j + dj < numcols:
                        if (i + di, j + dj) in visited:
                            # dont inspect visited nodes
                            continue
                        new_letter = self.terrain[i + di][j + dj]
                        if new_letter == 'S':
                            new_elevation = 0
                        elif new_letter == 'E':
                            new_elevation = 25
                        else:
                            new_elevation = ELEVATIONS[new_letter]
                        if new_elevation > elevation + 1:
                            # too high. cant go here
                            continue

                        queue.append((i + di, j + dj, distance + 1))
        return min(distances)

    def __str__(self):
        s = ''
        for k, v in self.answers.items():
            part1 = v['Part1']
            part2 = v['Part2']
            s += f'{k} --- Part 1: {part1} Part 2: {part2}\n'
        return s.strip()

d = Day(day='11', test_only=False)
d.solve()
print(d)