import math
from locations import locations

atlas = locations(11, seed=52)
mem = [[None]*(1<<atlas.loc_count)]*atlas.loc_count
paths = [[[]]*(1<<atlas.loc_count)]*atlas.loc_count

"""
this is not working.

it does not return optimal path as verified from complete_salesman.py
"""
calls = 0

def tsp(i, S, path):
    global calls
    calls += 1
    if S > ((1 << atlas.loc_count) - 1):
        exit()
    if (calls < 13):
        #pass
        print ("{}\t{}\t{}".format(i,bin(S),path))
    if S == ((1 << atlas.loc_count) - 1):
        return atlas.distances[i][0], path + [0]
    if mem[i][S] != None:
        return mem[i][S], paths[i][S]
    
    res = math.inf
    best = [-1]
    for j in range(atlas.loc_count):
        if S & (1 << j):
            continue
        
        tmp_res, tmp_path = tsp(j, S | (1 << j), paths[j][S | (1 << j)])
        if res < atlas.distances[i][j] + tmp_res:
            pass
        else:
            res = atlas.distances[i][j] + tmp_res
            best = paths[j][S | (1 << j)] + [i]
            
    mem[i][S] = res
    paths[i][S] = best
    return res, best

if __name__ == '__main__':
    tmp_res, tmp_path = tsp(0, 1<<0, [0])
    print(tmp_path)
    atlas.display_path(tmp_path)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    