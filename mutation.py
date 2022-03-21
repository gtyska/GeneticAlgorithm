import numpy as np
import random


class Mutation:
    def __init__(self, placement_array, machines_amount, probability):
        self.placement_array = placement_array
        self.machines_amount = machines_amount
        self.probability = probability
        self.x, self.y = np.shape(self.placement_array)

    def __get_next(self, x, y):
        max_x_idx = self.x - 1
        max_y_idx = self.y - 1
        if x == max_x_idx and y == max_y_idx:
            if max_y_idx == 0:
                return max_x_idx - 1, max_y_idx
            else:
                return max_x_idx, max_y_idx - 1
        if x % 2 == 0:
            if y == self.y - 1:
                x += 1
            else:
                y += 1
        else:
            if y == 0:
                x += 1
            else:
                y -= 1
        return x, y

    def mutate(self):
        counter = 0
        for i in range(self.x):
            for j in range(self.y):
                prob = random.random()
                if prob <= self.probability:
                    counter += 1
                    temp = self.placement_array[i, j]
                    x, y = self.__get_next(i, j)
                    self.placement_array[i, j] = self.placement_array[x, y]
                    self.placement_array[x, y] = temp
        return counter
