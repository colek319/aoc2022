from lib.lib import readfile_nolines

def part1():
    stream = readfile_nolines('05')
    for i in range(4, len(stream)):
        if len(set(stream[i-4:i])) == 4:
            print('Found a match!')
            print(stream[i-4:i])
            print(i)
            break
        

def part2():
    stream = readfile_nolines('05')
    for i in range(14, len(stream)):
        if len(set(stream[i-14:i])) == 14:
            print('Found a match!')
            print(stream[i-14:i])
            print(i)
            break

if __name__ == '__main__':
    part1()
    part2()