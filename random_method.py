import statistics
from flow_cost import FlowCost
from placement_generator import Placement
from evaluation import Evaluation


class RandomMethod:
    def __init__(self, flow_f_name, cost_f_name, machines_amount, x_dim, y_dim, n):
        flow_cost = FlowCost(flow_f_name=flow_f_name, cost_f_name=cost_f_name, amount=machines_amount)
        self.flow_cost_array = flow_cost.get_flow_cost_array()
        self.machines_amount = machines_amount
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.n = n

    def run(self):
        placement = Placement(amount=self.machines_amount, x=self.x_dim, y=self.y_dim)
        results = []
        for i in range(self.n):
            random_placement = placement.generate_random_placement()
            evaluation = Evaluation(placement_array=random_placement, amount=self.machines_amount,
                                    flow_cost_array=self.flow_cost_array)
            results.append(evaluation.count_cost())

        min_val = min(results)
        max_val = max(results)
        avg_val = sum(results) / len(results)
        st_dev = statistics.stdev(results)
        return min_val, max_val, avg_val, st_dev
