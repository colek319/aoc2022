from helpers.helpers import readfile

class Day():
    def __init__(self, problem='problem'):
        day = './data/' + problem +'.input'
        with open (day, 'r') as f:
            self.lines = f.readlines()
        self.monkeys = {}
        self.monkey_items = [] # tracks monkey values for each item
        self.num_items = 0

    def reset(self):
        self.monkeys = {}


    def part1(self):
        self.read_input(part1=True)
        for i in range(20):
            self.round(part1=True)

        return self.monkey_business()

    def part2(self):
        self.read_input() 

        for j in range(10000):
            self.round()

        return self.monkey_business()

    def read_input(self, part1=False):
        i = 0
        curr_monkey = None
        all_items = []
        for i in range(len(self.lines)):
            line = self.lines[i]
            match line.split():
                case ['Monkey', monkey_num]:
                    monkey_num = monkey_num[:-1] # remove trailing :
                    self.monkeys[monkey_num] = {'items': [], 'operation': (), 'result': (), 'activity': 0}
                    curr_monkey = monkey_num              
                case ['Starting', 'items:', *items]:
                    items = ' '.join(items).split(', ') # remove trailing ,
                    monkey = self.monkeys[curr_monkey]
                    for item in items:
                        monkey['items'].append(len(all_items)) # add item key to this monkey
                        all_items.append(item)
                case ['Operation:', *operation]:
                    monkey = self.monkeys[curr_monkey]
                    # new = a op b
                    _, _, a, op, b = operation 
                    monkey['operation'] = (a, op, b)
                case ['Test:', *result]:
                    monkey = self.monkeys[curr_monkey]
                    _, _, divisor = result
                    i += 1
                    line = self.lines[i].split()
                    if_true = line[-1]
                    i += 1
                    line = self.lines[i].split()
                    if_false = line[-1]
                    monkey['result'] = (int(divisor), if_true, if_false)
            i += 1

        self.monkey_items = [[0] * len(all_items) for _ in range(len(self.monkeys))]
        for m, monkey in self.monkeys.items():
            for item_id, item in enumerate(all_items):
                divisor = monkey['result'][0]
                if part1:
                    self.monkey_items[int(m)][item_id] = int(item)
                else:
                    self.monkey_items[int(m)][item_id] = int(item) % divisor

    def round(self, part1=False):
        for m, v in self.monkeys.items():
            # get items
            items = v['items']
            while items:
                item_id = items.pop(0)
                self.inspect_all(m, item_id, part1=part1)
                value = self.monkey_items[int(m)][item_id]
                divisor, if_true, if_false = v['result']
                if value % divisor == 0:
                    # do if_true
                    self.monkeys[if_true]['items'].append(item_id)
                else:
                    # do if_false
                    self.monkeys[if_false]['items'].append(item_id)
                # update activity
                v['activity'] += 1

    def monkey_business(self):
        activity_levels = [monkey['activity'] for monkey in self.monkeys.values()]
        activity_levels.sort()
        return activity_levels[-1] * activity_levels[-2]

    def inspect_all(self, inspecting_monkey, item_id, part1=False):
        a, op, b = self.monkeys[inspecting_monkey]['operation']
        for m, v in self.monkeys.items():
            mint = int(m)
            # get the monkeys update
            divisor, _, _ = v['result']
            old_value = self.monkey_items[mint][item_id]
            new_value = self.inspect(a, op, b, old_value)
            if part1:
                self.monkey_items[mint][item_id] = (new_value // 3)
            else:
                self.monkey_items[mint][item_id] = (new_value % divisor)

    def inspect(self, a, op, b, old_value):
        # update monkey view for all items
        if a == 'old':
            a = old_value
        if b == 'old':
            b = old_value
        if op == '+':
            return int(a) + int(b)
        if op == '*':
            return int(a) * int(b)


    def __str__(self):
        part1 = self.part1()
        self.reset()
        part2 = self.part2()
        s = f'Part 1: {part1} Part 2: {part2}'
        return s

d = Day('10')
print(d)