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
from pyvis.network import Network

vecadd = lambda *v: tuple(sum(x) for x in zip(*v))
sys.setrecursionlimit(10000)

day = '20'
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

nodes=dict()
for line in lines:
    if len(line)==0:
        continue
    pattern = r'(.*) -> (.*)'
    s,d=re.findall(pattern,line)[0]
    nodes[s[1:]]=[s[0],s,0,dict(),[]]

for line in lines:
    if len(line)==0:
        continue
    pattern = r'(.*) -> (.*)'
    s,d=re.findall(pattern,line)[0]
    t=s[0]
    n=s[1:]
    d=list(map(lambda x:x.strip(),d.split(",")))
    print(t,n,d)
    for v in d:
        if not v in nodes:
            nodes[v]=['O',v,0,dict(),[]]

        if nodes[v][0]=='&':
            nodes[v][3][n]='l'


        g.add_edge(nodes[n][1],nodes[v][1])
        nodes[n][4].append(v)


orig_nodes=copy.deepcopy(nodes)
print(nodes)

hc=0
lc=0


#nt, kx, rc, mg
values=defaultdict(int)

for i in range(0,10000000):
    pulse_queue=[('l','mg',None),('l','rc',None),('l','kx',None),('l','nt',None)]
    #pulse_queue=[('l','c',None),('l','b',None),('l','a',None)]

    # tc=0
    # for k,v in nodes['xq'][3].items():
    #     if v=='h':
    #         tc+=1
    #         #print(i)
    # if tc>7:
    #     print(i)
    #     print(nodes['xq'][3])
    #         #sys.exit()
    # print([
    #     nodes['nt'][2],
    #     nodes['cx'][2],
    #     nodes['qh'][2],
    #     nodes['ln'][2],
    #     nodes['mq'][2],
    #     nodes['hs'][2],
    #     nodes['sl'][2],
    #     nodes['zl'][2],
    #     nodes['nj'][2],
    #     nodes['pt'][2],
    #     nodes['gt'][2],
    #     nodes['hg'][2],
    # ])
    # print(i)

    # if i>100:
    #     sys.exit()

    lc+=1
    while len(pulse_queue)>0:
        p=pulse_queue.pop()
        pt=p[0]
        if pt=='l':
            lc+=1
        else:
            hc+=1
        d=p[1]
        f=p[2]

        for y in ['sp','xt','zv','lk']:

            if pt=='l' and d==y:
                #print(nodes['dg'][3])
                if y not in values:
                    values[y]=i+1
                    print(i+1)
                    p=1
                    for j in values.values():
                        p=p*j
                        print(p)
            #sys.exit()
        if nodes[d][0]=='%':
            if pt=='l':
                s=nodes[d][2]
                if s==0:
                    nodes[d][2]=1
                    for v in nodes[d][4]:
                        pulse_queue.insert(0,('h',v,d))
                else:
                    nodes[d][2]=0
                    for v in nodes[d][4]:
                        pulse_queue.insert(0,('l',v,d))
        elif nodes[d][0]=='&':
            nodes[d][3][f]=pt
            all_high=True
            for k,v in nodes[d][3].items():
                if v!='h':
                    all_high=False
            for v in nodes[d][4]:
                pulse_queue.insert(0,('l' if all_high else 'h',v,d))

print((lc)*hc)
sys.exit()


# Create a pyvis network
pyvis_graph = Network()
pyvis_graph.from_nx(g)

# Enable physics for dragging nodes
physics_options ="""
var options = {
    "physics": {
        "enabled": true,
        "barnesHut": {
            "springLength": 200
        }
    }
}
"""
pyvis_graph.set_options(physics_options)
print("ok")
# Save the graph as an HTML file
pyvis_graph.show('mygraph.html',notebook=False)