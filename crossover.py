import numpy as np
import random


class Crossover:
    def __init__(self, placement_array_1, placement_array_2, machines_amount, genes_amount):
        self.placement_array_1 = placement_array_1
        self.placement_array_2 = placement_array_2
        self.machines_amount = machines_amount
        self.genes_amount = genes_amount

    def __random_start_idx(self, x, y):
        idx_array = np.arange(0, x * y, 1, dtype=int)
        idx = random.randint(0, len(idx_array) - 1 - self.genes_amount)
        combined_placement = idx_array[idx]
        x_pos = combined_placement // y
        y_pos = combined_placement % y
        return x_pos, y_pos

    def __next_elements_idx(self, x_pos, y_pos, y):
        next_pos_array = [(x_pos, y_pos)]
        for i in range(self.genes_amount - 1):
            y_pos += 1
            if y_pos >= y:
                y_pos = y_pos % y
                x_pos += 1
            next_pos_array.append((x_pos, y_pos))
        return next_pos_array

    @staticmethod
    def __repair_array(placement_array, replace_from, replace_to, x_pos, y_pos):
        if not replace_from == replace_to:
            founded_array = np.where(placement_array == replace_from)
            rows_array = founded_array[0]
            cols_array = founded_array[1]
            number_founded = len(rows_array)
            for i in range(number_founded):
                if not (rows_array[i] == x_pos and cols_array[i] == y_pos):
                    if replace_to is None or not replace_to in placement_array:
                        placement_array[rows_array[i], cols_array[i]] = replace_to
                        return placement_array
        return placement_array

    def crossover(self):
        placement_array_1_new = np.copy(self.placement_array_1)
        placement_array_2_new = np.copy(self.placement_array_2)

        x, y = np.shape(self.placement_array_1)
        x_pos, y_pos = self.__random_start_idx(x, y)

        swap_pos_array = self.__next_elements_idx(x_pos, y_pos, y)

        for i in range(self.genes_amount):
            x_pos, y_pos = swap_pos_array[i]
            temp = placement_array_1_new[x_pos, y_pos]
            temp2 = placement_array_2_new[x_pos, y_pos]
            placement_array_1_new[x_pos, y_pos] = temp2
            placement_array_2_new[x_pos, y_pos] = temp

            placement_array_1_new = self.__repair_array(placement_array=placement_array_1_new,
                                                        replace_from=temp2, replace_to=temp, x_pos=x_pos, y_pos=y_pos)
            placement_array_2_new = self.__repair_array(placement_array=placement_array_2_new,
                                                        replace_from=temp, replace_to=temp2, x_pos=x_pos, y_pos=y_pos)

        return placement_array_1_new, placement_array_2_new
