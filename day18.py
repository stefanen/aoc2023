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

day = '18'
#p = subprocess.run("bash -c './p_data.sh " + day + " true' ")
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


matrix=[['.' for x in range(0,row_length)] for y in range(0,col_length)]

dirs= {
    "U":(-1,0),
    "D":(1,0),
    "L":(0,-1),
    "R":(0,1),
    "0":(0,1),
    "1":(1,0),
    "2":(0,-1),
    "3":(-1,0)
}
#
# curr=(319,55)
# corners=[curr]
# for line in lines:
#     if len(line)==0:
#         continue
#     x,y,z=tuple(line.split(' '))
#     y=int(y)
#     x=z[7:8]
#     y=int(z[2:7],16)
#     print(x,y)
#
#     matrix[curr[0]][curr[1]]='#'
#     for i in range(int(y)):
#         curr=vecadd(curr,dirs[x])
#         matrix[curr[0]][curr[1]]='#'

curr=(0,0)
corners=[curr]
for line in lines:
    if len(line)==0:
        continue
    x,y,z=tuple(line.split(' '))
    y=int(y)
    x=z[7:8]
    y=int(z[2:7],16)
    # print(x,y)
    curr=vecadd(curr,tuple(k * y for k in dirs[x]))
    corners.append(curr)



min_y=min(v[0] for v in corners)
max_y=max(v[0] for v in corners)
min_x=min(v[1] for v in corners)
max_x=max(v[1] for v in corners)
print(corners)
edges=[(x,y) for x,y in zip(corners,corners[1:])]
print(edges)
y_edges=[(x,y) for x,y in zip(corners,corners[1:]) if x[1]==y[1]]

x_edges=[(x,y) for x,y in zip(corners,corners[1:]) if x[0]==y[0]]
print(y_edges)

print(min_y,max_y,min_x,max_x)
s=0
prev_edges=set()
curr_edges=set()
expected_c=[]
for y in range(min_y,max_y+1):
    y_edges_match = sorted([edge[0][1] for edge in y_edges if min(edge[0][0],edge[1][0])<=y<=max(edge[0][0],edge[1][0])])
    if y%100000==0:
        print(y)
    #print (y, y_edges_match)
    counted_last=False
    s2=0
    for i,j in zip(y_edges_match,y_edges_match[1:]):
        if not counted_last:
            s2+=(j-i+1)
            if not ((((y,i),(y,j)) in x_edges) or (((y,j),(y,i)) in x_edges)):
                curr_edges.add((i,j))
            counted_last=True
        else:
            if ((i,j) in prev_edges) or (((y,i),(y,j)) in x_edges) or (((y,j),(y,i)) in x_edges):
                s2+=(j-i)
                if not ((((y,i),(y,j)) in x_edges) or (((y,j),(y,i)) in x_edges)):
                    curr_edges.add((i,j))
            elif len([e for e in prev_edges if (i<e[1]<=j or e[0]<j<=e[1])])>0:
                s2+=(j-i)
                if not ((((y,i),(y,j)) in x_edges) or (((y,j),(y,i)) in x_edges)):
                    curr_edges.add((i,j))
            else:
                counted_last=False
    s+=s2
    expected_c.append(s2)
    #(f'For {y} ={319+y+1} we counted {curr_edges} giving {s2}')
    prev_edges=copy.deepcopy(curr_edges)
    curr_edges.clear()

print(s)
sys.exit()

def flood_recursive(matrix):
    width = len(matrix)
    height = len(matrix[0])
    def fill(x,y,start_color,color_to_update):
        #if the square is not the same color as the starting point
        if matrix[x][y] != start_color:
            return
        #if the square is not the new color
        elif matrix[x][y] == color_to_update:
            return
        else:

            #update the color of the current square to the replacement color
            matrix[x][y] = color_to_update
            neighbors = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
            for n in neighbors:
                if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
                    fill(n[0],n[1],start_color,color_to_update)

    fill(320,56,'.','#')
    return matrix

#print(x,y,z)
flood_recursive(matrix)
s=0
actual_c=[]
for row in matrix:
    count = row.count('#')
    if count>0:
        actual_c.append(count)
    s+= count
    #print(''.join(row))

print(s)

print(expected_c)
print(actual_c)
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



