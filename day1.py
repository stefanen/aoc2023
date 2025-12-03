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
import numpy as np
import networkx as nx
import operator
import time

vecadd = lambda *v: tuple(sum(x) for x in zip(*v))
sys.setrecursionlimit(10000)

day = '1'
#p = subprocess.run("bash -c './p_data.sh " + day )
input = open('./input_d_' + day + '.txt').read()
#input = open('./1.txt').read()

lines=[e for e in input.split('\n')]

#REGEX
#pattern = r'.*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?'
#parsed = [(int(bid),int(ore),int(clay),int(obo),int(obc),int(geo),int(geob)) for bid,ore,clay,obo,obc,geo,geob in re.findall(pattern,input)]


#MATRIX
col_length=len(lines)-1
row_length=max([len(lines[c]) for c in range(0,col_length)])
print(col_length, row_length)
#matrix=[[list(lines[y])[x] if len(list(lines[y]))>x else " " for x in range(0,row_length)] for y in range(0,col_length)]
#matrix=[[list(lines[y])[x] for x in range(0,row_length)] for y in range(0,col_length)]
#print(matrix)



print(input)
#PARSE SIMPLE

r=0
s=50
prev_c=0
prev_m = 50
for line in lines[0:]:
    if len(line)==0:
        continue

    

    if line[0]=='R':
        s+=int(line[1:])
    else:
        s-=int(line[1:])

  
    new_m = s%100
    new_c = s//100

    diff=new_c-prev_c
  
    if new_m != 0 and prev_m != 0:
        r+=abs(diff)
    elif new_m == 0 and diff<0:
        r+=1+abs(diff)
    elif new_m == 0 and diff>0:
        r+=1+abs(diff-1)
    elif new_m == 0 and diff==0:
        r+=1
    elif prev_m == 0 and diff<0:
        r+=abs(diff+1)
    elif prev_m == 0 and diff>0:
        r+=abs(diff)
    else:
        r+=0 

    prev_m=new_m
    prev_c=new_c

    print(s,diff, r)
print(r)




