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
import numpy as np
import networkx as nx
import operator
import time

vecadd = lambda *v: tuple(sum(x) for x in zip(*v))
sys.setrecursionlimit(10000)

day = '3'
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
matrix=[[list(lines[y])[x] for x in range(0,row_length)] for y in range(0,col_length)]
#print(matrix)
s=0
s2=0

part_num_locations=[]
#[[x_min,x_max],y], ...]
for y in range(0,col_length):
    curr_num=None
    is_symbol_near=False
    for x in range(0,row_length):
        curr_elem=matrix[y][x]
        if curr_elem in '0123456789':
            curr_num=(curr_num+curr_elem) if curr_num else curr_elem
            #print(y,x,is_symbol_near)
        else:
            if curr_num and is_symbol_near:
                print(0, curr_num)
                part_num_locations.append([[x- len(curr_num),x-1],y,curr_num])
                s+=int(curr_num)
            curr_num=None
            is_symbol_near=False
            continue



        neighbour_candidates=[(y-1,x),(y+1,x),(y,x-1),(y,x+1),(y-1,x-1),(y+1,x+1),(y-1,x+1),(y+1,x-1)]
        for n in neighbour_candidates:
            if 0<=n[0]<len(matrix) and 0<=n[1]<len(matrix[0]):
                is_symbol_near=is_symbol_near or not ((matrix[n[0]][n[1]]) in '0123456789.')


        #print(f'{curr} has {is_symbol_near}')
    if curr_num and is_symbol_near:
        print(1, curr_num)
        part_num_locations.append([[x- len(curr_num),row_length-1],y,curr_num])
        s+=int(curr_num)

print(part_num_locations)
for y in range(0,col_length):
    for x in range(0,row_length):
        curr_elem=matrix[y][x]
        if curr_elem in '*':
            adj_c=[]
            for part_num_loc in part_num_locations:
                found=False
                neighbour_candidates=[(y-1,x),(y+1,x),(y,x-1),(y,x+1),(y-1,x-1),(y+1,x+1),(y-1,x+1),(y+1,x-1)]
                for n in neighbour_candidates:
                    if 0<=n[0]<len(matrix) and 0<=n[1]<len(matrix[0]):
                        if part_num_loc[0][0]<=n[1]<=part_num_loc[0][1] and n[0]==part_num_loc[1]:
                            print(f'partnum at {part_num_loc} is adj to {(y,x)}')
                            found=True
                    #print(part_num_loc, found)
                if found:
                    adj_c.append(part_num_loc)
                    print(y,x,adj_c,part_num_loc)
            if (len(adj_c)==2):
                s2+=math.prod(map(lambda x:int(x[2]),adj_c))
            print(y,x,adj_c)

print(s2)

#print(input)
#PARSE SIMPLE
for line in lines[0:]:
    parts=line.split(' ')
    #x,y=parts[0],parts[1]
    #print(x,y)






