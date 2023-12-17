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

day = '15'
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

def hash(str):
    curr=0
    for c in str:
        a=ord(c)
        curr+=a
        curr=curr*17
        curr=curr%256
    return curr

d=defaultdict(list)
for line in lines[0:1]:
    s=0
    for w in line.split(','):
        print(w, hash(w))
        pattern = r'(.*)([-=])(.*)'
        x,y,z= re.findall(pattern,w)[0]
        b=hash(x)
        if y=='=':
            found=False
            for l in d[b]:
                if l[0]==x:
                    l[1]=z
                    found=True
            if not found:
                d[b].append([x,z])
        if y=='-':
            for i in range(0,len(d[b])):
                if d[b][i][0]==x:
                    d[b]=d[b][0:i]+d[b][i+1:]
                    break
        #s+=hash(w)
        print(x,y,z)
    print(d)

s=0
for k,v in d.items():
    print(k,v)
    for i in range(0,len(v)):
        res=(k+1)*(i+1)*int(v[i][1])
        print(res)
        s+=res
print(s)


