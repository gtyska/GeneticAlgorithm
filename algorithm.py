from crossover import Crossover
from flow_cost import FlowCost
from placement_generator import Placement
from selection_operators import Selection
from mutation import Mutation
from evaluation import Evaluation


class Algorithm:
    def __init__(self, flow_f_name, cost_f_name, machines_amount, x_dim, y_dim,
                 tournament_number, is_roulette, mutation_probability, genes_amount,
                 individuals_amount, generations_amount):
        flow_cost = FlowCost(flow_f_name=flow_f_name, cost_f_name=cost_f_name, amount=machines_amount)
        self.flow_cost_array = flow_cost.get_flow_cost_array()
        self.machines_amount = machines_amount
        self.x_dim = x_dim
        self.y_dim = y_dim

        # for selection
        self.tournament_number = tournament_number
        self.is_roulette = is_roulette

        # for mutation
        self.mutation_prob = mutation_probability
        self.genes_amount = genes_amount

        # for algorithm
        self.individuals_amount = individuals_amount
        self.generations_amount = generations_amount
        self.population = self.__generate_first_generation()

    def __generate_first_generation(self):
        population = []
        placement_generator = Placement(amount=self.machines_amount, x=self.x_dim, y=self.y_dim)
        for i in range(self.individuals_amount):
            population.append(
                placement_generator.generate_random_placement())
        return population

    def selection(self):
        selection = Selection(population_array=self.population, number=self.tournament_number,
                              machines_amount=self.machines_amount, flow_cost_array=self.flow_cost_array)
        if self.is_roulette:
            self.population = selection.roulette()
        else:
            self.population = selection.tournament()

    def crossover(self):
        idx = 0
        for i in range(self.individuals_amount // 2):
            parent_1 = self.population[idx]
            idx += 1
            parent_2 = self.population[idx]
            crossover = Crossover(placement_array_1=parent_1, placement_array_2=parent_2, machines_amount=self.machines_amount, genes_amount=self.genes_amount)
            child_1, child_2 = crossover.crossover()
            self.population[idx - 1] = child_1
            self.population[idx] = child_2
            idx += 1

    def mutation(self):
        for i in range(self.individuals_amount):
            individual = self.population[i]
            mutation = Mutation(placement_array=individual, machines_amount=self.machines_amount, probability=self.mutation_prob)
            mutation.mutate()

    def __find_min_max_avg(self):
        fitness_list = []
        for individual in self.population:
            evaluation = Evaluation(individual, self.machines_amount, self.flow_cost_array)
            fitness_list.append(evaluation.count_cost())
        min_value = min(fitness_list)
        max_value = max(fitness_list)
        avg_value = sum(fitness_list) / len(fitness_list)
        return min_value, max_value, avg_value

    def run(self):
        min_arr = []
        max_arr = []
        avg_arr = []
        for i in range(self.generations_amount):
            self.selection()
            self.crossover()
            self.mutation()
            min_val, max_val, avg_val = self.__find_min_max_avg()
            min_arr.append(min_val)
            max_arr.append(max_val)
            avg_arr.append(avg_val)
        return min_arr, max_arr, avg_arr
