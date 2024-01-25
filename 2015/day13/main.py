# Advent of Code 2015
# Day 13: Knights of the Dinner Table
# https://adventofcode.com/2015/day/13

import itertools
 
def a(data):
    helper = dict()
    people = set()
    for line in data:
        fields = line[:-1].split(" ")
        person1, person2 = fields[0], fields[-1]
        happiness = int(fields[3]) if fields[2] == "gain" else -int(fields[3])
        helper[(person1, person2)] = happiness
        people.add(person1)
    maxValue = 0
    for arrangement in itertools.permutations(people):
        total = 0
        for i in range(-1, len(arrangement)-1):
            total += helper[(arrangement[i], arrangement[i+1])]
            total += helper[(arrangement[i+1], arrangement[i])]
        if total > maxValue:
            maxValue = total
    return maxValue
                
def b(data):    
    helper = dict()
    people = set()
    for line in data:
        fields = line[:-1].split(" ")
        person1, person2 = fields[0], fields[-1]
        happiness = int(fields[3]) if fields[2] == "gain" else -int(fields[3])
        helper[(person1, person2)] = happiness
        people.add(person1)
    for person in people:
        helper[(person, "Rodrigo")] = 0
        helper[("Rodrigo", person)] = 0
    people.add("Rodrigo")
    maxValue = 0
    for arrangement in itertools.permutations(people):
        total = 0
        for i in range(-1, len(arrangement)-1):
            total += helper[(arrangement[i], arrangement[i+1])]
            total += helper[(arrangement[i+1], arrangement[i])]
        if total > maxValue:
            maxValue = total
    return maxValue

def test():
    print()
    example = ["Alice would gain 54 happiness units by sitting next to Bob.","Alice would lose 79 happiness units by sitting next to Carol.","Alice would lose 2 happiness units by sitting next to David.","Bob would gain 83 happiness units by sitting next to Alice.","Bob would lose 7 happiness units by sitting next to Carol.","Bob would lose 63 happiness units by sitting next to David.","Carol would lose 62 happiness units by sitting next to Alice.","Carol would gain 60 happiness units by sitting next to Bob.","Carol would gain 55 happiness units by sitting next to David.","David would gain 46 happiness units by sitting next to Alice.","David would lose 7 happiness units by sitting next to Bob.","David would gain 41 happiness units by sitting next to Carol."]
    print("Test 1:", "Passed" if a(example) == 330 else "Failed")
    print("Test 2:", "Passed" if b(example) == 286 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 13: Knights of the Dinner Table")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day13/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))