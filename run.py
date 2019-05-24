import numpy as np

from ant_algo import AntAlgo

distances = np.array([[np.inf, 100, 60, 50, 55],
                      [150, np.inf, 65, 140, 70],
                      [40, 90, np.inf, 90, 40],
                      [70, 140, 65, np.inf, 150],
                      [55, 50, 60, 100, np.inf]])

ant_colony = AntAlgo(distances, 5, 1, 1000, 0.6, alpha=0.2, beta=0.6)
shortest_path = ant_colony.run()
print ("shorted_path: {}".format(shortest_path))

