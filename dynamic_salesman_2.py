

import math
from locations import locations

atlas = locations(11, seed=1337)
mem = [[None]*(1<<atlas.loc_count)]*atlas.loc_count
paths = [[[]]*(1<<atlas.loc_count)]*atlas.loc_count


def tsp(i, S):
    if S == ((1 << atlas.loc_count) - 1):
        return atlas.distances[i][0]

    if mem[i][S] != None:
        return mem[i][S]

    res = math.inf
    for j in range(atlas.loc_count):
        if S & (1 << j):
            continue
        
        res = min(res, atlas.distances[i][j] + tsp(j, S | (1 << j)))

    mem[i][S] = res
    return res


if __name__ == '__main__':
    print(tsp(0, 1<<0))