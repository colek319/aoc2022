from helpers.helpers import readfile

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorities = {alphabet[i]: i+1 for i in range(52)}

def main():
    lines = readfile('02')
    counter = 0
    total = 0
    groups = []
    for line in lines:
        if counter % 3 == 0:
            counter = 0
            groups.append([])
        groups[-1].append(line)
        counter += 1
    
    for group in groups:
        print(group)
        elf0 = set(group[0])
        elf1 = set(group[1])
        elf2 = set(group[2])
        badge = elf0.intersection(elf1, elf2)
        print(badge)
        total += priorities[badge.pop()]

    print(total)

if __name__ == '__main__':
    main()
