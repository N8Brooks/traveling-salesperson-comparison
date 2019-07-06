import random
import math

class locations:
    loc_count = None
    save_one = None
    PLANE_LENGTH = 1000
    
    def __init__(self, count, **kwargs):
        assert type(count) == type(0)
        self.loc_count = count
        
        # create random places
        if len(kwargs) == 0:
            self.generate_random()
            
        # generate from seed
        if 'seed' in kwargs.keys() and type(kwargs['seed']) == type(0):
            random.seed(kwargs['seed'])
            self.generate_random()
        
        # load from saved file???
    
    def generate_random(self):
        self.save_one = self.loc_count - 1
        self.coordinates = [(random.randrange(self.PLANE_LENGTH), random.randrange(self.PLANE_LENGTH)) for i in range(self.loc_count)]
        self.distances = []
        for (x_a, y_a) in self.coordinates:
            self.distances.append([math.hypot(x_b - x_a, y_b - y_a) for (x_b, y_b) in self.coordinates])

    def calculate_distance_plain(self, cur_path):
        assert len(cur_path) == self.save_one
        
        cur_distance = self.distances[0][cur_path[0]]
        cur_distance = self.distances[-1][cur_path[-1]]
        for a, b, in zip(cur_path[:-1], cur_path[1:]):
            cur_distance += self.distances[a][b]
        
        return cur_distance
    
    def calculate_distance_padded(self, cur_path):
        assert len(cur_path) == self.loc_count + 1
        
        cur_distance = 0
        for a, b, in zip(cur_path[:-1], cur_path[1:]):
            cur_distance += self.distances[a][b]
        
        return cur_distance

    def get_distance(self, loc_a, loc_b):
        return self.distances[loc_a][loc_b]