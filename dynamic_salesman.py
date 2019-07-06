# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:35:10 2019

@author: DSU
"""

import math
import random

#LOC_COUNT = 8
PLANE_LENGTH = 1000

mem = [[None]*(1<<LOC_COUNT)]*LOC_COUNT
paths = [[[]]*(1<<LOC_COUNT)]*LOC_COUNT

"""
coordinates = [(random.randrange(PLANE_LENGTH), random.randrange(PLANE_LENGTH)\
                ) for i in range(LOC_COUNT)]
distances = []
for (x_a, y_a) in coordinates:
    distances.append([math.hypot(x_b - x_a, y_b - y_a) for (x_b, y_b) in\
                      coordinates])
"""

def tsp(i, S, path):
    if S == ((1 << LOC_COUNT) - 1):
        return distances[i][0], paths[i][0]
    if mem[i][S] != None:
        return mem[i][S], paths[i][S]
    
    res = math.inf
    for j in range(LOC_COUNT):
        if S & (1 << j):
            continue
        
        tmp_res, tmp_path = tsp(j, S | (1 << j), path+[j])
        if res < distances[i][j] + tmp_res:
            pass
        else:
            res = distances[i][j] + tmp_res
            path = tmp_path + [j]
    
    mem[i][S] = res
    paths[i][S] = path
    return res, path

if __name__ == '__main__':
    tmp_res, tmp_path = tsp(0, 1<<0, [])
    print(tmp_path)
    print(tmp_res)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    