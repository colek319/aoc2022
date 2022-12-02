from lib.lib import readfile

def main():
    lines = readfile('00')
    elves = []
    elf_cals = 0
    for line in lines:
        if line == '':
            # start new elf
            elves.append(elf_cals)
            elf_cals = 0
        else:
            # add calories
            elf_cals += int(line)
    elves.append(elf_cals) # add last elf

    print(max(elves))
    elves.sort()
    print(elves[-1] + elves[-2] + elves[-3])

if __name__ == '__main__':
    main()
