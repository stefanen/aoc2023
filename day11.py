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

day = '11'
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
#print(matrix[9])
new_matrix=copy.deepcopy(matrix)
found=0
for y in range(0,col_length):
    curr=matrix[y]
    if all('.'==v for v in curr):
        new_matrix.insert(y+found,['.']*row_length)
        y_jumps.append(y+found)
        found+=1

matrix=new_matrix
for row in matrix:
    print(''.join(row))

new_matrix=copy.deepcopy(matrix)
found=0
for x in range(0,row_length):
    curr=[matrix[y][x] for y in range(0,len(matrix))]
    if all('.'==v for v in curr):
        print(x)
        for row in new_matrix:
            row.insert(x+found,'.')
        x_jumps.append(x+found)
        found+=1

matrix=new_matrix
for row in matrix:
    print(''.join(row))

state=[]
for y in range(0,len(matrix)):
    for x in range(0,len(matrix[0])):
        curr=matrix[y][x]
        if curr=='#':
            state.append((y,x))


print(x_jumps)
print(y_jumps)

print(state)
s=0
for y,x in itertools.combinations(state,2):
    min_y=min(x[0],y[0])
    max_y=max(x[0],y[0])
    y_jump_count=len(list(filter(lambda y:max_y>y>min_y,y_jumps)))
    print(y_jump_count)

    min_x=min(x[1],y[1])
    max_x=max(x[1],y[1])
    x_jump_count=len(list(filter(lambda x:max_x>x>min_x,x_jumps)))
    print(x_jump_count)

    s+=(abs(x[0]-y[0])+abs(x[1]-y[1]))
    s+=x_jump_count*999998
    s+=y_jump_count*999998
# for y in range(0,col_length):
#     for x in range(0,row_length):
#         #print(y,x)
#         curr=matrix[y][x]
#         if curr=='#':
#             print(curr)
#

print(s)