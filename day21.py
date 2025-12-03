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

day = '21'
p = subprocess.run("bash -c './p_data.sh " + day + " true' ")
input = open('./input_d_' + day + '.txt').read()
input = open('./input_d_' + day + '_small.txt').read()

lines=[e for e in input.split('\n')]

#REGEX
#pattern = r'.*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?'
#parsed = [(int(bid),int(ore),int(clay),int(obo),int(obc),int(geo),int(geob)) for bid,ore,clay,obo,obc,geo,geob in re.findall(pattern,input)]


#MATRIX
col_length=len(lines)-1
row_length=max([len(lines[c]) for c in range(0,col_length)])

matrix=[[list(lines[y])[x] for x in range(0,row_length)] for y in range(0,col_length)]

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        if matrix[i][j]=='S':
            start=(i,j)
            break

state=set()
state.add(start)
values=[0,0]
for s in range(0,col_length+row_length+10):
    new_state=set()
    for v in state:
        #print(v)
        i=v[0]
        j=v[1]
        neighbour_candidates=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        for n in neighbour_candidates:
            if 0<=n[0]<len(matrix) and 0<=n[1]<len(matrix[0]):
                if matrix[n[0]%col_length][n[1]%row_length]!="#":
                    new_state.add(n)

    #print(new_state)
    state=new_state
    values[s%2]=len(state)


#def solve(target):
target=202300*131+65
m=4
target=m*131+65
#target=132+131*4
state=set()
state.add(start+(0,0))



full_quads=set()
for s in range(0,target):
    new_state=set()
    for v in state:
        #print(v)
        i=v[0]
        j=v[1]
        neighbour_candidates=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        for n in neighbour_candidates:
            #if 0<=n[0]<len(matrix) and 0<=n[1]<len(matrix[0]):
            q_y=n[0]//col_length
            q_x=n[1]//row_length
            dist=abs(q_x)+abs(q_y)
            #print(f'In {(q_y,q_x)}')
            if matrix[n[0]%col_length][n[1]%row_length]!="#":
                if dist>=s//(col_length+row_length):
                #if not (dist==0 and s>col_length+row_length):
                    new_state.add(n+(q_y,q_x))
                else:
                    full_quads.add((q_y,q_x))
    #print(s,len(new_state))
    state=new_state


print(values)
c=len(state)
#print(s,len(state))
e_c=0
o_c=0
print("before",c)
for q in full_quads:
    if (q[0]+q[1])%2==0:
        e_c+=1
    else:
        o_c+=1
    c+=values[(q[0]+q[1]+1)%2]

    #return c
print(c, e_c,o_c)
#sys.exit()


# v=0
# for i in range(0,10):
#     old_v=v
#     v=solve(100+i*11)
#     print(100+i*11,v,v-old_v)
# sys.exit()

c=defaultdict(int)
for s in state:
    c[(s[2],s[3])]+=1

d=defaultdict(list)
f=defaultdict(int)
s2=0
for k,v in c.items():
    if v not in values:
        #print(k,v)
        d[v].append(k)
    else:
        print(k)
        s2+=1
print(f'full quadrant count {s2}')

print(f'After {target} steps, the max-distance-from-starting-point-quadrants have the following counts')


d2=defaultdict(list)
for k,v in d.items():
    d2[len(v)].append(k)
    print(f'edge-quadrants with exactly {k} reachable steps:{v}')


print(d2)


sys.exit()

print(d)

print(len(full_quads))
print(full_quads)

print(c)
sys.exit()

