from locations import locations
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

if __name__ == '__main__':
    atlas = locations(32, seed=1337)
    
    df = pd.DataFrame(atlas.distances)
    np.fill_diagonal(df.values, math.inf)
    
    cur_loc = 0
    tmp_loc = None
    cur_path = []
    for i in range(atlas.loc_count):
        cur_path.append(cur_loc)
        tmp_loc = df[cur_loc].idxmin()
        df = df.drop(cur_loc, axis=1)
        df = df.drop(cur_loc)
        cur_loc = tmp_loc
    cur_path.append(0)
    
    text = 'Nearest: {}'.format(atlas.calculate_distance(cur_path))
    atlas.display_path(cur_path, text)
    plt.waitforbuttonpress()