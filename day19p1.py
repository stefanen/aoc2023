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
for node in nodes:
    w="in"
    while w not in ["A","R"]:
        l=rules[w]
        for rule in l:
            if ":" not in rule:
                w=rule
            else:
                cond,t=rule.split(":")
                if ">" in cond:
                    k=cond.split('>')[0]
                    v=int(cond.split('>')[1])
                    if node[k]>v:
                        w=t
                        break
                else:
                    k=cond.split('<')[0]
                    v=int(cond.split('<')[1])
                    if node[k]<v:
                        w=t
                        break
    print(node,w)
    if w=='A':
        c+=sum([v for k,v in node.items()])
print(c)