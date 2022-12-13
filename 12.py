import os
import ast

TESTDIR = './days'

'''
Determine which pairs of packets are already in the right order
'''

class Day():
    def __init__(self, problem='problem', test_only=False):
        self.problem = problem
        self.test_only = test_only        
        self.answers = {}
        self.bookkeep() # define stateful variables in bookkeep

    def bookkeep(self):
        # declare vars here
        self.pairs = {}
        self.packets = []

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

    def _handle_input(self, fstream):
        # use this if part1 and part2 handle input the same way
        index = 1
        for line in fstream.read().splitlines():
            # read input here
            if line == '':
                index += 1
                continue
            packet_pair = self.pairs.setdefault(index, [])
            packet = ast.literal_eval(line)
            packet_pair.append(packet)
            self.packets.append(packet)
        self.packets.append([[2]])
        self.packets.append([[6]])
        return

    def _part1(self):
        index_sum = 0
        for k, v in self.pairs.items():
            if self.compare(v[0], v[1]):
                index_sum += k
        return index_sum

    def _part2(self):
        self.packets = self.merge_sort(self.packets)
        index_2 = self.packets.index([[2]]) + 1
        index_6 = self.packets.index([[6]]) + 1
        return index_2 * index_6

    # defines a l1 <= l2 function
    def compare(self, l1, l2):
        stack = [(list(l1), list(l2))]
        while stack:
            l1, l2 = stack.pop()
            if isinstance(l1, (int, float)) and isinstance(l2, (int, float)):
                if l1 < l2:
                    return True
                if l2 < l1:
                    return False
            if isinstance(l1, list) and isinstance(l2, list):
                diff = abs(len(l2) - len(l1))
                if len(l1) > len(l2):
                    l2 = l2 + [float('-inf')] * diff
                elif len(l2) > len(l1):
                    l1 = l1 + [float('-inf')] * diff
                stack.extend(reversed(list(zip(l1, l2))))
            if isinstance(l1, (int, float)) and isinstance(l2, list):
                stack.append(([l1], l2))                
            if isinstance(l1, list) and isinstance(l2, (int, float)):
                stack.append((l1, [l2]))

        return False

    def merge_sort(self, l):
        if len(l) <= 1:
            return l
        mid = len(l) // 2
        left = self.merge_sort(l[:mid])
        right = self.merge_sort(l[mid:])
        ret = []
        i, j = 0, 0
        while i < len(left) or j < len(right):
            if i == len(left):
                ret.append(right[j])
                j += 1
            elif j == len(right):
                ret.append(left[i])
                i += 1
            elif self.compare(left[i], right[j]):
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                j += 1
        return ret

    def __str__(self):
        s = ''
        for k, v in self.answers.items():
            part1 = v['Part1']
            part2 = v['Part2']
            s += f'{k} --- Part 1: {part1} Part 2: {part2}\n'
        return s.strip()

d = Day(problem='12', test_only=False)
d.solve()
print(d)
