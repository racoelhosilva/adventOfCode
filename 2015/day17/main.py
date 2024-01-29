# Advent of Code 2015
# Day 17: No Such Thing as Too Much
# https://adventofcode.com/2015/day/17

def a(sizesAvailable, remaining):
    if remaining < 0: 
        return 0
    if remaining == 0:
        return 1
    if len(sizesAvailable) == 0:
        return 0
    
    options = 0
    for idx, size in enumerate(sizesAvailable):
        options += a(sizesAvailable[idx+1:], remaining - size)
    return options

def helper(sizesAvailable, remaining):
    if remaining < 0:
        return []
    if remaining == 0:
        return [[]]
    if len(sizesAvailable) == 0:
        return []
    
    options = []
    for idx, size in enumerate(sizesAvailable):
        result = helper(sizesAvailable[idx+1:], remaining - size)
        for solution in result:
            options.append([size] + solution)
            
    return options

def b(sizesAvailable, remaining):  
    solutions = helper(sizesAvailable, remaining)
    return len(list(filter(lambda x: len(x) == min(list(map(lambda x: len(x), solutions))), solutions)))

def test():
    print()
    print("Test 1:", "Passed" if a([20,15,10,5,5], 25) == 4 else "Failed")
    print("Test 2:", "Passed" if b([20,15,10,5,5], 25) == 3 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 17: No Such Thing as Too Much")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day17/input.txt", "r").read().splitlines()
    data = [int(n) for n in data]
    test()
    print("Part a:", a(data, 150))
    print("Part b:", b(data, 150))