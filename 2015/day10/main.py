# Advent of Code 2015
# Day 10: Elves Look, Elves Say
# https://adventofcode.com/2015/day/10

import itertools

def hardcode(data, num):
    current = data[0]
    for _ in range(num):
        nextValue = ""
        prev = ""
        count = 0
        for char in current:
            if char != prev:
                if count > 0:
                    nextValue += str(count)
                    nextValue += prev
                prev = char
                count = 1
            else:
                count += 1
        nextValue += str(count)
        nextValue += prev
        current = nextValue
    
    return len(current)
    
def shortcut(data, num):
    current = data[0]
    for _ in range(num):
        nextValue = ""
        for key, group in itertools.groupby(current):
            nextValue += str(len(list(group)))
            nextValue += str(key)
        current = nextValue 
    return len(current)

def test():
    print()
    print("Test 1:", "Passed" if hardcode(["1"],5) == 6 else "Failed")
    print("Test 2:", "Passed" if shortcut(["1"],5) == 6 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 10: Elves Look, Elves Say")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day10/input.txt", "r").read().splitlines()
    test()
    print("Part a:", hardcode(data, 40))
    print("Part b:", shortcut(data, 50))