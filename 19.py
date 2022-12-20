import os

TESTDIR = './days'

'''
This problem was tricky for me. The directions were totally explicit, but lacking in 
detail making me lose insight into how key "circularity" is. This is a lesson I have
learned many times. Consider exactly what is stated. There are 6 spaces in a circle of
7 elements. A full circle is completed by moving forward "6 positions in a circle."
'''

class Day():
    def __init__(self, problem='problem', test=False):
        self.problem = problem
        self.test = test   
        self.answers = {}
        self.bookkeep() # define stateful variables in bookkeep

    def bookkeep(self):
        # declare vars here
        self.encrypted_file = None
        self.decrypted_file = None
        self.permutation = None
        self.file_size = 0
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
            # hold two of each, one for mixing one for reading operations
            self.encrypted_file = [int(s) for s in fstream.read().splitlines()]
            self.file_size = len(self.encrypted_file)
            self.decrypted_file = [i for i in range(self.file_size)]
            self.permutation = [i for i in range(self.file_size)]


    def _handle_input_part2(self, input_name):
        # handle input line for part 2 here
        with open(TESTDIR + '/' + self.problem + '/' + input_name + '.input', 'r') as fstream:
            # handle input for part 2
            self.encrypted_file = [int(s) * 811589153 for s in fstream.read().splitlines()]
            self.file_size = len(self.encrypted_file)
            self.decrypted_file = [i for i in range(self.file_size)]
            self.permutation = [i for i in range(self.file_size)]


    def _handle_input(self, fstream):
        # use this if part1 and part2 handle input the same way
        for line in fstream.read().splitlines():
            # read input here
            pass
        return

    def _part1(self):
        # print(self._decrypted_file_values())
        for i, op in enumerate(self.encrypted_file):
            # do operations on self.decrypted_file
            start = self.permutation[i] # gives us the new index of the i'th operation
            forward_movement = op % (self.file_size - 1) # translate to a movement forward. -3 -> move forward 3
            destination = start + forward_movement
            if destination >= self.file_size:
                destination = destination % (self.file_size - 1)
            self._move(start, destination)
            # print(self._decrypted_file_values())

        return self._get_mixing_number()

    def _part2(self):     
        # print(self._decrypted_file_values())
        for i in range(10):
            for i, op in enumerate(self.encrypted_file):
                # do operations on self.decrypted_file
                start = self.permutation[i] # gives us the new index of the i'th operation
                forward_movement = op % (self.file_size - 1) # translate to a movement forward. -3 -> move forward 3
                destination = start + forward_movement
                if destination >= self.file_size:
                    destination = destination % (self.file_size - 1)
                self._move(start, destination)
                # print(self._decrypted_file_values())
            
        return self._get_mixing_number()

    def _move(self, start, destination):
        if destination < start:
            # shift left
            self.decrypted_file = self.decrypted_file[:destination] + [self.decrypted_file[start]] + self.decrypted_file[destination:start] + self.decrypted_file[start+1:]
        elif destination > start:
            # shift right
            self.decrypted_file = self.decrypted_file[:start] + self.decrypted_file[start+1:destination+1] + [self.decrypted_file[start]] + self.decrypted_file[destination+1:]

        # update permutation
        for i, v in enumerate(self.decrypted_file):
            self.permutation[v] = i

    def _decrypted_file_values(self):
        return [self.encrypted_file[i] for i in self.decrypted_file]

    def _get_mixing_number(self):
        total = 0
        descrypted_file_values = self._decrypted_file_values()
        root_index = descrypted_file_values.index(0)
        for i in [1000, 2000, 3000]:
            i_modded = (root_index + i) % self.file_size
            total += descrypted_file_values[i_modded]
        return total        

    def __str__(self):
        s = ''
        for k, v in self.answers.items():
            part1 = v['Part1']
            part2 = v['Part2']
            s += f'{k} --- Part 1: {part1} Part 2: {part2}\n'
        return s.strip()

d = Day(problem='19', test=False)
d.solve()
print(d)