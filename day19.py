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
import matplotlib.pyplot as plt
import re
import aoc
import networkx
import numpy as np
import networkx as nx
import operator
import time
import json
from pyvis.network import Network

vecadd = lambda *v: tuple(sum(x) for x in zip(*v))
sys.setrecursionlimit(10000)

day = '19'
p = subprocess.run("bash -c './p_data.sh " + day + " true' ")
input = open('./input_d_' + day + '.txt').read()
#input = open('./input_d_' + day + '_small.txt').read()

lines=[e for e in input.split('\n')]

#REGEX
#pattern = r'.*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?'
#parsed = [(int(bid),int(ore),int(clay),int(obo),int(obc),int(geo),int(geob)) for bid,ore,clay,obo,obc,geo,geob in re.findall(pattern,input)]


#MATRIX
#col_length=len(lines)-1
#row_length=max([len(lines[c]) for c in range(0,col_length)])

col_length=1000
row_length=1000

g = nx.DiGraph()

nodes=[]
rules=dict()
objects=False
for line in lines:
    if line=="":
        objects=True
        continue
    #print(line)
    if not objects:
        x,y=line.split('{')
        r=y[:-1].split(',')
        rules[x]=r
        print(x,r)
    else:
        node=dict()
        parts=line[1:-1].split(",")
        for p in parts:
            x,y=p.split("=")
            node[x]=int(y)
        print(node)
        nodes.append(node)
c=0
node=nodes[0]
w="in"
q=[(("in",("True",)),)]

visited=set()

res=0
while len(q)>0:
    w=q.pop()
    l=rules[w[-1][0]]
    conds=()
    for r in l:
        t=r.split(':')[-1]
        cond="True"
        if ":" in r:
            cond=r.split(':')[0]

        if t not in ["A","R"]:
            q.insert(0,w+((t,conds+(cond,)),))
        if t == 'A':
            print(type(w+((t,conds+(cond,)),)), w+((t,conds+(cond,)),))
            visited.add(w+((t,conds+(cond,)),))
        conds=conds+("!"+cond,)
    #print(q)

print(visited)
c=0
for path in visited:
    conds=[]
    for v in path:
        print(path,v)
        for c in v[1]:
            conds.append(c)
    print(conds)
    limits=[1,4000,1,4000,1,4000,1,4000]
    for c in conds:
        if c[0] in "xmas":
            k=c[0]
            o=c[1]
            v=int(c[2:])
        elif c[0]=='!':
            k=c[1]
            o=">=" if c[2] == "<" else "<="
            v=int(c[3:])
        else:
            continue
        print(k,o,v)
        match (k,o):
            case ('x','<'):
                index=1
                v=v-1
            case ('x','<='):
                index=1
            case ('x','>'):
                index=0
                v=v+1
            case ('x','>='):
                index=0

            case ('m','<'):
                index=3
                v=v-1
            case ('m','<='):
                index=3
            case ('m','>'):
                index=2
                v=v+1
            case ('m','>='):
                index=2

            case ('a','<'):
                index=5
                v=v-1
            case ('a','<='):
                index=5
            case ('a','>'):
                index=4
                v=v+1
            case ('a','>='):
                index=4

            case ('s','<'):
                index=7
                v=v-1
            case ('s','<='):
                index=7
            case ('s','>'):
                index=6
                v=v+1
            case ('s','>='):
                index=6






        limits[index]=v
    print(limits)
    res+=math.prod([limits[i+1]-limits[i]+1 for i in range(0,8,2)])

print(res)










# while w not in ["A","R"]:
#     l=rules[w]
#     for rule in l:
#         if ":" not in rule:
#             w=rule
#         else:
#             cond,t=rule.split(":")
#             if ">" in cond:
#                 k=cond.split('>')[0]
#                 v=int(cond.split('>')[1])
#                 if node[k]>v:
#                     w=t
#                     break
#             else:
#                 k=cond.split('<')[0]
#                 v=int(cond.split('<')[1])
#                 if node[k]<v:
#                     w=t
#                     break
