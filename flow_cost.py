import numpy as np
import json


class FlowCost:
    def __init__(self, flow_f_name, cost_f_name, amount):
        self.cost_array = self.__create_cost_array(cost_f_name, amount)
        self.flow_array = self.__create_flow_array(flow_f_name, amount)

    @staticmethod
    def __create_cost_array(fname, amount):
        cost_array = np.zeros(shape=(amount, amount), dtype=int)
        file = open('data/' + fname)
        data = json.load(file)
        for i in data:
            cost_array[i['source'], i['dest']] = i['cost']
        file.close()
        return cost_array

    @staticmethod
    def __create_flow_array(fname, amount):
        flow_array = np.zeros(shape=(amount, amount), dtype=int)
        file = open('data/' + fname)
        data = json.load(file)
        for i in data:
            flow_array[i['source'], i['dest']] = i['amount']
        file.close()
        return flow_array

    def get_flow_cost_array(self):
        return self.flow_array * self.cost_array
