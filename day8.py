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

day = '8'
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
for line in lines[2:]:
    if len(line)==0:
        continue
    pattern = r'.*?([A-Z]+) = .([A-Z]+)..([A-Z]+).*?'
    x,y,z = list(re.findall(pattern,line))[0]
    d[(x,'R')]=z
    d[(x,'L')]=y
    nodes.append(x)
    # g.add_edge(x,y)
    # g.add_edge(x,z)

print(d)

t=0
dirs=lines[0]
l=len(dirs)
print(l,dirs)
print(dirs[0%l],dirs[283%283])

c='AAA'

d2=dict()
#d2=result of going 283 steps

def trav(a,x):
    for i in range(x):
        n=dirs[i%l]
        a=d[(a,n)]
    return a

def trav2(a,x):
    for i in range(x):
        a=d2[a]
    return a

for n in nodes:
    d2[n]=trav(n,283)


t1=16697//283
t2=16697%283
# #print(d2)
# while c!='ZZZ':
#     n=dirs[t%l]
#     c=d[(c,n)]
#     t+=1

# print(trav(trav2('AAA',t1),t2))
# print(trav('AAA',16697))
#
snodes=list(filter(lambda x:x[2]=='A',nodes))
enodes=list(filter(lambda x:x[2]=='Z',nodes))
#
# curr='AAA'
#
seen_d=defaultdict(list)
# for t in range(0,1000000):
#     curr=trav2(curr,1)
#     seen_d[curr].append(t)

for s in snodes:
    curr=s
    for t in range(0,1000000):
        n=dirs[t%l]
        curr=d[(curr,n)]
        if curr in enodes:
            seen_d[(s,curr)].append(t+1)

print(seen_d)
print(seen_d.keys())
print(seen_d[('AAA','ZZZ')])
periods=[]
for k,v in seen_d.items():
    periodicity=v[2]-v[1]
    periods+=[(k,v[0],periodicity)]
print(periods)

print(trav('AAA',16697))
print(trav('AAA',16697+16697*3))
v=tuple(map(lambda x:x[1],periods))
print(v)
print(math.lcm(*v))

    # for e in enodes:
    #     seen_d
    #     print(s,e)




print(seen_d['ZZZ'])
# while c!='ZZZ':
#     n=dirs[t%l]
#     c=d[(c,n)]
#     t+=1

print(snodes)
# while c!='ZZZ':
#     n=dirs[t%l]
#     c=d[(c,n)]
#     t+=1

print(t)
