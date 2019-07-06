"""
Author: Tylor Herndon
Date Created: 07/05/2019

This is a neural net implementation of the traveling salesman problem that will be compared to other solutions
in order to display the effiecnency of these implementations.
"""
import random
import numpy as np

class node:

    location_x = 0
    location_y = 0

    def __init__(self):
        self.location_x = random.randint(0,100)
        self.location_y = random.randint(0,100)

    def print_location(self):
        print("x: {} \ny: {}".format(self.location_x, self.location_y))

temp = node()
temp.print_location()

class grid:

    nodes=[]
    num_nodes=np.matrix(np.zeros(15))

    def __init__(self):
        node_cnt=0
        for(n in num_nodes):
            temp_node = node()
            n.append(temp_node)
        

