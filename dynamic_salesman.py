import math
from locations import locations

atlas = locations(12, seed=1337)
mem = [[None]*(1<<atlas.loc_count)]*atlas.loc_count
paths = [[[]]*(1<<atlas.loc_count)]*atlas.loc_count

"""
this is not working.

it does not return optimal path as verified from complete_salesman.py
"""

def tsp(i, S, path):
    if S == ((1 << atlas.loc_count) - 1):
        return atlas.distances[i][0], paths[i][0]
    if mem[i][S] != None:
        return mem[i][S], paths[i][S]
    
    res = math.inf
    for j in range(atlas.loc_count):
        if S & (1 << j):
            continue
        
        tmp_res, tmp_path = tsp(j, S | (1 << j), path+[j])
        if res < atlas.distances[i][j] + tmp_res:
            pass
        else:
            res = atlas.distances[i][j] + tmp_res
            path = tmp_path + [j]
    
    mem[i][S] = res
    paths[i][S] = path
    return res, path

if __name__ == '__main__':
    tmp_res, tmp_path = tsp(0, 1<<0, [])
    tmp_path.insert(0,0)
    tmp_path.append(0)
    atlas.display_path(tmp_path)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    