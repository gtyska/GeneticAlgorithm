import numpy as np
from evaluation import Evaluation
import random


class Selection:
    def __init__(self, population_array, number, machines_amount, flow_cost_array):
        self.population_list = population_array
        self.number = number
        self.individuals_number = len(self.population_list)
        self.machines_amount = machines_amount
        self.flow_cost_array = flow_cost_array
        self.fitness_list = self.__count_costs()

    def __count_costs(self):
        fitness_list = []
        for individual in self.population_list:
            evaluation = Evaluation(individual, self.machines_amount, self.flow_cost_array)
            fitness_list.append(evaluation.count_cost())
        return fitness_list

    def roulette(self):
        population_idx_array = np.arange(0, len(self.population_list), 1, dtype=int)
        min_fitness = min(self.fitness_list)
        tmp_fitness_list = [elem - min_fitness/1.1 for elem in self.fitness_list]
        sum = np.sum(tmp_fitness_list)
        selection_probs_array = [sum / cost for cost in tmp_fitness_list]
        sum = np.sum(selection_probs_array)
        selection_probs_array = [elem / sum for elem in selection_probs_array]
        chosen_idx_array = np.random.choice(population_idx_array, self.individuals_number, p=selection_probs_array)
        new_population_list = []
        for idx in chosen_idx_array:
            new_population_list.append(self.population_list[idx])
        return new_population_list

    @staticmethod
    def __find_min_idx(array):
        min_elem = array[0]
        best_idx = 0
        for i in range(len(array)):
            if min_elem > array[i]:
                min_elem = array[i]
                best_idx = i
        return best_idx

    def __tournament_iteration(self):
        population_idx_array = np.arange(0, len(self.population_list), 1, dtype=int)
        chosen_idx_array = []
        chosen_cost_array = []  # specifies the cost of refering machines
        for i in range(self.number):
            idx = random.randint(0, len(population_idx_array) - 1)
            machine_idx = population_idx_array[idx]
            chosen_idx_array.append(machine_idx)
            chosen_cost_array.append(self.fitness_list[machine_idx])
            population_idx_array = np.delete(population_idx_array, idx)
        best_idx = self.__find_min_idx(chosen_cost_array)
        best_machine_idx = chosen_idx_array[best_idx]
        return self.population_list[best_machine_idx], best_machine_idx

    def tournament(self):
        new_population_list = []
        chosen_idx_list = []
        for i in range(self.individuals_number):
            best_individual, best_idx = self.__tournament_iteration()
            new_population_list.append(best_individual)
            chosen_idx_list.append(best_idx)
        return new_population_list
