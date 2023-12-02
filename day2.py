import math
import sys
import itertools
import functools
import copy
from typing import Iterable
import subprocess
from collections import Counter
from collections import defaultdict
from collections import namedtuple
import re
import aoc
import numpy as np
import networkx as nx
import operator
import time

vecadd = lambda *v: tuple(sum(x) for x in zip(*v))
sys.setrecursionlimit(10000)

day = '2'
p = subprocess.run("bash -c './p_data.sh " + day + " true' ")
input = open('./input_d_' + day + '.txt').read()


lines=[e for e in input.split('\n')]

#REGEX
#pattern = r'.*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?'
pattern = r'.*?Game ([0-9]*): (.*);*?'
parsed = [[int(gid),gdata] for gid,gdata in re.findall(pattern,input)]


def parseLine(game):
    parts=game[1].split(';')
    res=[]
    for part in parts:
        item=[0,0,0] #red blue green
        item[0]=find_count('red', part)
        item[1]=find_count('blue', part)
        item[2]=find_count('green', part)
        #print(item)
        res.append(item)

    return game[0],res

def find_count(color, part):
    pattern = r'.*?([0-9]*) '+color+'?'
    parse = list(re.findall(pattern, part))
    return int(parse[0]) if parse else 0

games = dict(map(parseLine,parsed))

max_r=12
max_b=14
max_g=13
comp=[max_r,max_b,max_g]
s=0
for g,(k,v) in enumerate(games.items()):
    print(f'Game {k} Value = {v}')
    # c_r=0
    # c_b=0
    # c_g=0
    #
    # for round in v:
    #     c_r=max(c_r,round[0])
    #     c_b=max(c_b,round[1])
    #     c_g=max(c_g,round[2])
    # s+=c_r*c_g*c_b
    s+=math.prod(map(max,zip(*v)))


# possible=True
    # for round in v:
    #     if (not(all(x<=y for x,y in zip(round,comp)))):
    #         print(k,round)
    #         possible=False
    #         break
    # if possible:
    #     s+=k



print(s)
sys.exit()

#MATRIX
col_length=len(lines)-1
row_length=max([len(lines[c]) for c in range(0,col_length)])
print(col_length, row_length)
#matrix=[[list(lines[y])[x] if len(list(lines[y]))>x else " " for x in range(0,row_length)] for y in range(0,col_length)]
#matrix=[[x for x in range(0,row_length)] for y in range(0,col_length)]
#print(matrix)

print(input)
#PARSE SIMPLE
for line in lines[0:]:
    parts=line.split(' ')
    #x,y=parts[0],parts[1]
    #print(x,y)






