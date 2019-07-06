# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:51:49 2019

@author: DSU
"""

import itertools
import math

DISPLAY = False

if __name__ == '__main__':
    locations = [i for i in range(1, LOC_COUNT)]
    perm = itertools.permutations(locations, save_one)
    
    min_path = ()
    min_dist = math.inf
    for tup_path in perm:
        cur_path = [0]
        cur_path.extend(i for i in tup_path)
        cur_path.append(0)
        
        if cur_path[-2] > cur_path[1]:
            continue

        cur_distance = 0
        for a, b, in zip(cur_path[:-1], cur_path[1:]):
            cur_distance += distances[a][b]
        
        if cur_distance < min_dist:
            min_path = cur_path
            min_dist = cur_distance
            
            locations = [coordinates[i] for i in cur_path]
        
            if DISPLAY:
                plt.clf()
                plt.title(cur_distance)    
                for (x1, y1), (x2, y2) in zip(locations[:-1], locations[1:]):
                    plt.plot([x1,x2], [y1,y2], 'ro-')
                
                plt.pause(0.1)
            
    print(min_path)
    print(min_dist)
    
    
