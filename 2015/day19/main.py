# Advent of Code 2015
# Day 19: Medicine for Rudolph
# https://adventofcode.com/2015/day/19

import re

def a(data):
    helper = dict()
    target = data[-1]
    for line in data[:-2]:
        fields = line.split(" ")
        if fields[0] in helper.keys():
            helper[fields[0]] = helper[fields[0]] + [fields[-1]]
        else:
            helper[fields[0]] = [fields[-1]] 

    results = set()
    for key, value in helper.items():
        for match in re.finditer(key, target):
            for rep in value:
                new = target[0:match.start()] + rep + target[match.end():]
                results.add(new)

    return len(results)

def b(data):  
    helper = dict()
    target = data[-1]
    for line in data[:-2]:
        fields = line.split(" ")
        if fields[0] in helper.keys():
            helper[fields[0]] = helper[fields[0]] + [fields[-1]]
        else:
            helper[fields[0]] = [fields[-1]] 
    
    counter = 0
    while target != "e":
        shortest_len = float('inf')
        shortest = target
        for key, value in helper.items():
            for option in value:
                for match in re.finditer(option, target):
                    undo = target[:match.start()] + key + target[match.end():]
                    if len(undo) < shortest_len:
                        shortest_len = len(undo)
                        shortest = undo
        target = shortest
        counter += 1
    return counter  

def b2(data):
    MOLECULE = data[-1]
    elements = len(re.findall(r'[A-Z]', MOLECULE))
    rn = len(re.findall(r'Rn', MOLECULE))
    ar = len(re.findall(r'Ar', MOLECULE))
    y = len(re.findall(r'Y', MOLECULE))
    return elements - (rn + ar) - (2 * y) - 1

def test():
    print()
    print("Test 1:", "Passed" if a(["H => HO","H => OH","O => HH", "", "HOH"]) == 4 else "Failed")
    print("Test 2:", "Passed" if a(["H => HO","H => OH","O => HH", "", "HOHOHO"]) == 7 else "Failed")
    print("Test 3:", "Passed" if b(["e => H","e => O","H => HO","H => OH","O => HH", "", "HOH"]) == 3 else "Failed")
    print("Test 4:", "Passed" if b(["e => H","e => O","H => HO","H => OH","O => HH", "", "HOHOHO"]) == 6 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 19: Medicine for Rudolph")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day19/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))