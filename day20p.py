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
pos = nx.spring_layout(g)

# Draw the nodes
#nx.draw_networkx_nodes(g, pos)

# Draw the edges with arrows
#nx.draw_networkx_edges(g, pos)

nx.draw(g,with_labels=True)

# Display the graph
plt.axis('off')
plt.show()
sys.exit()


# Create a pyvis network
pyvis_graph = Network()
pyvis_graph.from_nx(g)

# Enable physics for dragging nodes
physics_options ="""
var options = {
    "physics": {
        "enabled": false,
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