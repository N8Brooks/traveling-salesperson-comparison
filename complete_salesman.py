import itertools
import math
from locations import locations

# can be 'improved', 'best', 'none'
DISPLAY = 'best'

if __name__ == '__main__':
    atlas = locations(12, seed=1337)
    
    loc_numbers = [i for i in range(1, atlas.loc_count)]
    perm = itertools.permutations(loc_numbers, atlas.save_one)
    
    min_path = []
    min_dist = math.inf
    min_iteration = -1
    for i, tup_path in enumerate(perm):
        # pad start and end at 0
        cur_path = [0]
        cur_path.extend(i for i in tup_path)
        cur_path.append(0)
        
        if cur_path[-2] > cur_path[1]:
            continue

        cur_dist = atlas.calculate_distance_plain(cur_path)
        
        if cur_dist < min_dist:
            min_iteration = i
            min_path = cur_path
            min_dist = cur_dist
        
            if DISPLAY == 'improved':
                atlas.display_path(cur_path, i)
    
    if DISPLAY == 'best':
        atlas.display_path(min_path, min_iteration)
    
    
