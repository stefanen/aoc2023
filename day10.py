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

day = '10'
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
big_matrix=[['?' for x in range(0,2*row_length)] for y in range(0,2*col_length)]

print(col_length, row_length)

#print(matrix[9])

for y in range(0,col_length):
    for x in range(0,row_length):
        #print(y,x)
        curr=matrix[y][x]
        if curr=='S':
            start_pos=(y,x)
#start_shape='J'
#print(matrix[start_pos[0]][start_pos[1]])


out_dirs={
    ('E','J'):'N',
    ('E','-'):'E',
    ('E','7'):'S',

    ('S','|'):'S',
    ('S','J'):'W',
    ('S','L'):'E',

    ('W','-'):'W',
    ('W','F'):'S',
    ('W','L'):'N',

    ('N','|'):'N',
    ('N','F'):'E',
    ('N','7'):'W'

}

#print(next_out_dir('E','J'))

i=0
#dirs=['E','S','W','N']

path=[]
def trav(curr,out_dir):
    global i
    global out_dirs
    global big_matrix
    global path
    path.append(curr)
    if out_dir=='E':
        next=(curr[0],curr[1]+1)
    elif out_dir=='S':
        next=(curr[0]+1,curr[1])
    elif out_dir=='W':
        next=(curr[0],curr[1]-1)
    elif out_dir=='N':
        next=(curr[0]-1,curr[1])
    next_shape=matrix[next[0]][next[1]]
    i+=1
    new_dir = out_dirs[(out_dir, next_shape)]



    match (out_dir,new_dir):
        case ('E','N'):
            big_matrix[2*curr[0]][2*curr[1]+2]=big_matrix[2*curr[0]][2*curr[1]+1]
            big_matrix[2*curr[0]+1][2*curr[1]+2]=big_matrix[2*curr[0]+1][2*curr[1]+1]
            big_matrix[2*curr[0]][2*curr[1]+3]=big_matrix[2*curr[0]+1][2*curr[1]+1]
            big_matrix[2*curr[0]+1][2*curr[1]+3]=big_matrix[2*curr[0]+1][2*curr[1]+1]
        case ('E','E'):
            big_matrix[2*curr[0]][2*curr[1]+2]=big_matrix[2*curr[0]][2*curr[1]+1]
            big_matrix[2*curr[0]+1][2*curr[1]+2]=big_matrix[2*curr[0]+1][2*curr[1]+1]
            big_matrix[2*curr[0]][2*curr[1]+3]=big_matrix[2*curr[0]][2*curr[1]+1]
            big_matrix[2*curr[0]+1][2*curr[1]+3]=big_matrix[2*curr[0]+1][2*curr[1]+1]
        case ('E','S'):
            big_matrix[2*curr[0]][2*curr[1]+2]=big_matrix[2*curr[0]][2*curr[1]+1]
            big_matrix[2*curr[0]+1][2*curr[1]+2]=big_matrix[2*curr[0]+1][2*curr[1]+1]
            big_matrix[2*curr[0]][2*curr[1]+3]=big_matrix[2*curr[0]][2*curr[1]+1]
            big_matrix[2*curr[0]+1][2*curr[1]+3]=big_matrix[2*curr[0]][2*curr[1]+1]

        case ('S','S'):
            big_matrix[2*curr[0]+2][2*curr[1]]=big_matrix[2*curr[0]+1][2*curr[1]]
            big_matrix[2*curr[0]+2][2*curr[1]+1]=big_matrix[2*curr[0]+1][2*curr[1]+1]
            big_matrix[2*curr[0]+3][2*curr[1]]=big_matrix[2*curr[0]+1][2*curr[1]]
            big_matrix[2*curr[0]+3][2*curr[1]+1]=big_matrix[2*curr[0]+1][2*curr[1]+1]
        case ('S','E'):
            big_matrix[2*curr[0]+2][2*curr[1]]=big_matrix[2*curr[0]+1][2*curr[1]]
            big_matrix[2*curr[0]+2][2*curr[1]+1]=big_matrix[2*curr[0]+1][2*curr[1]+1]
            big_matrix[2*curr[0]+3][2*curr[1]]=big_matrix[2*curr[0]+1][2*curr[1]]
            big_matrix[2*curr[0]+3][2*curr[1]+1]=big_matrix[2*curr[0]+1][2*curr[1]]
        case ('S','W'):
            big_matrix[2*curr[0]+2][2*curr[1]]=big_matrix[2*curr[0]+1][2*curr[1]]
            big_matrix[2*curr[0]+2][2*curr[1]+1]=big_matrix[2*curr[0]+1][2*curr[1]+1]
            big_matrix[2*curr[0]+3][2*curr[1]]=big_matrix[2*curr[0]+1][2*curr[1]+1]
            big_matrix[2*curr[0]+3][2*curr[1]+1]=big_matrix[2*curr[0]+1][2*curr[1]+1]
        #
        case ('W','W'):
            big_matrix[2*curr[0]][2*curr[1]-1]=big_matrix[2*curr[0]][2*curr[1]]
            big_matrix[2*curr[0]+1][2*curr[1]-1]=big_matrix[2*curr[0]+1][2*curr[1]]
            big_matrix[2*curr[0]][2*curr[1]-2]=big_matrix[2*curr[0]][2*curr[1]]
            big_matrix[2*curr[0]+1][2*curr[1]-2]=big_matrix[2*curr[0]+1][2*curr[1]]
        case ('W','S'):
            big_matrix[2*curr[0]][2*curr[1]-1]=big_matrix[2*curr[0]][2*curr[1]]
            big_matrix[2*curr[0]+1][2*curr[1]-1]=big_matrix[2*curr[0]+1][2*curr[1]]
            big_matrix[2*curr[0]][2*curr[1]-2]=big_matrix[2*curr[0]][2*curr[1]]
            big_matrix[2*curr[0]+1][2*curr[1]-2]=big_matrix[2*curr[0]][2*curr[1]]
        case ('W','N'):
            big_matrix[2*curr[0]][2*curr[1]-1]=big_matrix[2*curr[0]][2*curr[1]]
            big_matrix[2*curr[0]+1][2*curr[1]-1]=big_matrix[2*curr[0]+1][2*curr[1]]
            big_matrix[2*curr[0]][2*curr[1]-2]=big_matrix[2*curr[0]+1][2*curr[1]]
            big_matrix[2*curr[0]+1][2*curr[1]-2]=big_matrix[2*curr[0]+1][2*curr[1]]
        #
        case ('N','N'):
            big_matrix[2*curr[0]-1][2*curr[1]]=big_matrix[2*curr[0]][2*curr[1]]
            big_matrix[2*curr[0]-1][2*curr[1]+1]=big_matrix[2*curr[0]][2*curr[1]+1]
            big_matrix[2*curr[0]-2][2*curr[1]]=big_matrix[2*curr[0]][2*curr[1]]
            big_matrix[2*curr[0]-2][2*curr[1]+1]=big_matrix[2*curr[0]][2*curr[1]+1]

        case ('N','E'):
            big_matrix[2*curr[0]-1][2*curr[1]]=big_matrix[2*curr[0]][2*curr[1]]
            big_matrix[2*curr[0]-1][2*curr[1]+1]=big_matrix[2*curr[0]][2*curr[1]+1]
            big_matrix[2*curr[0]-2][2*curr[1]]=big_matrix[2*curr[0]][2*curr[1]]
            big_matrix[2*curr[0]-2][2*curr[1]+1]=big_matrix[2*curr[0]][2*curr[1]]
        case ('N','W'):
            big_matrix[2*curr[0]-1][2*curr[1]]=big_matrix[2*curr[0]][2*curr[1]]
            big_matrix[2*curr[0]-1][2*curr[1]+1]=big_matrix[2*curr[0]][2*curr[1]+1]
            big_matrix[2*curr[0]-2][2*curr[1]]=big_matrix[2*curr[0]][2*curr[1]+1]
            big_matrix[2*curr[0]-2][2*curr[1]+1]=big_matrix[2*curr[0]][2*curr[1]+1]

    return (next, new_dir)


