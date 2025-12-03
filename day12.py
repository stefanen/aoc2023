import math
import sys
import itertools
import functools
import copy
from typing import Iterable
import subprocess
from functools import cache
import re


vecadd = lambda *v: tuple(sum(x) for x in zip(*v))
sys.setrecursionlimit(10000)

day = '12'
#p = subprocess.run("bash -c './p_data.sh " + day + " true' ")
input = open('./input_d_' + day + '.txt').read()
#input = open('./input_d_' + day + '_small.txt').read()

lines=[e for e in input.split('\n') if len(e)>0]

#REGEX
#pattern = r'.*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?'
#parsed = [(int(bid),int(ore),int(clay),int(obo),int(obc),int(geo),int(geob)) for bid,ore,clay,obo,obc,geo,geob in re.findall(pattern,input)]


#MATRIX
col_length=len(lines)-1
row_length=max([len(lines[c]) for c in range(0,col_length)])
#matrix=[[list(lines[y])[x] if len(list(lines[y]))>x else " " for x in range(0,row_length)] for y in range(0,col_length)]
#matrix=[[list(lines[y])[x] for x in range(0,row_length)] for y in range(0,col_length)]

print(col_length, row_length)

@cache
def solve(str,k):
    l=list(k)
    #print(str,l)
    if len(l)==0:
        return 1 if re.match("^[?.]*$" ,str) else 0
    t=l[0]
    for i in range(len(str)):
        c=str[i]
        if c=='#':
            if i+t>len(str):
                return 0
            elif i+t==len(str):
                return 1 if re.match("^[?#]*$" ,str[i:i+t]) and len(l)==1 else 0
            elif re.match("^[?#]*[.?]$" ,str[i:i+t+1]):
                return solve(str[i+t+1:],tuple(l[1:]))
            else:
                return 0
        if c=='?':
            h_str='#'+str[i+1:]
            p_str='.'+str[i+1:]
            solve1 = solve(h_str, tuple(l))

            solve2 = solve(p_str, tuple(l))
            #print(h_str, solve1,p_str,solve2,l)
            return solve1 + solve2
    return 0

            #print(str[i:i+t])



s=0
for line in lines[0:]:
    r,y=line.split(' ');
    l=list(map(int,y.split(',')))
    r=r+'?'
    r=r*5
    r=r[0:-1]
    l=l*5
    print(r,l)
    res = solve(r, tuple(l))
    print(res)
    s+= res

print(s)
#print(solve("#.#??",[1]))

