from algorithm import Algorithm
import matplotlib.pyplot as plt
import statistics
from random_method import RandomMethod


def easy_random():
    print()
    print('\033[92m' + 'Easy [random]' + '\033[0m')
    flow_f_name = 'easy_flow.json'
    cost_f_name = 'easy_cost.json'
    machines_amount = 9
    x_dim = 3
    y_dim = 3
    n = 5000
    random = RandomMethod(flow_f_name=flow_f_name, cost_f_name=cost_f_name,
                          machines_amount=machines_amount, x_dim=x_dim, y_dim=y_dim, n=n)
    min_val, max_val, avg_val, std = random.run()
    print('Min:', min_val)
    print('Max:', max_val)
    print('Avg:', avg_val)
    print('Std:', std)


def easy_tournament_10():
    print()
    print('\033[92m' + 'Easy x10 [tournament]' + '\033[0m')
    flow_f_name = 'easy_flow.json'
    cost_f_name = 'easy_cost.json'
    machines_amount = 9
    x_dim = 3
    y_dim = 3
    tournament_number = 10
    is_roulette = False
    mutation_probability = 0.04
    genes_amount = 3
    individuals_amount = 100
    generations_amount = 50
    results = []
    for i in range(10):
        algorithm = Algorithm(flow_f_name=flow_f_name, cost_f_name=cost_f_name, machines_amount=machines_amount,
                              x_dim=x_dim, y_dim=y_dim, tournament_number=tournament_number, is_roulette=is_roulette,
                              mutation_probability=mutation_probability, genes_amount=genes_amount,
                              individuals_amount=individuals_amount, generations_amount=generations_amount)
        min_arr, max_arr, avg_arr = algorithm.run()
        best_result = min(min_arr)
        results.append(best_result)
    min_val = min(results)
    max_val = max(results)
    avg_val = sum(results) / len(results)
    std = statistics.stdev(results)
    print('Min:', min_val)
    print('Max:', max_val)
    print('Avg:', avg_val)
    print('Std:', std)


def easy_tournament():
    print()
    print('\033[92m' + 'Easy [tournament]' + '\033[0m')
    flow_f_name = 'easy_flow.json'
    cost_f_name = 'easy_cost.json'
    machines_amount = 9
    x_dim = 3
    y_dim = 3
    tournament_number = 10
    is_roulette = False
    mutation_probability = 0.04
    genes_amount = 3
    individuals_amount = 200
    generations_amount = 50

    algorithm = Algorithm(flow_f_name=flow_f_name, cost_f_name=cost_f_name, machines_amount=machines_amount,
                          x_dim=x_dim, y_dim=y_dim, tournament_number=tournament_number, is_roulette=is_roulette,
                          mutation_probability=mutation_probability, genes_amount=genes_amount,
                          individuals_amount=individuals_amount, generations_amount=generations_amount)

    min_arr, max_arr, avg_arr = algorithm.run()

    for i in range(len(min_arr)):
        print('Min:', min_arr[i])
        print('Max:', max_arr[i])
        print('Avg:', avg_arr[i])
        print('-------------------')
    print('Minimum of all:', min(min_arr))
    draw_plot(min_arr, max_arr, avg_arr)


def easy_roulette():
    print()
    print('\033[92m' + 'Easy [roulette]' + '\033[0m')
    flow_f_name = 'easy_flow.json'
    cost_f_name = 'easy_cost.json'
    machines_amount = 9
    x_dim = 3
    y_dim = 3
    tournament_number = 10
    is_roulette = True
    mutation_probability = 0.04
    genes_amount = 3
    individuals_amount = 100
    generations_amount = 100

    algorithm = Algorithm(flow_f_name=flow_f_name, cost_f_name=cost_f_name, machines_amount=machines_amount,
                          x_dim=x_dim, y_dim=y_dim, tournament_number=tournament_number, is_roulette=is_roulette,
                          mutation_probability=mutation_probability, genes_amount=genes_amount,
                          individuals_amount=individuals_amount, generations_amount=generations_amount)

    min_arr, max_arr, avg_arr = algorithm.run()

    for i in range(len(min_arr)):
        print('Min:', min_arr[i])
        print('Max:', max_arr[i])
        print('Avg:', avg_arr[i])
        print('-------------------')
    print('Minimum of all:', min(min_arr))
    draw_plot(min_arr, max_arr, avg_arr)


def flat_random():
    print()
    print('\033[92m' + 'Flat [random]' + '\033[0m')
    flow_f_name = 'flat_flow.json'
    cost_f_name = 'flat_cost.json'
    machines_amount = 12
    x_dim = 1
    y_dim = 12
    n = 10000
    random = RandomMethod(flow_f_name=flow_f_name, cost_f_name=cost_f_name,
                          machines_amount=machines_amount, x_dim=x_dim, y_dim=y_dim, n=n)
    min_val, max_val, avg_val, std = random.run()
    print('Min:', min_val)
    print('Max:', max_val)
    print('Avg:', avg_val)
    print('Std:', std)


