# Advent of Code 2015
# Day 09: All in a Single Night
# https://adventofcode.com/2015/day/9

import itertools, sys

def a(data):
    places = set()
    helper = dict()
    for line in data:
        source, _1, dest, _2, distance = line.split(" ")
        helper[(source, dest)] = int(distance)
        helper[(dest, source)] = int(distance)
        places.add(source)
        places.add(dest)
    
    minDistance = sys.maxsize
    for order in itertools.permutations(places):
        total = sum([helper[pair] for pair in zip(order[:-1], order[1:])])
        minDistance = min(minDistance, total)      
    return minDistance
                
def b(data):    
    places = set()
    helper = dict()
    for line in data:
        source, _1, dest, _2, distance = line.split(" ")
        helper[(source, dest)] = int(distance)
        helper[(dest, source)] = int(distance)
        places.add(source)
        places.add(dest)
    
    maxDistance = 0
    for order in itertools.permutations(places):
        total = sum([helper[pair] for pair in zip(order[:-1], order[1:])])
        maxDistance = max(maxDistance, total)      
    return maxDistance

def test():
    print()
    print("Test 1:", "Passed" if a(["London to Dublin = 464","London to Belfast = 518","Dublin to Belfast = 141"]) == 605 else "Failed")
    print("Test 2:", "Passed" if b(["London to Dublin = 464","London to Belfast = 518","Dublin to Belfast = 141"]) == 982 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 09: All in a Single Night")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day09/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))