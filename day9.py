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

day = '9'
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
print(col_length, row_length)
#matrix=[[list(lines[y])[x] if len(list(lines[y]))>x else " " for x in range(0,row_length)] for y in range(0,col_length)]
#matrix=[[list(lines[y])[x] for x in range(0,row_length)] for y in range(0,col_length)]
#print(matrix)


g=networkx.DiGraph()
d=dict()
nodes=[]
nums=[[[]] for i in range(col_length)]
i=0
s=0
for line in lines[0:]:
    if len(line)==0:
        continue
    #pattern = r'.*?([A-Z]+) = .([A-Z]+)..([A-Z]+).*?'
    #x,y,z = list(re.findall(pattern,line))[0]
    nums[i][0]+=list(map(int,line.split(' ')))
    curr=nums[i][0]
    print(nums)
    while not all(v == 0 for v in curr):
        curr=[y-x for x,y in zip(curr,curr[1:])]
        nums[i].append(curr)
    nums[i][len(nums[i])-1].insert(0,0)
    for k in reversed(range(len(nums[i])-1)):
        new=nums[i][k][0]-nums[i][k+1][0]
        nums[i][k].insert(0,new)
    print(nums)
    s+=nums[i][0][0]
    i+=1
print(s)