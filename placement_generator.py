import numpy as np
import random


class Placement:
    def __init__(self, amount, x, y):
        self.amount = amount
        self.x = x
        self.y = y

    def generate_random_placement(self):
        amount = self.amount
        x = self.x
        y = self.y
        placement_array = np.full((x, y), None)
        idx_array = np.arange(0, x * y, 1, dtype=int)
        while amount > 0:
            idx = random.randint(0, len(idx_array) - 1)
            combined_placement = idx_array[idx]
            x_pos = combined_placement // y
            y_pos = combined_placement % y
            idx_array = np.delete(idx_array, idx)
            placement_array[x_pos, y_pos] = amount
            amount -= 1
        return placement_array
