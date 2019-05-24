#https://github.com/McKay1717/Ants-Algo
import random as rn
import numpy as np
from numpy.random import choice as np_choice

class AntAlgo(object):

    def __init__(self, dist, num_ants, num_best, iterations, decay, alpha=1, beta=1):
	self.all_inds = range(len(dist))
	self.dist = dist
        self.pheromone = np.ones(self.dist.shape) / len(dist)
        self.iterations = iterations
        self.decay = decay
        self.alpha = alpha
	self.num_best = num_best
	self.beta = beta
	self.num_ants = num_ants

    def run(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)#Internet
        for i in range(self.iterations):
            all_paths = self.gen_all_paths()
	    print(all_paths)
            self.add_pheronome(all_paths, self.num_best, shortest_path=shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path            
            self.pheromone * self.decay            
        return all_time_shortest_path

    def add_pheronome(self, all_paths, num_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:num_best]:
            for move in path:
                self.pheromone[move] += 1.0 / self.dist[move]

    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.dist[ele]
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for i in range(self.num_ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.dist) - 1):
            move = self.do_move(self.pheromone[prev], self.dist[prev], visited)
            path.append((prev, move))
            prev = move
            visited.add(move)
        path.append((prev, start)) # going back to where we started    
        return path

    def do_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0

        row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)

        norm_row = row / row.sum()
        move = np_choice(self.all_inds, 1, p=norm_row)[0]
        return move


