import re
import os

def readfile(daynum):
    with open('./data/' + daynum, 'r') as f:
        return f.read()

def readlines(daynum):
    with open('./data/' + daynum, 'r') as f:
        return f.read().splitlines()

def shrink_whitespace(s):
    return re.sub(r' +', ' ', s.strip())

# parses a file into several sub problems
def read_problem(problem: str) -> dict:
    print(os.listdir('./problems/' + problem))
    # with open('./problems/' + problem + '.input', 'r') as f:
    #     for line in 