# Advent of Code 2015
# Day 24: It Hangs in the Balance
# https://adventofcode.com/2015/day/24

import itertools, numpy

def a(data):
    data = [int(x) for x in data]
    target = sum(data) / 3
    largest = max(data)
    base = int(target / largest)
    solutions = []
    while (len(solutions) == 0):
        solutions = list(filter(lambda x: sum(x) == target, itertools.combinations(data, base)))
        base += 1
    solutions = min([numpy.prod(x) for x in solutions])
    return solutions
                
def b(data):    
    data = [int(x) for x in data]
    target = sum(data) / 4
    largest = max(data)
    base = int(target / largest)
    solutions = []
    while (len(solutions) == 0):
        solutions = list(filter(lambda x: sum(x) == target, itertools.combinations(data, base)))
        base += 1
    solutions = min([numpy.prod(x) for x in solutions])
    return solutions

def test():
    print()
    print("Test 1:", "Passed" if a([str(x) for x in range(6)] + [str(x) for x in range(7,12)]) == 99 else "Failed")
    print("Test 2:", "Passed" if b([str(x) for x in range(6)] + [str(x) for x in range(7,12)]) == 44 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 24: It Hangs in the Balance")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day24/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))