def flat_tournament_10():
    print()
    print('\033[92m' + 'Flat x10 [tournament]' + '\033[0m')
    flow_f_name = 'flat_flow.json'
    cost_f_name = 'flat_cost.json'
    machines_amount = 12
    x_dim = 1
    y_dim = 12
    tournament_number = 5
    is_roulette = False
    mutation_probability = 0.03
    genes_amount = 3
    individuals_amount = 100
    generations_amount = 100
    results = []
    for i in range(10):
        algorithm = Algorithm(flow_f_name=flow_f_name, cost_f_name=cost_f_name, machines_amount=machines_amount,
                              x_dim=x_dim, y_dim=y_dim, tournament_number=tournament_number, is_roulette=is_roulette,
                              mutation_probability=mutation_probability, genes_amount=genes_amount,
                              individuals_amount=individuals_amount, generations_amount=generations_amount)
        min_arr, max_arr, avg_arr = algorithm.run()
        best_result = min(min_arr)
        results.append(best_result)
    min_val = min(results)
    max_val = max(results)
    avg_val = sum(results) / len(results)
    std = statistics.stdev(results)
    print('Min:', min_val)
    print('Max:', max_val)
    print('Avg:', avg_val)
    print('Std:', std)


def flat_tournament():
    print()
    print('\033[92m' + 'Flat [tournament]' + '\033[0m')
    flow_f_name = 'flat_flow.json'
    cost_f_name = 'flat_cost.json'
    machines_amount = 12
    x_dim = 1
    y_dim = 12
    tournament_number = 10
    is_roulette = False
    mutation_probability = 0.04
    genes_amount = 3
    individuals_amount = 50
    generations_amount = 100

    algorithm = Algorithm(flow_f_name=flow_f_name, cost_f_name=cost_f_name, machines_amount=machines_amount,
                          x_dim=x_dim, y_dim=y_dim, tournament_number=tournament_number, is_roulette=is_roulette,
                          mutation_probability=mutation_probability, genes_amount=genes_amount,
                          individuals_amount=individuals_amount, generations_amount=generations_amount)

    min_arr, max_arr, avg_arr = algorithm.run()

    for i in range(len(min_arr)):
        print('Min:', min_arr[i])
        print('Max:', max_arr[i])
        print('Avg:', avg_arr[i])
        print('-------------------')
    print('Minimum of all:', min(min_arr))
    draw_plot(min_arr, max_arr, avg_arr)


def flat_roulette():
    print()
    print('\033[92m' + 'Flat [roulette]' + '\033[0m')
    flow_f_name = 'flat_flow.json'
    cost_f_name = 'flat_cost.json'
    machines_amount = 12
    x_dim = 1
    y_dim = 12
    tournament_number = 10
    is_roulette = True
    mutation_probability = 0.04
    genes_amount = 3
    individuals_amount = 100
    generations_amount = 100

    algorithm = Algorithm(flow_f_name=flow_f_name, cost_f_name=cost_f_name, machines_amount=machines_amount,
                          x_dim=x_dim, y_dim=y_dim, tournament_number=tournament_number, is_roulette=is_roulette,
                          mutation_probability=mutation_probability, genes_amount=genes_amount,
                          individuals_amount=individuals_amount, generations_amount=generations_amount)

    min_arr, max_arr, avg_arr = algorithm.run()

    for i in range(len(min_arr)):
        print('Min:', min_arr[i])
        print('Max:', max_arr[i])
        print('Avg:', avg_arr[i])
        print('-------------------')
    print('Minimum of all:', min(min_arr))
    draw_plot(min_arr, max_arr, avg_arr)


def hard_random():
    print()
    print('\033[92m' + 'Hard [random]' + '\033[0m')
    flow_f_name = 'hard_flow.json'
    cost_f_name = 'hard_cost.json'
    machines_amount = 24
    x_dim = 5
    y_dim = 6
    n = 5000
    random = RandomMethod(flow_f_name=flow_f_name, cost_f_name=cost_f_name,
                          machines_amount=machines_amount, x_dim=x_dim, y_dim=y_dim, n=n)
    min_val, max_val, avg_val, std = random.run()
    print('Min:', min_val)
    print('Max:', max_val)
    print('Avg:', avg_val)
    print('Std:', std)


