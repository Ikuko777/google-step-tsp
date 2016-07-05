#!/usr/bin/env python3

import math
import sys
import itertools

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def sum_distance(solution,cities):
    i = 0
    sum_d = 0.0
    for i in range(len(solution)-1):
        sum_d += distance(cities[solution[i]-1],cities[solution[i+1]-1])
    sum_d +=distance(cities[solution[i+1]-1],cities[solution[0]-1])
    return sum_d



def solve(cities):
    # Build a trivial solution.
    # Visit the cities in the order they appear in the input.
    l = [1, 2, 3, 4, 5]
    elements = []
    min_dis=5000.0
    for element in itertools.permutations(l, 5):
        elements.append(element)

    j=0
    for j in range(len(elements)):
        if min_dis>sum_distance(elements[j],cities):
            min_dis=sum_distance(elements[j],cities)
    return min_dis
        


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print (solution)
    
