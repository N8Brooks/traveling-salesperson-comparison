"""
Author: Tylor Herndon
Date Created: 07/05/2019

This is a neural net implementation of the traveling salesman problem that will be compared to other solutions
in order to display the effiecnency of these implementations.

            ∩

　　　　　　　＼＼

　　　　　　　／　 ）

⊂＼＿／￣￣￣　 ／

　＼＿／   ° ͜ʖ ° （

　　　）　　 　／⌒＼

　　／　 ＿＿＿／⌒＼⊃

　（　 ／

　　＼＼

       U




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
        print("x: {}\ny: {}\n".format(self.location_x, self.location_y))

class grid:

    nodes=[]
    num_nodes=np.matrix(np.zeros(15))

    def __init__(self):
        node_cnt=15
        for n in range(node_cnt):
            temp_node = node()
            self.nodes.append(temp_node)





####################################################################################################
#                               Learning and testing follow this                                   #
####################################################################################################


temp_grid = grid()
for n in range(len(temp_grid.nodes)) :
    print("Node[{}]".format(n+1)) 
    temp_grid.nodes[n].print_location()

