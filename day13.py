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

day = '13'
p = subprocess.run("bash -c './p_data.sh " + day + " true' ")
input = open('./input_d_' + day + '.txt').read()
#input = open('./input_d_' + day + '_small.txt').read()

s=0
parts=[e for e in input.split('\n\n')]
for part in parts:
    lines=[e for e in part.split('\n') if len(e)>0]
    col_length=len(lines)
    row_length=max([len(lines[c]) for c in range(0,col_length)])
    #matrix=[[list(lines[y])[x] if len(list(lines[y]))>x else " " for x in range(0,row_length)] for y in range(0,col_length)]
    matrix=[[list(lines[y])[x] for x in range(0,row_length)] for y in range(0,col_length)]
    print(matrix)
    print(col_length, row_length)

    #test for horizontals
    for y in range(0,col_length):
        if y==col_length-1:
            continue
        min_d=min(1+y-0,(col_length-1)-y)
        bad_count=0
        #print(min_d)
        for i in range(0,min_d):
            for x in range(0,row_length):
                #print(f'testing {y,x} with delta {i}')
                if matrix[y-i][x]!=matrix[y+i+1][x]:
                    bad_count+=1

        if bad_count==0:
            print(f"h mirror row {y}")

        elif bad_count==1:
            s+=(y+1)*100
            print(f"almost h mirror row {y}")
    #test for verticals
    for x in range(0,row_length):
        if x==row_length-1:
            continue
        min_d=min(1+x-0,(row_length-1)-x)
        bad_count=0
        #print(min_d)
        for i in range(0,min_d):
            for y in range(0,col_length):
                #print(f'testing {y,x} with delta {i}')
                if matrix[y][x-i]!=matrix[y][x+i+1]:
                    bad_count+=1
        if bad_count==0:
            print(f"v mirror row {x}")
        elif bad_count==1:
            s+=(x+1)
            print(f"almost v mirror col {x}")


print(s)

