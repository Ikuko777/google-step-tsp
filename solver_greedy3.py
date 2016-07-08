#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)



def opt_2(size, path,dist):
    total = 0
    while True:
        count = 0
        for i in xrange(size - 2):
            i1 = i + 1
            for j in xrange(i + 2, size):
                if j == size - 1:
                    j1 = 0
                else:
                    j1 = j + 1
                if i != 0 or j1 != 0:
                    l1 = dist[path[i]][path[i1]]
                    l2 = dist[path[j]][path[j1]]
                    l3 = dist[path[i]][path[j]]
                    l4 = dist[path[i1]][path[j1]]
                    if l1 + l2 > l3 + l4:
                        #reconnect
                        new_path = path[i1:j+1]
                        path[i1:j+1] = new_path[::-1]
                        count += 1
        total += count
        if count == 0: break
    return path

def or_opt(size, path,dist):
    global distance_table
    total = 0
    while True:
        count = 0
        for i in xrange(size):
            #
            i0 = i - 1
            i1 = i + 1
            if i0 < 0: i0 = size - 1
            if i1 == size: i1 = 0
            for j in xrange(size):
                j1 = j + 1
                if j1 == size: j1 = 0
                if j != i and j1 != i:
                    l1 = dist[path[i0]][path[i]]  # i0 - i - i1
                    l2 = dist[path[i]][path[i1]]
                    l3 = dist[path[j]][path[j1]]  # j - j1
                    l4 = dist[path[i0]][path[i1]] # i0 - i1
                    l5 = dist[path[j]][path[i]]   # j - i - j1
                    l6 = dist[path[i]][path[j1]] 
                    if l1 + l2 + l3 > l4 + l5 + l6:
                        p = path[i]
                        path[i:i + 1] = []
                        if i < j:
                            path[j:j] = [p]
                        else:
                            path[j1:j1] = [p]
                        count += 1
        total += count
        if count == 0: break
    return path

def solve(cities):
    N = len(cities)
    adj = N*[0]

    dist = [[0] * N for i in range(N)]
    dist2 = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist2[i][j] = dist2[j][i] = distance(cities[i], cities[j])


    for i in range(N):
        adj[i]=0
        for j in range(N):
            adj[i]+=distance(cities[i],cities[j])
            
        adj[i]=adj[i]/(N-1)

    for i in range(N):
        for j in range(N):
            dist[i][j] = distance(cities[i],cities[j])-(adj[i]+adj[j]) 
            dist[j][i] = distance(cities[j],cities[i])-(adj[j]+adj[i])

    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]




    def distance_from_current_city(to):
        return dist[current_city][to]


    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city

    solution=opt_2(N,solution,dist2)
    solution=or_opt(N,solution,dist2)
    return solution



def sum_distance(solution,cities):
    i = 0
    sum_d = 0.0
    for i in range(len(solution)-1):
        sum_d += distance(cities[solution[i]],cities[solution[i+1]])
    sum_d +=distance(cities[solution[i+1]],cities[solution[0]])
    return sum_d


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))

    print sum_distance(solution,read_input(sys.argv[1]))
