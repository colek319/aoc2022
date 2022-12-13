from helpers.helpers import readfile

point_chart = {
    'A': {
        'A': 4,
        'B': 1,
        'C': 7,
    },
    'B': {
        'A': 8,
        'B': 5,
        'C': 2,
    },
    'C': {
        'A': 3,
        'B': 9,
        'C': 6,
    },
}

decision_chart = {
    'X': {
        'A': 'C',
        'B': 'A',
        'C': 'B',
    }, # lose
    'Y': {
        'A': 'A',
        'B': 'B',
        'C': 'C',
    }, # draw
    'Z': {
        'A': 'B',
        'B': 'C',
        'C': 'A',
    }, # win
}

def main():
    lines = readfile('01')
    score = 0
    for line in lines:
        guide = line.split(' ')
        them = guide[0]
        directions = guide[1]
        me = decision_chart[directions[0]][them]
        score += point_chart[me][them]
    print(score)

if __name__ == '__main__':
    main()

import os
class Day():
    def __init__(self, problem='problem', test_only=False):
        self.problem = problem
        self.test_only = test_only        
        self.answers = {}
        self.bookkeep() # define stateful variables in bookkeep

    def bookkeep(self):
        # declare vars here
        return

    def solve(self):
        for file in os.listdir('./problems/' + self.problem):
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
        with open('./problems/' + self.problem + '/' + input_name + '.input', 'r') as fstream:
            # handle input for part 1
            pass

    def _handle_input_part2(self, input_name):
        # handle input line for part 2 here
        with open('./problems/' + self.problem + '/' + input_name + '.input', 'r') as fstream:
            # handle input for part 2
            pass

    def _handle_input(self, fstream):
        # use this if part1 and part2 handle input the same way
        for line in fstream.read().splitlines():
            # read input here
            pass
        return

    def _part1(self):
        return 'TODO'

    def _part2(self):     
        return 'TODO'

    def __str__(self):
        s = ''
        for k, v in self.answers.items():
            part1 = v['Part1']
            part2 = v['Part2']
            s += f'{k} --- Part 1: {part1} Part 2: {part2}\n'
        return s.strip()

d = Day(problem='00', test_only=False)
d.solve()
print(d)