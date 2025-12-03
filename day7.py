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

day = '7'
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
#matrix=[[list(lines[y])[x] for x in range(0,row_length)] for y in range(0,col_length)]
#print(matrix)



s=0
cards=[]
#print(input)
#PARSE SIMPLE
for line in lines[0:]:
    if len(line)==0:
        continue
    parts=line.split(' ')
    card=parts[0]
    bid=int(parts[1])
    cardc=reversed(sorted(list(map(str,Counter(card).values()))))
    x=list(map(int,cardc))
    print("b",x)
    print(card,card.count('J'))
    y=card.count('J')
    if 5>y>0:
        if x.index(y)==0:
            x[1]+=y
            x[0]-=y
        else:
            x[0]+=y
            x[x.index(y)]-=y
    cardc=reversed(sorted(list(map(str,x))))
    #print("a",list(cardc))

    cardv=int(''.join(cardc).ljust(5,'0'))
    print(cardv)
    card=card.replace('A','E');
    card=card.replace('K','D');
    card=card.replace('Q','C');
    card=card.replace('J','1');
    card=card.replace('T','A');
    hexv='0x'+card
    print(cardv,int(hexv,0))
    sort_v=cardv*10000000+int(hexv,0)
    print(card,bid,sort_v)
    cards+=[(bid,sort_v)]

print(cards)
cards.sort(key=lambda x: x[1])
print(cards)

i=0
s=0
for c in cards:
    i+=1
    s+=i*c[0]
    #print(s)

print(s)



