# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:42:04 2019

@author: DSU
* immutable stuff
* static stuff
* accumulate functions
"""

import random
import math
import itertools
import matplotlib.pyplot as plt

# change for different functionality
LOC_COUNT = 8
PATH_COUNT = 100
LEFT_COUNT = int(0.2 * PATH_COUNT)  # approxamite pareto distribution
PLANE_LENGTH = 1000
DISPLAY = 'best'                    # can be: all, best, dist

# helper global variables
save_one = LOC_COUNT - 1
random.seed(1)
coordinates = [(random.randrange(PLANE_LENGTH), random.randrange(PLANE_LENGTH)\
                ) for i in range(LOC_COUNT)]
distances = []
for (x_a, y_a) in coordinates:
    distances.append([math.hypot(x_b - x_a, y_b - y_a) for (x_b, y_b) in\
                      coordinates])

class path:
    global distances
    def __init__(self, *args):
        # radomize, set, or breed path
        if len(args) == 0:
            self.path = random.sample(range(1, LOC_COUNT), save_one)
        elif len(args) == 1:
            assert type(args[0]) == type([])
            self.path = args[0]
        elif len(args) == 2:
            # input data validation
            assert type(args[0]) == type(path())
            assert type(args[1]) == type(path())
            par_a = args[0].path
            par_b = args[1].path
            
            self.path = []
            last = 0
            legitamate = [i for i in range(1, LOC_COUNT)]
            for node in range(save_one):
                # find first legitamate in a_par
                a_legit = None
                for a in par_a[node:]:
                    if a in legitamate:
                        a_legit = a
                        break
                if a_legit == None:
                    a_legit = legitamate[0]
                
                # find first legitamate in b_par
                b_legit = None
                for b in par_b[node:]:
                    if b in legitamate:
                        b_legit = b
                        break
                if b_legit == None:
                    b_legit = legitamate[0]
                # use that node
                if distances[last][a_legit] <= distances[last][b_legit]:
                    legitamate.remove(a_legit)
                    last = a_legit
                    self.path.append(a_legit)
                else:
                    legitamate.remove(b_legit)
                    last = b_legit
                    self.path.append(b_legit)
        else:
            print('Too many args.')
            assert False
            
            # mutate
            one, two = random.sample(range(0, save_one), 2)
            self.path[one], self.path[two] = self.path[two], self.path[one]
        
        # make sure it is 'clockwise'
        self.order()    
        
        # set distance
        self.distance = distances[0][self.path[0]]
        for i, j in zip(self.path[:-1], self.path[1:]):
            self.distance += distances[i][j]
        self.distance += distances[self.path[-1]][0]
            
    def __hash__(self):
        # this isn't used anymore
        coefficients = []
        path_copy = self.path.copy()
        for i in range(1, LOC_COUNT):
            c = path_copy.index(i)
            coefficients.append(c)
            path_copy.pop(c)
            
        return sum(math.factorial(i) * x for i, x in enumerate(reversed(\
                   coefficients)))
    
    def order(self):
        # since distances are symmetric, reversed paths equal each other
        if self.path[0] > self.path[-1]:
            self.path.reverse()
    
    def display(self, text):
        locations = [coordinates[0]]
        locations.extend([coordinates[i] for i in self.path])
        locations.append(coordinates[0])
        
        plt.clf()
        plt.title(text)    
        for (x1, y1), (x2, y2) in zip(locations[:-1], locations[1:]):
            plt.plot([x1,x2], [y1,y2], 'ro-')
        
        plt.pause(0.1)

if __name__ == '__main__':
    # random gen 0 - display one of them
    population = [path() for i in range(PATH_COUNT)]
    best_path = math.inf
    
    # run until ctr + c
    for i in itertools.count():
        # sort
        population.sort(key=lambda x: x.distance)
        
        # check the best
        if population[0].distance < best_path:
            best_path = population[0].distance
            if DISPLAY == 'best':
                population[0].display('Gen {}: {}'.format(i,\
                                  population[0].distance))
                print(population[0].distance)
            elif DISPLAY == 'dist':
                print(population[0].distance)
        
        if DISPLAY == 'all':
            population[0].display('Gen {}: {}'.format(i,\
                                  population[0].distance))
        
        # keep the top percent
        parents = population[:LEFT_COUNT]
    
        # breed
        parents_a = [parents[a] for a in random.choices(range(0,LEFT_COUNT),\
                     k=PATH_COUNT)]
        parents_b = [parents[b] for b in random.choices(range(0,LEFT_COUNT),\
                     k=PATH_COUNT)]
        population = [path(a, b) for a, b in zip(parents_a, parents_b)]
    
    
    
    
    
    
    
    