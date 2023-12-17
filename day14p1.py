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
import networkx
import numpy as np
import networkx as nx
import operator
import time

vecadd = lambda *v: tuple(sum(x) for x in zip(*v))
sys.setrecursionlimit(10000)

day = '14'
p = subprocess.run("bash -c './p_data.sh " + day + " true' ")
input = open('./input_d_' + day + '.txt').read()
#input = open('./input_d_' + day + '_small.txt').read()

lines=[e for e in input.split('\n')]

#REGEX
#pattern = r'.*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?'
#parsed = [(int(bid),int(ore),int(clay),int(obo),int(obc),int(geo),int(geob)) for bid,ore,clay,obo,obc,geo,geob in re.findall(pattern,input)]


#MATRIX
col_length=len(lines)-1
row_length=max([len(lines[c]) for c in range(0,col_length)])
#matrix=[[list(lines[y])[x] if len(list(lines[y]))>x else " " for x in range(0,row_length)] for y in range(0,col_length)]
matrix=[[list(lines[y])[x] for x in range(0,row_length)] for y in range(0,col_length)]

print(col_length, row_length)

y_jumps=[]
x_jumps=[]
new_matrix=copy.deepcopy(matrix)
found=0
s=0
depth=100
for x in range(0,row_length):
    curr_start=0
    for y in range(0,col_length):
        curr=matrix[y][x]
        print(curr_start,y)
        #if curr=='.':
            #curr_start+=1

        if curr=='#':
            curr_start=y+1
        if curr=='O':
            s+=(depth-curr_start)
            new_matrix[curr_start][x]='O'
            if curr_start<y:
                new_matrix[curr_start][x]='.'
            curr_start+=1

for row in matrix:
    print(''.join(row))
print("")
for row in new_matrix:
    print(''.join(row))
print(s)