curr=start_pos
#fake
curr_dir='E'
matrix[start_pos[0]][start_pos[1]]='F'

#real
curr_dir='N'
matrix[start_pos[0]][start_pos[1]]='J'
big_matrix[2*start_pos[0]][2*start_pos[1]]='O'
big_matrix[2*start_pos[0]][2*start_pos[1]+1]='I'
big_matrix[2*start_pos[0]+1][2*start_pos[1]]='I'
big_matrix[2*start_pos[0]+1][2*start_pos[1]+1]='I'

#p2fake
# curr_dir='S'
# matrix[start_pos[0]][start_pos[1]]='7'
# big_matrix[2*start_pos[0]][2*start_pos[1]]='O'
# big_matrix[2*start_pos[0]][2*start_pos[1]+1]='O'
# big_matrix[2*start_pos[0]+1][2*start_pos[1]]='I'
# big_matrix[2*start_pos[0]+1][2*start_pos[1]+1]='O'


while True:
    curr,curr_dir=trav(curr,curr_dir)
    if curr==start_pos:
        break
#print(i//2)
print(path)

new_matrix=copy.deepcopy(matrix)
for y in range(0,col_length):
    for x in range(0,row_length):
        curr=matrix[y][x]
        if (y,x) in path:
            new_matrix[y][x]=curr
        else:
            new_matrix[y][x]=' '




for row in new_matrix:
    print(''.join(row))

for row in big_matrix:
    print(''.join(row))

last='?'
s=0
for row in big_matrix:
    active_interval=False
    for e in row:
        if e=='?' and last=='I':
            active_interval=True
        if e!='?':
            active_interval=False
        last=e
        if active_interval:
            s+=1
print(s//4)



# g=networkx.DiGraph()
# d=dict()
# nodes=[]
# nums=[[[]] for i in range(col_length)]
# i=0
# s=0
# for line in lines[0:]:
#     if len(line)==0:
#         continue
#     #pattern = r'.*?([A-Z]+) = .([A-Z]+)..([A-Z]+).*?'
#     #x,y,z = list(re.findall(pattern,line))[0]
#     nums[i][0]+=list(map(int,line.split(' ')))
#     curr=nums[i][0]
#     print(nums)
#     while not all(v == 0 for v in curr):
#         curr=[y-x for x,y in zip(curr,curr[1:])]
#         nums[i].append(curr)
#     nums[i][len(nums[i])-1].insert(0,0)
#     for k in reversed(range(len(nums[i])-1)):
#         new=nums[i][k][0]-nums[i][k+1][0]
#         nums[i][k].insert(0,new)
#     print(nums)
#     s+=nums[i][0][0]
#     i+=1
# print(s)