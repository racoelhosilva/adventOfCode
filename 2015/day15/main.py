# Advent of Code 2015
# Day 15: Science for Hungry People
# https://adventofcode.com/2015/day/15

import itertools

def a(data):
    ingredients = []
    stats = []
    for line in data:
        fields = line.split(" ")
        ingredients.append(fields[0][:-1])
        stats.append([int(fields[2][:-1]), int(fields[4][:-1]), int(fields[6][:-1]), int(fields[8][:-1])])
    
    maxValue = -1
    for possibility in itertools.combinations_with_replacement(ingredients, 100):
        capacity = durability = flavor = texture = 0
        if (len(set(possibility)) != len(ingredients)):
            continue
        for idx,ingredient in enumerate(ingredients):
            capacity += possibility.count(ingredient) * stats[idx][0]
            durability += possibility.count(ingredient) * stats[idx][1]
            flavor += possibility.count(ingredient) * stats[idx][2]
            texture += possibility.count(ingredient) * stats[idx][3]
        
        capacity = max(capacity, 0)
        durability = max(durability, 0)
        flavor = max(flavor, 0)
        texture = max(texture, 0)
        
        maxValue = max(maxValue, capacity * durability * flavor * texture)
    return maxValue
                
def b(data):    
    ingredients = []
    stats = []
    for line in data:
        fields = line.split(" ")
        ingredients.append(fields[0][:-1])
        stats.append([int(fields[2][:-1]), int(fields[4][:-1]), int(fields[6][:-1]), int(fields[8][:-1]), int(fields[10])])
    
    maxValue = -1
    for possibility in itertools.combinations_with_replacement(ingredients, 100):
        capacity = durability = flavor = texture = calories = 0
        if (len(set(possibility)) != len(ingredients)):
            continue
        for idx,ingredient in enumerate(ingredients):
            capacity += possibility.count(ingredient) * stats[idx][0]
            durability += possibility.count(ingredient) * stats[idx][1]
            flavor += possibility.count(ingredient) * stats[idx][2]
            texture += possibility.count(ingredient) * stats[idx][3]
            calories += possibility.count(ingredient) * stats[idx][4]
        
        if calories != 500:
            continue
        
        capacity = max(capacity, 0)
        durability = max(durability, 0)
        flavor = max(flavor, 0)
        texture = max(texture, 0)
        
        maxValue = max(maxValue, capacity * durability * flavor * texture)
    return maxValue

def test():
    print()
    example = ["Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8","Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"]
    print("Test 1:", "Passed" if a(example) ==  62842880 else "Failed")
    print("Test 2:", "Passed" if b(example) == 57600000 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 15: Science for Hungry People")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day15/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))