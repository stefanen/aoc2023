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

day = '16'
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


best=0
starting_beams=[((0,-1),(0,1)),((1,-1),(0,1))]
s_beams_e=[((y,-1),(0,1)) for y in range(0,col_length)]
s_beams_w=[((y,row_length),(0,-1)) for y in range(0,col_length)]
s_beams_n=[((col_length,x),(-1,0)) for x in range(0,row_length)]
s_beams_s=[((0,x),(1,0)) for x in range(0,row_length)]

starting_beams=s_beams_e+s_beams_s+s_beams_n+s_beams_w

for s in starting_beams:
    #print(s)
    visited=set()
    visited_dirs=set()
    #visited.add((0, 0))
    beams=[s]
    for i in range(0,100000):
        new_beams=[]
        #print(len(beams))
        if (len(beams)==0):
            break
        if i>9000:
            print("oh dear...")
            sys.exit()
        for beam in beams:
            y=beam[0][0]
            x=beam[0][1]
            dir=beam[1]

            if (0<=y<=col_length-1 and 0<=x<=row_length-1):
                visited.add((y, x))

            new_loc=vecadd((y,x),dir)
            if not (0<=new_loc[0]<=col_length-1 and 0<=new_loc[1]<=row_length-1):
                continue
            visited.add(new_loc)

            symbol=matrix[new_loc[0]][new_loc[1]]

            match(symbol,dir):

                case ('.',(1,0)):
                    new_beams.append((new_loc,(1,0)))
                case ('|',(1,0)):
                    new_beams.append((new_loc,(1,0)))
                case ('-',(1,0)):
                    new_beams.append((new_loc,(0,1)))
                    new_beams.append((new_loc,(0,-1)))
                case ('\\',(1,0)):
                    new_beams.append((new_loc,(0,1)))
                case ('/',(1,0)):
                    new_beams.append((new_loc,(0,-1)))

                case ('.',(-1,0)):
                    new_beams.append((new_loc,(-1,0)))
                case ('|',(-1,0)):
                    new_beams.append((new_loc,(-1,0)))
                case ('-',(-1,0)):
                    new_beams.append((new_loc,(0,1)))
                    new_beams.append((new_loc,(0,-1)))
                case ('\\',(-1,0)):
                    new_beams.append((new_loc,(0,-1)))
                case ('/',(-1,0)):
                    new_beams.append((new_loc,(0,1)))

                case ('.',(0,1)):
                    new_beams.append((new_loc,(0,1)))
                case ('|',(0,1)):
                    new_beams.append((new_loc,(1,0)))
                    new_beams.append((new_loc,(-1,0)))
                case ('-',(0,1)):
                    new_beams.append((new_loc,(0,1)))
                case ('\\',(0,1)):
                    new_beams.append((new_loc,(1,0)))
                case ('/',(0,1)):
                    new_beams.append((new_loc,(-1,0)))

                case ('.',(0,-1)):
                    new_beams.append((new_loc,(0,-1)))
                case ('|',(0,-1)):
                    new_beams.append((new_loc,(1,0)))
                    new_beams.append((new_loc,(-1,0)))
                case ('-',(0,-1)):
                    new_beams.append((new_loc,(0,-1)))
                case ('\\',(0,-1)):
                    new_beams.append((new_loc,(-1,0)))
                case ('/',(0,-1)):
                    new_beams.append((new_loc,(1,0)))


        beams=list(filter(lambda x:x not in visited_dirs,new_beams))
        visited_dirs=visited_dirs.union(set(beams))

    # pmatrix=copy.deepcopy(matrix)
    # for v in visited:
    #     pmatrix[v[0]][v[1]]='#'
    # for row in pmatrix:
    #     print(''.join(row))
    best=max(best,len(visited))
    #print(best)

print(best)

