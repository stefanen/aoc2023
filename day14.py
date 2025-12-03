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

day = '14'
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
#matrix=[[list(lines[y])[x] if len(list(lines[y]))>x else " " for x in range(0,row_length)] for y in range(0,col_length)]
matrix=[[list(lines[y])[x] for x in range(0,row_length)] for y in range(0,col_length)]

print(col_length, row_length)

y_jumps=[]
x_jumps=[]
found=0
s=0
depth=100

def stepN(matrix):
    new_matrix=copy.deepcopy(matrix)

    for x in range(0,row_length):
        curr_start=0
        for y in range(0,col_length):
            curr=matrix[y][x]

            if curr=='#':
                curr_start=y+1
            if curr=='O':
                #s+=(depth-curr_start)
                new_matrix[curr_start][x]='O'
                if curr_start<y:
                    new_matrix[y][x]='.'
                curr_start+=1
    return new_matrix

def stepS(matrix):
    new_matrix=copy.deepcopy(matrix)

    for x in range(0,row_length):
        curr_start=depth-1
        for y in reversed(range(0,col_length)):
            curr=matrix[y][x]

            if curr=='#':
                curr_start=y-1
            if curr=='O':
                #s+=(depth-curr_start)
                new_matrix[curr_start][x]='O'
                if curr_start>y:
                    new_matrix[y][x]='.'
                curr_start-=1
    return new_matrix

def stepW(matrix):
    new_matrix=copy.deepcopy(matrix)

    for y in range(0,col_length):
        curr_start=0
        for x in range(0,row_length):
            curr=matrix[y][x]

            if curr=='#':
                curr_start=x+1
            if curr=='O':
                #s+=(depth-curr_start)
                new_matrix[y][curr_start]='O'
                if curr_start<x:
                    new_matrix[y][x]='.'
                curr_start+=1
    return new_matrix

def stepE(matrix):
    new_matrix=copy.deepcopy(matrix)

    for y in range(0,col_length):
        curr_start=depth-1
        for x in reversed(range(0,row_length)):
            curr=matrix[y][x]

            if curr=='#':
                curr_start=x-1
            if curr=='O':
                #s+=(depth-curr_start)
                new_matrix[y][curr_start]='O'
                if curr_start>x:
                    new_matrix[y][x]='.'
                curr_start-=1
    return new_matrix

for row in matrix:
    print(''.join(row))
print("")
for row in stepN(matrix):
    print(''.join(row))
print("")
for row in stepS(matrix):
    print(''.join(row))
print("")
for row in stepW(matrix):
    print(''.join(row))
print("")
for row in stepE(matrix):
    print(''.join(row))
print("")

target=1000000000
d=defaultdict(list)
for i in range(1,1000):
    matrix=stepE(stepS(stepW(stepN(matrix))))
    s=''.join([''.join(row) for row in matrix])
    d[s].append(i)
    if len(d[s])>1:
        print("loop")
        print(s,d[s])
        diff=d[s][1]-d[s][0]
        if (target-i)%diff==0:
            print("done")
            print(s)
            c=0
            for y in range(0,col_length):
                for x in range(0,row_length):
                    curr=matrix[y][x]
                    if curr=='O':
                        c+=(depth-y)
            print(c)
            break;
        #break


#print(s)
