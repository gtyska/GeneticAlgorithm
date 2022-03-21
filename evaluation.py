import numpy as np


class Evaluation:
    def __init__(self, placement_array, amount, flow_cost_array):
        self.placement_array = placement_array
        self.amount = amount
        self.flow_cost_array = flow_cost_array

    def __refactor_placement_array(self):
        placement_light_array = np.zeros(shape=(2, self.amount), dtype=int)
        for i in range(1, self.amount + 1):
            coord = np.where(self.placement_array == i)
            placement_light_array[0, i - 1] = coord[0]
            placement_light_array[1, i - 1] = coord[1]
        return placement_light_array

    def count_cost(self):
        amount = self.amount
        placement_light_array = self.__refactor_placement_array()
        distance_array = np.zeros(shape=np.shape(self.flow_cost_array), dtype=int)
        for i in range(0, amount):
            for j in range(0, amount):
                distance = abs(placement_light_array[0, i] - placement_light_array[0, j]) + \
                           abs(placement_light_array[1, i] - placement_light_array[1, j])
                distance_array[i, j] = distance
        return (self.flow_cost_array * distance_array).sum()
