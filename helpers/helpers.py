import re

def readfile(daynum):
    with open('./data/' + daynum, 'r') as f:
        return f.read()

def readlines(daynum):
    with open('./data/' + daynum, 'r') as f:
        return f.read().splitlines()

def shrink_whitespace(s):
    return re.sub(r' +', ' ', s.strip())