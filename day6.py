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

day = '6'
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


times=[''.join(lines[0].split(' ')[1:])]
times=list(filter(lambda e:len(e)>0,times))
times=list(map(int,times))
d=[''.join(lines[1].split(' ')[1:])]
d=list(filter(lambda e:len(e)>0,d))
d=list(map(int,d))
print(times,d)

p=1
for s in range(len(d)):
    print(s,len(d))
    t=times[s]
    m=d[s]
    k=0
    for x in range(t):
        #print((t-x)*x,x,m)
        if (t-x)*x>m:
            k+=1
    #print(k)
    p*=k

print(p)

s=0
#print(input)
#PARSE SIMPLE
for line in lines[0:]:
    parts=line.split(' ')
    times=map(int,parts[1:])





