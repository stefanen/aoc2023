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

day = '5'
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

#print(input)
#PARSE SIMPLE
seeds=[]
c=defaultdict(list)
for line in lines[0:]:
    parts=line.split(' ')
    if len(parts)<=1:
        continue

    if parts[0]=="seeds:":
        seeds=list(map(int,parts[1:]))
    elif parts[1]=="map:":
        curr_s=parts[0].split('-to-')[0]
        curr_d=parts[0].split('-to-')[1]
        print(curr_s,curr_d)
        c[curr_s]+=[curr_d]
    else:
        c[curr_s]+=[list(map(int,parts[0:]))]

print(seeds)
print(c)

def conv(s_type,val):
    global c
    if s_type=="location":
        return val
    d_type=c[s_type][0]
    for r in c[s_type][1:]:
        if (r[1]<=val<r[1]+r[2]):
            new_v = val - (r[1] - r[0])
            #print(new_v,d_type)
            return conv(d_type, new_v)
    return conv(d_type,val)

print(conv('seed',3454726063-1))
print(conv('seed',3454726063))
print(conv('seed',3454726063+1))


endpoints=[]
#translations=[]

v=c["humidity"]
for a in v[1:]:
    endpoints+=[a[1],a[1]+a[2]-1]

for k,v in list(reversed(c.items()))[1:]:
    new_endpoints=[]
    for a in v[1:]:
        t=a[1]-a[0]
        x_min=a[1]
        x_max=a[1]+a[2]-1
        new_endpoints+=[x_min,x_max]
        for e in endpoints:
            if x_min-t<=e<=x_max-t:
                new_endpoints+=[e+t]
            #which x map to e?

    endpoints=new_endpoints+endpoints
        #translations+=[a[2]]
    #print(k,v)
#print(translations)

endpoints_s=sorted(list(set(endpoints)))

print(endpoints_s)
#sys.exit()

t_seeds=[]
pair_c=0
best=99999999999999999
for seed_pair in zip(seeds[::2],seeds[1::2]):
    pair_c+=1
    # if (pair_c!=9):
    #     continue
    # print(pair_c)
    # print(seed_pair)
    min_p=seed_pair[0]
    max_p=seed_pair[0]+seed_pair[1]-1
    #
    # for i in range(min_p,max_p+1,1000):
    # for i in range(3454726125-1000,3454726125+1000,1):
    #     #i+=1000000
    #     res=conv('seed',i)
    #     if res<best:
    #         print(f"new best {res} for {i} in {pair_c}")
    #         best=res
        #best=min(best,conv('seed',i))
        #print(conv('seed',i))

#new best 1240097 for 3454726125 in 9
#new best 1240697 for 3454726725 in 9

    #t_seeds.append(min_p)
    #t_seeds+=list(range(min_p,max_p+1))
    t_seeds.append(min_p+1)
    t_seeds.append(max_p)
    t_seeds.append(max_p-1)
    for e in endpoints_s:
        if min_p<e<max_p:
            t_seeds.append(e)
            t_seeds.append(e+1)
            t_seeds.append(e-1)

#sys.exit()

print("test")
print(endpoints_s)

#print(t_seeds)


print(min(map(lambda x:conv('seed',x),t_seeds)))
#print(conv('seed',14))






