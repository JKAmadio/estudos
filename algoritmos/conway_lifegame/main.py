import numpy as np
import conway_game_of_life

matrix = np.random.randint(0, 2, size=(8, 8))
count_generations = 0
for i in range(20):
    conway_game_of_life.print_grid(matrix, count_generations)
    matrix = conway_game_of_life.update_grid(matrix)
    count_generations += 1
conway_game_of_life.record_grid_changes()
