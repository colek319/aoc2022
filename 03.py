from helpers.helpers import readfile

def part1():
    lines = readfile('03')
    count = 0
    for line in lines:
        interval1, interval2 = line.split(',')
        a1, a2 = interval1.split('-')
        b1, b2 = interval2.split('-')
        a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
        if (a1 >= b1 and a2 <= b2) or (a1 <= b1 and a2 >= b2):
            count += 1
    print(count)

def part2():
    lines = readfile('03')
    count = 0
    for line in lines:
        interval1, interval2 = line.split(',')
        a1, a2 = interval1.split('-')
        b1, b2 = interval2.split('-')
        a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
        if (a1 >= b1 and a2 <= b2) or (a1 <= b1 and a2 >= b2):
            count += 1
        elif (a2 >= b1 and a2 <= b2) or b2 >= a1 and b2 <= a2:
            count += 1
    print(count)

if __name__ == '__main__':
    part1()
    part2()
