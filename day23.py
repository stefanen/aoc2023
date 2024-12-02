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
import matplotlib.pyplot as plt

vecadd = lambda *v: tuple(sum(x) for x in zip(*v))
sys.setrecursionlimit(10000)

day = '23'
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

matrix=[[list(lines[y])[x] for x in range(0,row_length)] for y in range(0,col_length)]

g=networkx.DiGraph()
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        curr=matrix[i][j]
        if i==0 and curr=='.':
            s=(i,j)
        if i==len(matrix)-1 and curr=='.':
            t=(i,j)


        if curr=='#':
            continue
        neighbour_candidates=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        # if curr=="^":
        #     neighbour_candidates=[(i-1,j)]
        # if curr=="v":
        #     neighbour_candidates=[(i+1,j)]
        # if curr==">":
        #     neighbour_candidates=[(i,j+1)]
        # if curr=="<":
        #     neighbour_candidates=[(i,j-1)]

        for n in neighbour_candidates:
            if 0<=n[0]<len(matrix) and 0<=n[1]<len(matrix[0]) and matrix[n[0]][n[1]]!='#':
                g.add_edge((i,j),n)

#nx.draw(g,with_labels=True)

# # Display the graph
# plt.axis('off')
# plt.show()

adjacency_dict = {node: list(g.successors(node)) for node in g.nodes()}

junctions=dict()
for k,v in adjacency_dict.items():
    if len(v)>2 or k==s or k==t:
        junctions[k]=v

print(junctions)
d=dict()

shortest_p={}

g3=nx.DiGraph()
for s2,t2 in itertools.combinations(junctions.keys(),2):
    g2=g.copy()
    for v in junctions.keys():
        if v not in [s2,t2]:
            g2.remove_node(v)
    try:
        shortest=networkx.shortest_path(g2,s2,t2)
    except Exception:
        continue
    shortest_p[(s2,t2)]=len(shortest)
    shortest_p[(t2,s2)]=len(shortest)
    print(s2,t2,len(shortest))
    g3.add_edge(s2,t2)
    g3[s2][t2]['weight']=len(shortest)-1
    g3.add_edge(t2,s2)
    g3[t2][s2]['weight']=len(shortest)-1
    #print(shortest)

#print(adjacency_dict)

curr=s
path=[]
# while True:
#     1

#sys.exit()

#print(networkx.shortest_path(g,s,t))
# best=0
# for p in networkx.all_simple_paths(g,s,t):
#     #print(p)
#     best=max(best,len(p))
#     if best==len(p):
#         res=[]
#         c=0
#         for v in p:
#             if v in junctions.keys():
#                 res.append(v)
#                 if len(res)>1:
#                     c+=shortest_p[(res[-1],res[-2])]-1
#         print(c)
#         print(res)
#         print(p)
# print(best-1)


#1262816
1262816:wq:§

c=0
best=0
for p in networkx.all_simple_paths(g3, s, t):
    m=0
    prev=None
    for v in p:
        if prev != None:
            m+=g3[v][prev]['weight']
        prev=v

    #             if v in junctions.keys():
    #                 res.append(v)
    #                 if len(res)>1:
    #                     c+=shortest_p[(res[-1],res[-2])]-1
    c+=1
    if c%1000==0:
        print(c)
    best=max(m,best)
print(best)
#print(networkx.all_simple_paths(g3, s, t,"weight"))