def hard_tournament_10():
    print()
    print('\033[92m' + 'Hard x10 [tournament]' + '\033[0m')
    flow_f_name = 'hard_flow.json'
    cost_f_name = 'hard_cost.json'
    machines_amount = 24
    x_dim = 5
    y_dim = 6
    tournament_number = 5
    is_roulette = False
    mutation_probability = 0.80
    genes_amount = 4
    individuals_amount = 100
    generations_amount = 50
    results = []
    for i in range(10):
        algorithm = Algorithm(flow_f_name=flow_f_name, cost_f_name=cost_f_name, machines_amount=machines_amount,
                              x_dim=x_dim, y_dim=y_dim, tournament_number=tournament_number, is_roulette=is_roulette,
                              mutation_probability=mutation_probability, genes_amount=genes_amount,
                              individuals_amount=individuals_amount, generations_amount=generations_amount)
        min_arr, max_arr, avg_arr = algorithm.run()
        best_result = min(min_arr)
        results.append(best_result)
    min_val = min(results)
    max_val = max(results)
    avg_val = sum(results) / len(results)
    std = statistics.stdev(results)
    print('Min:', min_val)
    print('Max:', max_val)
    print('Avg:', avg_val)
    print('Std:', std)


def hard_tournament():
    print()
    print('\033[92m' + 'Hard [tournament]' + '\033[0m')
    flow_f_name = 'hard_flow.json'
    cost_f_name = 'hard_cost.json'
    machines_amount = 24
    x_dim = 5
    y_dim = 6
    tournament_number = 5
    is_roulette = False
    mutation_probability = 0.80
    genes_amount = 4
    individuals_amount = 100
    generations_amount = 50

    algorithm = Algorithm(flow_f_name=flow_f_name, cost_f_name=cost_f_name, machines_amount=machines_amount,
                          x_dim=x_dim, y_dim=y_dim, tournament_number=tournament_number, is_roulette=is_roulette,
                          mutation_probability=mutation_probability, genes_amount=genes_amount,
                          individuals_amount=individuals_amount, generations_amount=generations_amount)

    min_arr, max_arr, avg_arr = algorithm.run()

    for i in range(len(min_arr)):
        print('Min:', min_arr[i])
        print('Max:', max_arr[i])
        print('Avg:', avg_arr[i])
        print('-------------------')
    print('Minimum of all:', min(min_arr))
    draw_plot(min_arr, max_arr, avg_arr)


def hard_roulette_10():
    print()
    print('\033[92m' + 'Hard x10 [roulette]' + '\033[0m')
    flow_f_name = 'hard_flow.json'
    cost_f_name = 'hard_cost.json'
    machines_amount = 24
    x_dim = 5
    y_dim = 6
    tournament_number = 5
    is_roulette = True
    mutation_probability = 0.2
    genes_amount = 4
    individuals_amount = 100
    generations_amount = 50
    results = []
    for i in range(10):
        algorithm = Algorithm(flow_f_name=flow_f_name, cost_f_name=cost_f_name, machines_amount=machines_amount,
                              x_dim=x_dim, y_dim=y_dim, tournament_number=tournament_number, is_roulette=is_roulette,
                              mutation_probability=mutation_probability, genes_amount=genes_amount,
                              individuals_amount=individuals_amount, generations_amount=generations_amount)
        min_arr, max_arr, avg_arr = algorithm.run()
        best_result = min(min_arr)
        results.append(best_result)
    min_val = min(results)
    max_val = max(results)
    avg_val = sum(results) / len(results)
    std = statistics.stdev(results)
    print('Min:', min_val)
    print('Max:', max_val)
    print('Avg:', avg_val)
    print('Std:', std)


def hard_roulette():
    print()
    print('\033[92m' + 'Hard [roulette]' + '\033[0m')
    flow_f_name = 'hard_flow.json'
    cost_f_name = 'hard_cost.json'
    machines_amount = 24
    x_dim = 5
    y_dim = 6
    tournament_number = 5
    is_roulette = False
    mutation_probability = 0.2
    genes_amount = 4
    individuals_amount = 100
    generations_amount = 50

    algorithm = Algorithm(flow_f_name=flow_f_name, cost_f_name=cost_f_name, machines_amount=machines_amount,
                          x_dim=x_dim, y_dim=y_dim, tournament_number=tournament_number, is_roulette=is_roulette,
                          mutation_probability=mutation_probability, genes_amount=genes_amount,
                          individuals_amount=individuals_amount, generations_amount=generations_amount)

    min_arr, max_arr, avg_arr = algorithm.run()

    for i in range(len(min_arr)):
        print('Min:', min_arr[i])
        print('Max:', max_arr[i])
        print('Avg:', avg_arr[i])
        print('-------------------')
    print('Minimum of all:', min(min_arr))
    draw_plot(min_arr, max_arr, avg_arr)


def draw_plot(min_arr, max_arr, avg_arr):
    x = range(len(min_arr))
    plt.plot(x, min_arr, label="min")
    plt.plot(x, max_arr, label="max")
    plt.plot(x, avg_arr, label="avg")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    easy_tournament()
    easy_random()
    easy_tournament_10()
    easy_tournament()
    easy_roulette()
    flat_random()
    flat_tournament_10()
    flat_roulette()
    hard_random()
    hard_tournament_10()
    hard_tournament()
    hard_roulette_10()

