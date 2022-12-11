from helpers.helpers import readfile

class Day():
    def __init__(self, problem='problem'):
        day = './data/' + problem +'.input'
        with open (day, 'r') as f:
            self.lines = f.readlines()

    def part1(self):
        for line in self.lines:
            continue
        return 'answer'

    def part2(self):
        for line in self.lines:
            continue
        return 'answer'        

    def __str__(self):
        s = f'Part 1: {self.part1()} Part 2: {self.part2()}'
        return s

d = Day('input problem here')
print(d)