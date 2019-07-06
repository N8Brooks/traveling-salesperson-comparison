import itertools
import math
import matplotlib.pyplot as plt
from locations import locations

DISPLAY = True

if __name__ == '__main__':
    atlas = locations(11, seed=1337)
    
    loc_numbers = [i for i in range(1, atlas.loc_count)]
    perm = itertools.permutations(loc_numbers, atlas.save_one)
    
    min_path = []
    min_dist = math.inf
    for tup_path in perm:
        # pad start and end at 0
        cur_path = [0]
        cur_path.extend(i for i in tup_path)
        cur_path.append(0)
        
        if cur_path[-2] > cur_path[1]:
            continue

        cur_distance = atlas.calculate_distance_padded(cur_path)
        
        if cur_distance < min_dist:
            min_path = cur_path
            min_dist = cur_distance
            
            locations = [atlas.coordinates[i] for i in cur_path]
        
            if DISPLAY:
                plt.clf()
                plt.title(cur_distance)    
                for (x1, y1), (x2, y2) in zip(locations[:-1], locations[1:]):
                    plt.plot([x1,x2], [y1,y2], 'ro-')
                
                plt.pause(0.1)
            
    print(min_path)
    print(min_dist)
    
    
