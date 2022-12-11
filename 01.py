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
