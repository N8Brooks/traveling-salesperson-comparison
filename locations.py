import random
import math
import matplotlib.pyplot as plt

class path:
    pass

class locations:
    plane_length = 1000
    loc_count = None
    save_one = None
    distances = None
    coordinates = None
    
    def __init__(self, arg, **kwargs):
        # change plane length if desired
        try:
            self.plane_length = kwargs['plane']
        except:
            pass
        
        # load from saved file
        if type(arg) == type(' '):
            print('Not implemented.')
            exit()
        
        # get amount of locations
        assert type(arg) == type(0)
        self.loc_count = arg
        
        # create random places: atlas = locations(12)
        if len(kwargs) == 0:
            self.generate_random()
            
        # generate from seed: atlas = locations(12, seed=1337)
        if 'seed' in kwargs.keys() and type(kwargs['seed']) == type(0):
            random.seed(kwargs['seed'])
            self.generate_random()
    
    def generate_random(self):
        self.save_one = self.loc_count - 1
        self.coordinates = [(random.randrange(self.plane_length),\
                             random.randrange(self.plane_length)) for i in\
                             range(self.loc_count)]
        self.distances = []
        for (x_a, y_a) in self.coordinates:
            self.distances.append([math.hypot(x_b - x_a, y_b - y_a) for (x_b,\
                                   y_b) in self.coordinates])

    def calculate_distance(self, cur_path):
        # pad if not padded
        cur_path = self.pad_path(cur_path)
        
        # add up vectors
        cur_distance = 0
        for a, b, in zip(cur_path[:-1], cur_path[1:]):
            cur_distance += self.distances[a][b]
        
        return cur_distance

    def pad_path(self, cur_path):
        if cur_path[0] != 0:
            cur_path.insert(0, 0)
        if cur_path[-1] != 0:
            cur_path.append(0)
        
        # input validation
        assert len(cur_path) == self.loc_count + 1
        
        return cur_path

    def get_distance(self, loc_a, loc_b):
        return self.distances[loc_a][loc_b]
    
    def display_path(self, cur_path, *args):
        # pad path if not padded
        cur_path = self.pad_path(cur_path)
        
        # get distances:
        cur_dist = self.calculate_distance(cur_path)
        
        # get coordinates of locations
        loc_coords = [self.coordinates[i] for i in cur_path]
        
        # generate text
        if len(args) > 0:
            text = '{}. - {} - {}'.format(int(args[0]), cur_dist, cur_path)
        else:
            text = '{} - {}'.format(cur_dist, cur_path)
        
        # display with matplotlib
        plt.clf()
        plt.title(text)
        for (x1, y1), (x2, y2) in zip(loc_coords[:-1], loc_coords[1:]):
            plt.plot([x1,x2], [y1,y2], 'ro-')
        plt.pause(0.1)
    
    