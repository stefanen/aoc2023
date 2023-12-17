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

day = '17'
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

def rev(dir):
    if dir=='<':
        return '>'
    if dir=='>':
        return '<'
    if dir=='^':
        return 'v'
    if dir=='v':
        return '^'

matrix=[[int(list(lines[y])[x]) for x in range(0,row_length)] for y in range(0,col_length)]
g = nx.DiGraph()
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        for v in itertools.product([0,1,2,3,4,5,6,7,8,9,10],['v','^','>','<']):
            node=f'{i}_{j}_{v[0]}_{v[1]}'
            neighbour_candidates=[(i-1,j,'^'),(i+1,j,'v'),(i,j-1,'<'),(i,j+1,'>')]
            for n in neighbour_candidates:
                if v[1]==rev(n[2]):
                    continue
                if v[1]==n[2] and v[0]==10:
                    continue
                if v[1]!=n[2] and v[0]<4:
                    continue
                if 0<=n[0]<len(matrix) and 0<=n[1]<len(matrix[0]):
                    c=1 if v[1]!=n[2] else v[0]+1
                    d_node=f'{n[0]}_{n[1]}_{c}_{n[2]}'
                    g.add_edge(node, d_node)
                    g[node][d_node]['weight'] = matrix[n[0]][n[1]]

best=99999999
t_nodes=[]
for v in itertools.product([1,2,3,4,5,6,7,8,9,10],['v','>']):
    t_nodes.append(f'{len(matrix)-1}_{len(matrix)-1}_{v[0]}_{v[1]}')

for t_node in t_nodes:
    s=0
    try:
        shortest_path=nx.shortest_path(g,"0_0_0_>",t_node,"weight")
        for edge in shortest_path:
            y=int(edge.split("_")[0])
            x=int(edge.split("_")[1])
            s+=matrix[y][x]
        best=min(best,s)
    except Exception as e:
        print("continuing"+str(e))

print(best-matrix[0][0])

# s=0
# for edge in shortest_path:
#     y=int(edge.split("_")[0])
#     x=int(edge.split("_")[1])
#     pmatrix[y][x]='#'
#     s+=matrix[y][x]
# print(s)
# for row in pmatrix:
#     srow=list(map(str,row))
#     print(''.join(srow))



